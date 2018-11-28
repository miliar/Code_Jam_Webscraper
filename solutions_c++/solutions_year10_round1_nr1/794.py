#include <fstream>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <string>
#include <queue>
#include <stack>

using namespace std;

//const string PATH = "A-small-attempt0";
const string PATH = "A-large";
//const string PATH = "A";

int color(const vector<string> &b, int r, int c)
{
	if(c >= 0 && c < b.size())
	{
		if(r >= 0 && r < b[c].size())
		{
			if(b[c][r] == 'R')
			{
				return 1;
			}
			else if(b[c][r] == 'B')
			{
				return 2;
			}
		}
	}
	return 0;
}

int kInRow(const vector<string> &b, int K, int N)
{
	int ret = 0;
	for(int r = 0; r < N; r++)
	{
		for(int c = 0; c < N; c++)
		{
			int colAcross = color(b, r, c);
			int colUp = colAcross;
			int colDiagLeft = colUp;
			int colDiagRight = colDiagLeft;
			for(int i = 1; i < K; i++)
			{
				if(colAcross != color(b, r, c + i))
				{
					colAcross = 0;
				}
				if(colUp != color(b, r + i, c))
				{
					colUp = 0;
				}
				if(colDiagLeft != color(b, r + i, c - i))
				{
					colDiagLeft = 0;
				}
				if(colDiagRight != color(b, r + i, c + i))
				{
					colDiagRight = 0;
				}
			}
			ret |= colAcross;
			ret |= colUp;
			ret |= colDiagLeft;
			ret |= colDiagRight;
		}
	}
	return ret;
}

int main()
{
	stringstream inPath;
	inPath << PATH.c_str() << ".in";
	stringstream outPath;
	outPath << PATH.c_str() << ".out";
	ifstream inFile(inPath.str());
	ofstream outFile(outPath.str());
	int T;
	inFile >> T;
	for(int i = 0; i < T; i++)
	{
		int N, K;
		inFile >> N >> K;
		vector<string> b(N);
		for(int j = 0; j < N; j++)
		{
			inFile >> b[j];
			stringstream temp;
			for(int k = 0; k < b[j].size(); k++)
			{
				if(b[j][k] != '.')
				{
					temp << b[j][k];
				}
			}
			b[j] = temp.str();
			reverse(b[j].begin(), b[j].end());
		}
		reverse(b.begin(), b.end());
		int ret = kInRow(b, K, N);
		if(ret == 0)
		{
			outFile << "Case #" << (i+1) << ": " << "Neither" << endl;
		}
		else if(ret == 1)
		{
			outFile << "Case #" << (i+1) << ": " << "Red" << endl;
		}
		else if(ret == 2)
		{
			outFile << "Case #" << (i+1) << ": " << "Blue" << endl;
		}
		else if(ret == 3)
		{
			outFile << "Case #" << (i+1) << ": " << "Both" << endl;
		}
	}
	inFile.close();
	outFile.close();
	return 0;
}