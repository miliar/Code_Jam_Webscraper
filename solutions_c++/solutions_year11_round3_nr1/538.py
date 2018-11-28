#include <cstdio>
#include <memory>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <complex>
#include <string>
#include <cstring>
#include <cmath>
#include <ctime>
#include <iostream>
#include <fstream>
#include <functional>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef short int si;
typedef long double ld;
typedef pair<int,int> pii;
#define rep(x,y,z) for(int x=(y),e##x=(z);x<e##x;x++)

const double PI=acos(-1.0);

template<class T> inline T SQR(T a){return a*a;}

//#define __small
#define __large

void test(int T)
{
	int n,m;
	cin>>n>>m;
	char *A[50];
	rep(i,0,n)
	{
		A[i]=new char[51];
		scanf(" %s",A[i]);
	}
	bool ok=true;
	rep(i,0,n)
		rep(j,0,m)
		{
			bool curr=1;
			if (A[i][j]=='#')
			{
				if (i==n-1 || A[i+1][j]!='#') curr=false;
				if (j==m-1 || A[i][j+1]!='#') curr=false;
				if (j==m-1 || i==n-1 || A[i+1][j+1]!='#') curr=false;
				if (!curr)
				{
					ok=false;
					goto out;
				}
				A[i][j]=A[i+1][j+1]='/';
				A[i+1][j]=A[i][j+1]='\\';
			}
		}
out:
	if (T==50)
		int a=1;
	printf("Case #%d:\n",T);
	if (!ok) puts("Impossible");
	else
	{
		rep(i,0,n)
			puts(A[i]);
	}
}

int main()
{
#ifdef __small
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-out.txt","w",stdout);
#endif
#ifdef __large
	freopen("A-large.in","r",stdin);
	freopen("A-large-out.txt","w",stdout);
#endif
	int T;
	cin>>T;
	cerr<<T;
	rep(i,0,T)
		test(i+1);
	return 0;	
}
/*
4 2
1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
1 1 1
1 0 2
*/