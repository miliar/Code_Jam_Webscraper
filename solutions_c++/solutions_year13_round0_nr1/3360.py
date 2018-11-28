//#ifdef _MONYURA_
#pragma comment(linker,"/STACK:256000000")
//#endif

#include <iostream>
#include <iomanip>
#include <cstdio>
#include <bitset>
#include <memory>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <string>
#include <cstring>
#include <fstream>
#include <functional>
#include <stack>
#include <complex>
#include <wchar.h>
#include <wctype.h>
#include <cmath>
#include <queue>
#include <ctime>
#include <numeric>


using namespace std;

template<typename T> T mabs(const T &a){ return a<0?-a:a;}
#define rep(x,y,z) for(int x=(y),e##x=(z);x<e##x;x++)
#define SQR(x) ((x)*(x))
#define all(c) (c).begin(), (c).end()

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef short int si;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

const double PI = acos(-1.0);

void test()
{
	char A[4][5];
	rep(i,0,4)
		scanf("%s",A[i]);
	char S[3]="XO";
	rep(t,0,2)
	{
		bool ok = false;
		int d1=0;
		int d2=0;
		rep(i,0,4)
		{
			int cnt=0;
			rep(j,0,4)
				cnt+= A[i][j]==S[t] || A[i][j]=='T';
			if (cnt==4) ok = true;
			cnt=0;
			rep(j,0,4)
				cnt+= A[j][i]==S[t] || A[j][i]=='T';
			if (cnt==4) ok = true;
			d1+=A[i][i]==S[t] || A[i][i]=='T';
			d2+=A[i][3-i]==S[t] || A[i][3-i]=='T';
		}
		if (d1==4 || d2==4) ok = true;
		if (ok)
		{
			printf("%c won\n",S[t]);
			return;
		}
	}
	rep(i,0,4)
		rep(j,0,4)
			if (A[i][j]=='.')
			{
				puts("Game has not completed");
				return;
			}
	puts("Draw");
}

void run()
{
	int t;
	cin>>t;
	rep(i,0,t)
	{
		printf("Case #%d: ",i+1);
		test();
	}
}

#define problem "A-large"

int main()
{
#ifdef _DEBUG
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	time_t st=clock();
#else
	freopen(problem".in","r",stdin);
	freopen(problem".out","w",stdout);
#endif
	run();
#ifdef _MONYURA_
	printf( "=============\n");
	printf("Time: %.2lf sec\n",(clock()-st)/double(CLOCKS_PER_SEC));
#endif

	return 0;
} 