#include <stdio.h>
#include <tchar.h>
#include <iostream>
#include <fstream>
#include <string>
#include <typeinfo>

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

bool check(int A, int B);

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
		for (int k = 1; k <= T; ++k)
		{
			auto A1 = r.get<int>();
			auto A2 = r.get<int>();
			auto B1 = r.get<int>();
			auto B2 = r.get<int>();
			int count = 0;
			for (int i = A1; i <= A2; ++i)
			{
				for (int j = B1; j <= B2; ++j)
				{
					if (check(i,j))
					{
						++count;
					}
				}
			}
			outFile << "Case #" << k << ": " << count << endl;
		}
	}
	catch (const std::exception& e)
	{
		std::cout << "exception [" << typeid(e).name() << "] " << (e.what() ? e.what() : "no description") << std::endl;
		return -4;
	}
	return 0;
}

bool check(int A, int B)
{
	if (A < B)
	{
		swap(A, B);
	}
	int k = A/B;
	if (k != 1)
		return true;
	int r = A % B;
	if (r == 0)
		return false;
	return !check(B, r);
}
