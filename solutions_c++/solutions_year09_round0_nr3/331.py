#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <iomanip>
using namespace std;

ifstream fin("C-large.in");
FILE* fout;

string patternStr = "welcome to code jam";
int patternLen = patternStr.length();

void solve(int caseNum)
{
	string line;
	getline(fin, line);
	int lineLen = line.length();
	long count[501][20];
	count[0][0] = (patternStr[0] == line[0]) ? 1 : 0;
	for (int i=1; i<lineLen; i++)
		count[i][0] = (line[i] == patternStr[0]) ? count[i-1][0]+1 : count[i-1][0];
	for (int j=1; j<patternLen; j++)
	{
		for (int i=0; i<j; i++)
			count[i][j] = 0;
		for (int i=j; i<lineLen; i++)
		{
			if (line[i] != patternStr[j])
				count[i][j] = count[i-1][j];
			else
				count[i][j] = (count[i-1][j] + count[i-1][j-1]) % 10000;
		}
	}
	fprintf(fout, "Case #%d: %4.4d\n", caseNum, count[lineLen-1][patternLen-1]);
	
}

int main() 
{
	fout = fopen("C-large.out", "w");
	int T;
	fin >> T;
	fin.get();
	for (int i=1; i<=T; i++) 
		solve(i);
	fin.close();
	fclose(fout);
}