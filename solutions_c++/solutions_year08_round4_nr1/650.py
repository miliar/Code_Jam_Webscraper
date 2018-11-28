#include <iostream>
#include <stdio.h>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <math.h>
#include <algorithm>
#include <map>
#include <set>
#include <limits.h>
#include <memory.h>

using namespace std;

#define LL              	long long
#define pb              	push_back
#define mp              	make_pair
typedef vector <int> 		vi;
typedef vector <string> 	vs;
typedef pair   <int,int>    pii;

const int LM = INT_MAX/3;

int n,e,res;
int v[10000],t[10000],c[10000];
int cached[10000][2];

void input()
{
	int i;

	cin >> n >> e;
	for (i=0; i<(n-1)/2; i++) cin >> t[i] >> c[i];

	memset(v,-1,sizeof(v));
	for (i=(n-1)/2; i<n; i++) cin >> v[i];
}

int f(int x, int e)
{
	int& r = cached[x][e];
	if (r != -1) return r;

	int y;
	if (x>=(n-1)/2) return r = (v[x]==e ? 0 : LM);

	r = LM;
	if (e==0)
	{
		if (t[x]==1 || c[x]==1)
		{
			y = (t[x]==0 ? 1 : 0);
			r = min(r, y+min(f(x+x+1,0),f(x+x+2,0)));
		}
		if (t[x]==0 || c[x]==1)
		{
			y = (t[x]==1 ? 1 : 0);
			r = min(r, y+f(x+x+1,0)+f(x+x+2,0));
		}
	} else
	{
		if (t[x]==1 || c[x]==1)
		{	
			y = (t[x]==0 ? 1 : 0);
			r = min(r, y+f(x+x+1,1)+f(x+x+2,1));
		}
		if (t[x]==0 || c[x]==1)
		{
			y = (t[x]==1 ? 1 : 0);
			r = min(r, y+min(f(x+x+1,1),f(x+x+2,1)));
		}
	}
	// cerr << x << " " << e << " " << r << endl;
	return r;
}

void process()
{
	memset(cached,-1,sizeof(cached));
	res = f(0,e);
}

int main()
{
	int numTest;

	cin >> numTest;
	for (int i=1; i<=numTest; i++)
	{
		input();
		process();
		if (res != LM)
			cout << "Case #" << i << ": " << res << endl;
		else
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
	}
	return 0;
}
