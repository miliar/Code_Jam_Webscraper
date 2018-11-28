#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
#include<string>
#include<set>
#include<numeric>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<bitset>
#include<queue>
#include<ctime>
#include<sstream>
#include<map>
using namespace std;
typedef long long ll;
const double EPS = 1e-9;
int nextint(){int a;scanf("%d",&a);return a;}
double nextdouble(){double a;scanf("%lf",&a);return a;}
bool equal(double a, double b){return fabs(a-b)<EPS;}

bool isWin(char c, vector<string> &g)
{
	for(int i = 0; i < 4; i++)
	{
		bool ok = true;
		for(int j = 0; j < 4; j++)
			if(g[i][j] != c && g[i][j] != 'T')
				ok = false;
		if(ok) return true;
	}

	for(int i = 0; i < 4; i++)
	{
		bool ok = true;
		for(int j = 0; j < 4; j++)
			if(g[j][i] != c && g[j][i] != 'T')
				ok = false;
		if(ok) return true;
	}

	bool ok = true;
	for(int i = 0; i < 4; i++)
		if(g[i][i] != c && g[i][i] != 'T')
			ok = false;
	if(ok) return true;

	ok = true;
	for(int i = 0; i < 4; i++)
		if(g[i][3-i] != c && g[i][3-i] != 'T')
			ok = false;
	if(ok) return true;

}

int main()
{
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int t = nextint();
	for(int test = 1; test <= t; test++)
	{
		vector<string> g(4);
		for(int i = 0; i < 4; i++)
			cin >> g[i];

		bool filled = true;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				if(g[i][j] == '.')
					filled = false;
		bool xWin = isWin('X', g);
		bool oWin = isWin('O', g);

		if(xWin && oWin)
			cout << "Case #" << test << ": Draw" << endl;
		else if(xWin)
			cout << "Case #" << test << ": X won" << endl;
		else if(oWin)
			cout << "Case #" << test << ": O won" << endl;
		else if(filled)
			cout << "Case #" << test << ": Draw" << endl;
		else
			cout << "Case #" << test << ": Game has not completed" << endl;


	}


	return 0;
}