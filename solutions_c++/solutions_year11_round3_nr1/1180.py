#include <cstring>
#include <stdio.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <climits>
#include <cctype>

using namespace std;

#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz(v) ((int)v.size())
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define pb push_back

typedef stringstream ss;
typedef long long ll;
typedef pair<int, int> pii;
typedef long double ld;

const int oo = (int) 1e9;
const double PI = 2 * acos(0.0);
const double eps = 1e-9;

int compFloats(const double &a, const double &b) {
  if (fabs(a - b) < eps)
    return 0;
  return a > b ? 1 : -1;
}



int grid[60][60]; //, 1 is blue , 2 is white , 3 is red
int rows,clmns;

bool valid(int i,int j)
{
	if(i>=0 && j>=0 && i<rows && j<clmns && grid[i][j]==1)
		return true;
	return false;
}

void calc()
{
	for (int i = 0; i < rows; ++i) {
		for (int j = 0; j < clmns; ++j) {
			if(grid[i][j]==1)
			{
				if(valid(i,j) && valid(i+1,j+1) && valid(i,j+1) && valid(i+1,j))
				{
					grid[i][j] = (int)'/';
					grid[i][j+1] = (int)'\\';
					grid[i+1][j] = (int)'\\';
					grid[i+1][j+1] = (int)'/';
				}
			}
		}
	}
}

void printGrid()
{
	for (int i = 0; i < rows; ++i) {
		for (int j = 0; j < clmns; ++j) {
			if(grid[i][j]==2)
				cout<<".";
			else
				cout<<(char)grid[i][j];
		}
		cout<<endl;
	}
}

int main()
{
	freopen("a_large.in","r",stdin);
	freopen("a_large.out","w",stdout);
	int tc;
	char dummy;
	cin>>tc;
	bool flag;
	for (int i = 1; i <=  tc; ++i) {
		flag = true;
		memset(grid,0,sizeof(grid));
		cout<<"Case #"<<i<<":"<<endl;
		cin>>rows>>clmns;
		for (int ii = 0; ii < rows; ++ii) {
			for (int jj = 0; jj < clmns; ++jj) {
				cin>>dummy;
				if(dummy=='#')
				{
					flag = false;//blue found
					grid[ii][jj] = 1;
				}
				else
					grid[ii][jj] = 2;
			}
		}
		if(flag)//no blue
		{
			for (int ii = 0; ii < rows; ++ii) {
				for (int jj = 0; jj < clmns; ++jj) {
					cout<<".";
				}
				cout<<endl;
			}
			continue;
		}
		calc();
		flag = true;
		for (int ii = 0; ii < rows; ++ii)
			for (int jj = 0; jj < clmns; ++jj)
				if(grid[ii][jj]==1)
					flag = false;

		if(flag)
			printGrid();
		else
			cout<<"Impossible"<<endl;
	}
	return 0;
}
