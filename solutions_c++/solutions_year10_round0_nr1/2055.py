#include<iostream>
#include<string.h>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<deque>
#include<set>
#include<stack>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<cassert>
#define CLRM(x) memset(x,-1,sizeof(x))
#define CLR(x) memset(x,0,sizeof(x))
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define MP make_pair
#define VI vector<int> 
#define VVI vector<vector<int> >
#define PII pair<int,int>
#define SZ(x) (int)x.size()
#define LL unsigned long long
#define MIN(a,b) (a)<(b)?(a):(b)
#define MAX(a,b) (a)>(b)?(a):(b)
#define LMAX 1000000000000000000LL
#define IMAX 100000000
using namespace std;


int main()
{
	int tes;
	cin >> tes;
	int tt = 0;
	while(tes--)
	{
		tt++;
		LL n, k;
		cin >> n >> k;
		LL t = 1LL<<n;
		LL t2 = k % t;
		if(t2 == t-1)
		{
			printf("Case #%d: ON\n", tt);
		}
		else
		{
			printf("Case #%d: OFF\n", tt);
		}
	}
	return 0;
}
