#include <stdio.h>
#include <tchar.h>
#include <iostream>
#include <fstream>
#include <string>
#include <typeinfo>
#include <vector>
#include <assert.h>

class stream_reader
{
public:
	stream_reader(std::istream& s) : s_(s) {}
	template <typename T> T get()
	{
		T v;
		s_ >> v;
		if (s_.fail())
		{
			throw std::exception("Failed to read from a stream");
		}
		return v;
	}
private:
	std::istream& s_;
};


using namespace std;

void PrintUsage(const char* exeName)
{
	cout << "Usage: " << exeName << " infile [outfile]" << endl;
}


struct chains
{
	chains(int fromLeft, int fromUp, int fromUpLeft, int fromUpRight)
		: fromLeft_(fromLeft), fromUp_(fromUp), fromUpLeft_(fromUpLeft), fromUpRight_(fromUpRight) {}
	chains() : fromLeft_(0), fromUp_(0), fromUpLeft_(0), fromUpRight_(0) {}
	int fromLeft_;
	int fromUp_;
	int fromUpLeft_;
	int fromUpRight_;
};

int main(int argc, char* argv[])
{
	if (argc < 2)
	{
		PrintUsage(argv[0]);
		return -1;
	}
	string inName = argv[1];
	
	string outName = argc > 2 ? argv[2] : inName + ".out";
	
	ifstream inFile(inName);
	if (!inFile.is_open())
	{
		cout << "Bad input file: " << inName.c_str() << endl;
		return -2;
	}
	ofstream outFile(outName);
	if (!outFile.is_open())
	{
		cout << "Bad output file: " << outName.c_str() << endl;
		return -3;
	}

	try
	{
		stream_reader r(inFile);
		auto T = r.get<int>();
		cout << "Number of cases: " << T;
		for (int i = 1; i <= T; ++i)
		{
			auto N = r.get<int>(); //board size
			auto K = r.get<int>(); //win sequence len
			vector<char> board0(N * N);
			int rStart = N; //rEnd always = N-1 except an empty board
			int cStart = N; int cEnd = N;
			int rowIdx0 = 0;
			for (int r = 0; r < N; ++r)
			{
				for (int c = 0; c < N; ++c)
				{
					char piece;
					inFile >> piece;
					if (piece != '.')
					{
						board0[rowIdx0 + c] = piece;
						if (r < rStart)
						{
							rStart = r;
						}
						if (c < cStart)
						{
							cStart = c;
						}
					}
				}
				rowIdx0 += N;
			}
			if (rStart == N) //empty board
			{
				outFile << "Case #" << i << ": " << "Neither" << endl;
				continue;
			}
			//rotate and optimize
			int rows = cEnd - cStart + 1;
			int columns = N - rStart + 2;
			vector<char> board(rows * columns);
			for (int c = 1; c < columns - 1; ++c)
			{
				int r = rows - 1;
				int j = cEnd - 1;
				int origRowIdx = (N - c) * N;

				while (board0[origRowIdx + j] == 0 && j >= cStart)
				{
					--j;
				}
				while (j >= cStart)
				{
					char tmp = board0[origRowIdx + j];
					if (tmp != 0)
					{
						board[r * columns + c] = tmp;
						--r;
					}
					--j;
				}
			}
			// use wave algo
			vector<chains> reds(rows * columns);
			vector<chains> blues(rows * columns);			
			int maxReds = 0;
			int maxBlues = 0;
			int rowIdx = columns;
			for (int r = 1; r < rows; ++r)
			{				
				for (int c = 1; c < columns - 1; ++c)
				{
					vector<chains>* v;
					int* max;
					switch (board[rowIdx + c])
					{
					case 'B':
						{
							v = &blues;
							max = &maxBlues;
						}
						break;
					case 'R':
						{
							v = &reds;
							max = &maxReds;
						}
						break;
					default:
						continue;
					}
					chains t;
					t.fromUp_ = (*v)[rowIdx - columns + c].fromUp_ + 1;
					if (t.fromUp_ > *max)
						*max = t.fromUp_;
					t.fromLeft_ = (*v)[rowIdx + c - 1].fromLeft_ + 1;
					if (t.fromLeft_ > *max)
						*max = t.fromLeft_;
					t.fromUpLeft_ = (*v)[rowIdx - columns + c - 1].fromUpLeft_ + 1;
					if (t.fromUpLeft_ > *max)
						*max = t.fromUpLeft_;
					t.fromUpRight_ = (*v)[rowIdx - columns + c + 1].fromUpRight_ + 1;
					if (t.fromUpRight_ > *max)
						*max = t.fromUpRight_;
					(*v)[rowIdx + c] = t;
				}
				rowIdx += columns;
			}
			const char* answer = maxBlues >= K ? (maxReds >= K ? "Both" : "Blue") : (maxReds >= K ? "Red" : "Neither");
			outFile << "Case #" << i << ": "
					<< answer << endl;
		}
	}
	catch (const std::exception& e)
	{
		std::cout << "exception [" << typeid(e).name() << "] " << (e.what() ? e.what() : "no description") << std::endl;
		return -4;
	}
	return 0;
}
