#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <deque>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <queue>
#include <complex>
#include <queue>
#include <string.h>
#include <fstream>
using namespace std;

#define IT(c) typeof((c).begin())

#define FOR(i, a, b) for(int (i) =  int(a); i < int(b); ++i)
#define REP(x, n) FOR(x,0,n)
#define FORIT(c, i) for(IT(c) i = (c).begin(); i != (c).end(); ++i)

#define bound(num, lower, upper) (max(min((num),((upper)-1)),(lower)))
#define debug(x) cerr << #x << " = " << x << "\n"

#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()


typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<string> vs;
typedef pair<int, int> ii;

/*==================================================================================================================*/

int main()
{
int np; cin >> np;
for(int p = 0; p < np; p++)
{
	int n, k; cin >> n >> k;
	int o[50][50];
	for(int r = 0; r < n; r++)
	{
		string s; cin >> s;
		for(int c = 0; c < n; c++)
		{
			o[r][c] = s[c];
		}
	}
	
	vector<vector<int> > r(n, vector<int>());
	for(int i = 0; i < n; i++)
		for(int c = n-1; c >= 0; c--)
			if(o[i][c] != '.')
				r[i].pb(o[i][c]);
	
	for(int i = 0; i < n; i++)
	{
		while(r[i].size() <= n)
			r[i].pb('.');
	}
/*
	FORIT(r, it)
	{
		FORIT(*it, it2)
			cout << (char)*it2 << " ";
		cout << endl;
	}
*/
#define clear(c) memset(c, 0, sizeof(c));

	int vert[2][50][50];
	int hor[2][50][50];
	int diag[2][50][50];
	int adiag[2][50][50];
	clear(vert); clear(hor); clear(diag); clear(adiag);
	for(int i = 0; i < n; i++)
	{
		for(int k= 0; k < n; k++)
		{
			if(r[i][k] == 'B')
			{
				if(i >= 1)
				{
					vert[0][i][k] = vert[0][i-1][k] + 1;
				}
				else
					vert[0][i][k] = 1;
				if(k >= 1)
					hor[0][i][k] = hor[0][i][k-1] + 1;
				else
					hor[0][i][k] = 1;
				if(k >= 1 && i >= 1)
					diag[0][i][k] = diag[0][i-1][k-1] + 1;
				else
					diag[0][i][k] = 1;
				if(k < n-1 && i >= 1)
					adiag[0][i][k] = adiag[0][i-1][k + 1] + 1;
				else
					adiag[0][i][k] = 1;
			}
			if(r[i][k] == 'R')
			{
				if(i >= 1)
				{
					vert[1][i][k] = vert[1][i-1][k] + 1;
				}
				else
					vert[1][i][k] = 1;
				if(k >= 1)
					hor[1][i][k] = hor[1][i][k-1] + 1;
				else
					hor[1][i][k] = 1;
				if(k >= 1 && i >= 1)
					diag[1][i][k] = diag[1][i-1][k-1] + 1;
				else
					diag[1][i][k] = 1;
				if(k < n-1 && i >= 1)
					adiag[1][i][k] = adiag[1][i-1][k + 1] + 1;
				else
					adiag[1][i][k] = 1;
			}
		}
	}

	int bestB = 0;
	for(int i = 0; i < n; i++)
	{
		for(int k = 0; k < n; k++)
		{
			int probe = max(max(vert[0][i][k], hor[0][i][k]), diag[0][i][k]);
			probe = max(probe, adiag[0][i][k]);
			if(probe > bestB) bestB = probe;
		}
	}
	
	int bestA = 0;
	for(int i = 0; i < n; i++)
	{
		for(int k = 0; k < n; k++)
		{
			int probe = max(max(vert[1][i][k], hor[1][i][k]), diag[1][i][k]);
			probe = max(probe, adiag[1][i][k]);
			if(probe > bestA) bestA = probe;
		}
	}

	bool A = (bestA >= k);
	bool B = (bestB >= k);
	printf("Case #%d: ", p + 1);
	if(!A && ! B)
		cout << "Neither";
	if(A && !B)
		cout << "Red";
	if(B && !A)
		cout << "Blue";
	if(A && B)
		cout << "Both";
	cout << endl;
}			

}
