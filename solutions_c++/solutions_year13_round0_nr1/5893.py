#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

bool CheckComplete(vector<vector<char> > vec)
{
	for(int i=0;i<vec.size();i++)
	{
		for(int j=0;j<vec[i].size();j++)
		{
			if(vec[i][j] == '.') return false;
		}
	}
	return true;
}

bool CheckWin(vector<vector<char> > vec, char c)
{
	map<int,int> countRow, countColumn;

	for(int i=0;i<vec.size();i++)
	{
		for(int j=0;j<vec[i].size();j++)
		{
			if(vec[i][j] == c || vec[i][j] == 'T')
			{	
				countRow[i]++;
				countColumn[j]++;
			}
		}
	}

	bool RowWin = false;
	bool ColumnWin = false;

	for(int i=0;i<4;i++)
	{
		if(countRow[i] == 4) return true;
		if(countColumn[i] == 4) return true;
	}

	int Diagonal = 0;
	int AntiDiagonal = 0;

	for(int i=0;i<4;i++)
	{
		if(vec[i][i] == c || vec[i][i] == 'T')
			Diagonal++;
	}

	if(Diagonal == 4) return true;

	for(int i=0;i<4;i++)
	{
		if(vec[i][4-i-1] == c || vec[i][4-i-1] == 'T')
			AntiDiagonal++;
	}

	if(AntiDiagonal == 4) return true;

	return false;

}

int main() {
	
	ifstream cin("A-large.in");
	ofstream cout("output.txt");

	int t;
	cin >> t;

	for(int cs=1;cs<=t;cs++)
	{

		vector<vector<char> > vec;

		for(int i=0;i<4;i++)
		{
			vector<char> vt;

			for(int j=0;j<4;j++)
			{
				char c;
				cin >> c;
				vt.push_back(c);
			}

			vec.push_back(vt);
		}

		if(CheckWin(vec,'X'))
			cout << "Case #" << cs << ": X won" << endl;
		else if(CheckWin(vec,'O'))
			cout << "Case #" << cs << ": O won" << endl;
		else if(CheckComplete(vec))
			cout << "Case #" << cs << ": Draw" << endl;
		else
			cout << "Case #" << cs << ": Game has not completed" << endl;
			
		

	}

	
}
