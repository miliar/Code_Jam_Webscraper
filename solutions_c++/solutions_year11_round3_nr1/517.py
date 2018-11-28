#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <fstream>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <functional>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <utility>

using namespace std;

#define SIZE(X) ((int)X.size())
#define LENGTH(X) ((int)X.length())
#define MP(A,B) make_pair(A,B)
//typedef long long int64;
//typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) ((S&two(X))>0)
#define containL(S,X) ((S&twoL(X))>0)
const double pi=acos(-1.0);
const double eps=1e-11;
template<class T> void checkmin(T &a,T b){if (b<a) a=b;}
template<class T> void checkmax(T &a,T b){if (b>a) a=b;}
template<class T> T sqr(T x) {return x*x;}
int countbit(int n) {return (n==0)?0:(1+countbit(n&(n-1)));}
int lowbit(int n) {return (n^(n-1))&n;}
typedef pair<int,int> ipair;
template <class T> void out(T A[],int n){for (int i=0;i<n;i++) cout<<A[i]<<" ";cout<<endl;}
template <class T> void out(vector<T> A,int n=-1){if(n==-1) n=A.size(); for (int i=0;i<n;i++) cout<<A[i]<<" ";cout<<endl;}
template <class T> gcd(T a,T b){ if (a<0) return gac(-a,b); if(b<0) return gac(a,-b); return (b==0)?a:gcd(b,a%b);}
template <class T> lcm(T a,T b){ return a*(b/gcd(a,b));}
//int64 toInt64(string s){ istringstream sin(s); int64 t; sin>>t; return t;}
int toInt(string s){ istringstream sin(s); int t; sin>>t; return t;}
//string toString(int64 v){ ostringstream sout; sout<<v; return sout.str();}
string toString(int v){ ostringstream sout; sout<<v; return sout.str();}


void main2()
{
	int R, C, i, j;
	char map[55][55];
	bool flag = true;

	scanf("%d%d", &R, &C);

	for(i=0; i<R; i++)
		scanf("%s", map[i]);

	for(i=0; i<R; i++)
		for(j=0; j<C; j++)
		{
			if(map[i][j]=='#')
			{
				if(i+1<R && j+1<C && map[i][j+1]=='#' && map[i+1][j]=='#' && map[i+1][j+1]=='#')
				{
					map[i][j]= map[i+1][j+1] = '/';
					map[i][j+1] = map[i+1][j] = '\\';
				}
				else
				{
					flag = false; goto Err;
				}
			}
		}
Err:
		if(flag)
		{
			for(i=0;i<R;i++) {
				for(j=0;j<C;j++)
					printf("%c", map[i][j]);
				printf("\n");
			}
		}
		else
		{
			printf("Impossible\n");
		}

}


int main()
{
	freopen("1.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int t, x;
	
	scanf("%d", &t);

	for(x=1; x<=t; x++)
	{
		printf("Case #%d:\n", x);
		main2();
	}
	return 0;
}
