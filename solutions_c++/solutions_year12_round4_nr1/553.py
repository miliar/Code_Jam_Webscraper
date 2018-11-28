#pragma comment(linker,"/STACK:128000000")
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

typedef unsigned long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef unsigned char uc;
typedef short int si;
typedef unsigned short int usi;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

#define rep(x,y,z) for(int x=(y),e##x=(z);x<e##x;x++)
#define all(x) (x).begin(),(x).end()
#define movmax(A,B) {if(A<(B)) A=(B);}
#define movmin(A,B) {if(A>(B)) A=(B);}
#define x first
#define y second

const double PI=acos(-1.0);
template<class T> T SQR(const T &a){return a*a;}

void test(int T)
{
	int n;
	cin>>n;
	ll Len[10002];
	ll maxLen[10002]={0};
	ll D[10002];
	rep(i,0,n)
		cin>>D[i]>>Len[i];
	cin>>D[n];
	Len[n]=1e9+1;
	n++;
	maxLen[0]=D[0];
	rep(i,0,n)
		if (maxLen[i])
		{
			rep(j,i+1,n)
			{
				if (D[i]+maxLen[i]<D[j]) 
					break;
				else 
					movmax(maxLen[j],min(D[j]-D[i],Len[j]));
			}
		}
	puts(maxLen[n-1]?"YES":"NO");
}

void run()
{
	int t;
	cin>>t;
	rep(i,0,t)
	{
		printf("Case #%d: ",i+1);
		test(i+1);
	}
}

#define F_NAME "A-large"
int main()
{
#ifndef F_NAME
		freopen("test.in","r",stdin);
		freopen("test.out","w",stdout);
#else
		freopen(F_NAME".in","r",stdin);
		freopen(F_NAME".out","w",stdout);
#endif
	time_t beg=clock();
	run();
	fprintf(stderr,"Time: %.3lf s.\n",(clock()-beg)/double(CLOCKS_PER_SEC));
	return 0;
}

/*

*/