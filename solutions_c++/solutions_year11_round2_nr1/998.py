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

void test(int t)
{
	printf("Case #%d:\n",t);
	char *A[100];
	int n;
	cin>>n;
	rep(i,0,n)
	{
		A[i]=new char[101];
		scanf(" %s",A[i]);
	}
	double WP[100]={0};
	double OWP[100]={0};
	double OOWP[100]={0};
	int Cnt[100]={0};
	rep(i,0,n)
	{
		rep(j,0,n)
		{
			if (A[i][j]!='.') Cnt[i]++;
			if (A[i][j]=='1') WP[i]+=1.0;
		}
		//WP[i]/=Cnt[i];
	}
	rep(i,0,n)
	{
		int cnt=0;
		rep(j,0,n)
		{
			if (A[i][j]!='.') cnt++;
			if (A[i][j]=='0') 
				OWP[i]+=(WP[j]-1)/(Cnt[j]-1);
			if (A[i][j]=='1') 
				OWP[i]+=(WP[j]-0)/(Cnt[j]-1);
		}
		OWP[i]/=cnt;
	}
	rep(i,0,n)
	{
		WP[i]/=Cnt[i];
		int cnt=0;
		rep(j,0,n)
		{
			if (A[i][j]!='.') cnt++;
			if (A[i][j]!='.') OOWP[i]+=OWP[j];
		}
		OOWP[i]/=cnt;
	}
	rep(i,0,n)
		printf("%7lf\n",0.25*(WP[i]+OOWP[i])+0.5*(OWP[i]));
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