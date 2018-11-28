#include <set>
//#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <string>
#include <vector>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <iostream>
#include <algorithm>
#include <functional>
using namespace std;
//typedef long long LL;
//typedef __int64 LL;
//typedef long double DB;
//typedef unisigned __int64 LL;
//typedef unsigned long long ULL;
#define EPS  1e-8
#define MAXN 1600
#define MAXE 300000
#define INF  0x3f3f3f3f
#define PI   acos(-1.0)
#define MOD  99991
//#define MOD  99990001
//#define MOD  1000000007
#define max(a,b) 	((a)>(b)?(a):(b))
#define min(a,b) 	((a)<(b)?(a):(b))
#define max3(a,b,c) (max(max(a,b),c))
#define min3(a,b,c) (min(min(a,b),c))
#define mabs(a) 	((a<0)?(-a):a)
//#define L(t) 		(t << 1)  //Left son t*2
//#define R(t) 		(t << 1 | 1) //Right son t*2+1
//#define Mid(a,b) 	((a+b)>>1) //Get Mid
//#define lowbit(a) (a&-a) //Get Lowbit
//int gcd(int a,int b){return b?gcd(b,a%b):a;}
//int lcm(int a,int b){return a*b/gcd(a,b);}
//std::ios::sync_with_stdio(false);
char a[4][4];
int solve() //0 = not, 1 = O , 2 = X , 3 = draw
{
	int cntO,cntX,cntdot = 0;
	for(int i = 0; i < 4; i++)
	{
		cntO = 0;
		cntX = 0;
		for(int j = 0; j < 4; j++)
		{
		    if(a[i][j] == 'X' || a[i][j] == 'T')
                cntX++;
            if(a[i][j] == 'O' || a[i][j] == 'T')
                cntO++;
            if(a[i][j] == '.')
            	cntdot++;
		}
		//cout<<cntO<<" "<<cntX<<endl;
		if(cntO == 4) return 1;
		if(cntX == 4) return 2;
	}
	for(int j = 0; j < 4; j++)
	{
		cntO = 0;
		cntX = 0;
		for(int i = 0; i < 4; i++)
		{
		    if(a[i][j] == 'X' || a[i][j] == 'T')
                cntX++;
            if(a[i][j] == 'O' || a[i][j] == 'T')
                cntO++;
		}
		//cout<<cntO<<" "<<cntX<<endl;
		if(cntO == 4) return 1;
		if(cntX == 4) return 2;
	}
	cntO = 0;
	cntX = 0;
	for(int i = 0; i < 4; i++)
	{
		if(a[i][i] == 'X' || a[i][i] == 'T')
                cntX++;
        if(a[i][i] == 'O' || a[i][i] == 'T')
                cntO++;
	}
	if(cntO == 4) return 1;
	if(cntX == 4) return 2;
	cntO = 0;
	cntX = 0;
	for(int i = 0; i < 4; i++)
	{
		if(a[i][3-i] == 'X' || a[i][3-i] == 'T')
                cntX++;
        if(a[i][3-i] == 'O' || a[i][3-i] == 'T')
                cntO++;
	}
	if(cntO == 4) return 1;
	if(cntX == 4) return 2;
	if(cntdot == 0) return 3;
	return 0;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int T;
	cin>>T;
	for(int k = 1; k <= T; k++)
	{
//	    getchar();
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
			    cin>>a[i][j];
			}
		}
		if(solve() == 0) printf("Case #%d: Game has not completed\n",k);
		if(solve() == 1) printf("Case #%d: O won\n",k);
		if(solve() == 2) printf("Case #%d: X won\n",k);
		if(solve() == 3) printf("Case #%d: Draw\n",k);
	}
    return 0;
}
