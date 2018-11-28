#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

const double pi=acos(-1.0);
const double eps=1e-11;

#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)

template<class T> T& operator >?= (T& x, T y) {if(y>x) x=y; return x;}
template<class T> T& operator <?= (T& x, T y) {if(y<x) x=y; return x;}
template<class T> T operator >? (T x, T y) {return x>y?x:y;}
template<class T> T operator <? (T x, T y) {return x<y?x:y;}

template<class T>
void splitstr(const string &s, vector<T> &out)
{
    istringstream in(s);
    out.clear();
    copy(istream_iterator<T>(in), istream_iterator<T>(), back_inserter(out));
}

template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }

#define SIZE(A) ((int)A.size())
#define LENGTH(A) ((int)A.length())
#define MP(A,B) make_pair(A,B)

const int oo=1000000;
const int maxsize=50000;

ifstream fin("C-small.in");
ofstream fout("C-small.out");
//ifstream fin("C-large.in");
//ofstream fout("C-large.out");

const int maxn=200;
const int dx[4]={1,1,0,0};
const int dy[4]={-1,1,1,-1};

int ans;
int m,n;
int vis[maxn][maxn];

void search(int x, int y, int tot)
{
	if (tot+(m-x)*n/2+(n-y)/2+1<=ans) return;
	if (x>m)
	{
		if (tot>ans) ans=tot;
		return;
	}
	if (vis[x][y]>0)
	    search(y<n?x:x+1, y<n?y+1:1, tot);
	else
	{
	    search(y<n?x:x+1, y<n?y+1:1, tot);
		vis[x][y]++;
		for (int i=0; i<4; ++i)
		    vis[x+dx[i]][y+dy[i]]++;
  	    search(y<n?x:x+1, y<n?y+1:1, tot+1);
  	    vis[x][y]--;
		for (int i=0; i<4; ++i)
		    vis[x+dx[i]][y+dy[i]]--;
	}
}
void solve()
{
	fin >> m >> n;
	memset(vis,0,sizeof(vis));
	for (int i=1; i<=m; ++i)
	{
		string str;
		fin>>str;
	    for (int j=1; j<=n; ++j)
			if (str[j-1]=='x') vis[i][j]=1;
	}
	
	ans=0;
	search(1,1,0);
	fout << ans << endl;
}

int main()
{
	int tc;
	fin >> tc;
	for (int i = 1; i <= tc; ++i)
	{
		fout << "Case #" << i << ": ";
		solve();
	}
	fin.close();
	fout.close();
	system("Pause");
	return 0;
}
