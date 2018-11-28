#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <numeric>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <utility>
using namespace std;

typedef int uint;
class DisjointSet
{
private:
	std::vector<int> _parentVector;
	std::vector<int> _rankVector;
	uint _distinctSets;

public:
	DisjointSet(uint n) : _parentVector(n), _rankVector(n), _distinctSets(n)
	{
		for (uint i = 0; i < n; ++i)
			_parentVector[i] = i;
	}

	uint Find(uint n)
	{
		if (_parentVector[n] == n)
			return n;
		
		return (_parentVector[n] = Find(_parentVector[n]));
	}

	void Union(uint n, uint m)
	{
		n = Find(n);
		m = Find(m);
		if (_rankVector[n] > _rankVector[m])
			_parentVector[m] = n;
		else if (_rankVector[n] < _rankVector[m])
			_parentVector[n] = m;
		else if (n != m)
		{
			_parentVector[m] = n;
			++_rankVector[n];
		}

		if (n != m)
			--_distinctSets;
	}

	uint DistinctSets() const
	{
		return _distinctSets;
	}
};
struct Matrix
{
	int* _data;
	int _rows, _cols;
	
	Matrix(int rows, int cols) : _data(new int[rows * cols]), _rows(rows), _cols(cols)
	{
	}

	~Matrix()
	{
		delete [] _data;
	}

	int& operator()(int r, int c)
	{
		return _data[r * _cols + c];
	}

	int operator()(int r, int c) const
	{
		return _data[r * _cols + c];
	}
};
struct GuardMatrix
{
	int* _data;
	int _rows, _cols;

	int _guard;
	
	GuardMatrix(int rows, int cols) : _data(new int[rows * cols]), _rows(rows), _cols(cols), _guard(1000000000)
	{
	}

	~GuardMatrix()
	{
		delete [] _data;
	}

	int& operator()(int r, int c)
	{
		if (r >= _rows || c >= _cols || r < 0 || c < 0)
			return _guard;

		return _data[r * _cols + c];
	}

	int operator()(int r, int c) const
	{
		if (r >= _rows || c >= _cols || r < 0 || c < 0)
			return _guard;

		return _data[r * _cols + c];
	}
};

struct Pattern
{
    vector<string> letters;

	Pattern(string line)
	{
		for (int i = 0; i < line.size(); ++i)
		{
			if (line[i] == '(')
			{
				letters.push_back("");
				while (line[++i] != ')')
				{
					letters.back().append(string(1, line[i]));
				}
			}
			else
			{
				letters.push_back(string(1, line[i]));
			}
		}
	}
    
    bool Match(string word)
    {
        for (int i = 0; i < word.size(); ++i)
		{
			if (letters[i].find(word[i]) == string::npos)
				return false;
		}
		return true;
    }
};

void Alien()
{
	int L, D, N;
	ifstream cin("A-small.in");
	ofstream cout("Aout.txt");

	cin >> L >> D >> N;
	vector<string> words;
	string tmp;
	getline(cin, tmp);
	while (D-- > 0)
	{
		getline(cin, tmp);
		words.push_back(tmp);
	}

	for (int i = 1; i <= N; ++i)
	{
		int count = 0;
		getline(cin, tmp);
		Pattern p(tmp);
		for (int j = 0; j < words.size(); ++j)
			if (p.Match(words[j]))
				++count;

		cout << "Case #" << i << ": " << count << endl; 
	}
}

int CountMatches(string small, string big)
{
	Matrix M(small.size(), big.size());
	
	// Set first column to 0
	for (int i = 0; i < M._rows; ++i)
		M(i, 0) = 0;

	// Except perhaps the first entry
	if (big[0] == small[0])
		M(0, 0) = 1;

	// Fill in matrix
	for (int col = 1; col < M._cols; ++col)
	{
		// Treat first row specially
		M(0, col) = M(0, col - 1);
		if (big[col] == small[0])
			M(0, col) = (M(0, col) + 1) % 1000;

		for (int row = 1; row < M._rows; ++row)
		{
			M(row, col) = M(row, col - 1);

			// Check if we add any other possibilities
			if (big[col] == small[row])
				M(row, col) = (M(row, col) + M(row - 1, col - 1)) % 1000;
		}
	}

	return M(small.size() - 1, big.size() - 1);
}

void Welcome()
{
	int N;
	ifstream cin("C-small.in"); ofstream cout("Cout.txt");

	cin >> N;

	string s;
	getline(cin, s);
	for (int i = 1; i <= N; ++i)
	{
		getline(cin, s);
		int count = CountMatches("welcome to code jam", s);
		cout << "Case #" << i << ": " << setw(4) << setfill('0') << count << endl; 
	}
}

void Basin()
{	
	ofstream cout("Bout");
	int N;
	ifstream cin("B-small.in");

	cin >> N;
	for (int i = 1; i <= N; ++i)
	{
		int H, W;
		cin >> H >> W;
		GuardMatrix M(H, W);
		int j = 0;
		while (j < H * W)
		{
			cin >> M._data[j++];
		}
		Matrix L(H, W);
		fill(L._data, L._data + (H * W), -1);
		int curLabel = -1;
		for (int row = 0; row < M._rows; ++row)
		{
			for (int col = 0; col < M._cols; ++col)
			{
				// Find min
				int minVal = M(row, col);
				int minRow = row, minCol = col;

				if (M(row + 1, col ) <= minVal) { minVal = M(row+1, col); minRow = row + 1; minCol = col ; }
				if (M(row , col + 1) <= minVal) { minVal = M(row, col+1); minRow = row ; minCol = col + 1; }
				if (M(row , col - 1) <= minVal) { minVal = M(row, col-1); minRow = row ; minCol = col - 1; }
				if (M(row - 1, col ) <= minVal) { minVal = M(row-1, col); minRow = row - 1; minCol = col ; }
				if (M(row , col ) <= minVal) { minVal = M(row, col); minRow = row ; minCol = col ; }

				// If we are a sink, make a new label (if needed)
				if (minRow == row && minCol == col)
				{
					if (L(row, col) == -1)
						L(row, col) = ++curLabel;
				} 
				else if (L(minRow, minCol) > -1) 
				{
					// If this was processed *before* this cell, take their label
					L(row, col) = L(minRow, minCol);
				}
				else
				{
					// This will be processed *after*, so give them a label
					L(row, col) = ++curLabel;
					L(minRow, minCol) = L(row, col);
				}

			}
		}
		cout << "Case #" << i << ": "  << endl; 
		for (int row = 0; row < M._rows; ++row)
		{
			for (int col = 0; col < M._cols; ++col)
			{
				cout << ((char)('a' + L(row ,col)));
				if (col + 1 < M._cols) cout << ' ';
			}
			cout << endl;
		}
	}
}

int main()
{
	//Alien();
	Welcome();
	//Basin();
	//while (true) ;
}