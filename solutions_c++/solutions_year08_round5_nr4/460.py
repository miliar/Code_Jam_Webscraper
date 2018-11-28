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

ifstream fin("D-small.in");
ofstream fout("D-small.out");
//ifstream fin("D-large.in");
//ofstream fout("D-large.out");

const int prime=10007;
const int maxn=1000;

int f[maxn][maxn];
bool bad[maxn][maxn];

void solve()
{
	int h,w,r;
	fin >>h >> w >> r;
	memset(bad,0,sizeof(bad));
	for (int i=0; i<r; ++i)
	{
		int x,y;
		fin >> x>> y;
		bad[x][y]=1;
	}
	memset(f,0,sizeof(f));
	f[1][1]=1;
	for (int i=1; i<=h; ++i)
	    for (int j=1; j<=w; ++j)
	        if (bad[i][j])
	            f[i][j]=0;
	        else
	        {
				if (i>1 && j>2)
					f[i][j] += f[i-1][j-2];
				if (i>2 && j>1)
					f[i][j] += f[i-2][j-1];
				f[i][j] %= prime;
			}
	fout << f[h][w] << endl;
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
//	system("Pause");
	return 0;
}
