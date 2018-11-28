#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <complex>
#include <limits>
#include <string.h>
#include <fstream>
using namespace std;
#define rep(x,n) for(int x=0;x<n;x++)
#define mp(x,y) make_pair(x,y)
#define getBit(code, i) (code & (1 << i))
#define setBit(code, i) (code | (1 << i))
#define resetBit(code, i) (code & ~(1 << i))
#define mem(a, b) memset(a, b, sizeof(a))

char matr[101][101];
double WP[101];
double OWP[101];
double OOWP[101];
int N;

void calc()
{
	rep(i,N)
	{
		double tot = 0;
		int cnt = 0;
		rep(j,N)
		{
			if(matr[i][j] == '1')
			{
				tot += 1;
				cnt++;
			}
			else if(matr[i][j] == '0')
				cnt++;
		}
		WP[i] = tot/cnt;
	}
	rep(i,N)
	{
		double WPT = 0;
		int WPcnt = 0;
		rep(j,N)if(matr[i][j] != '.')
		{
			double tot = 0;
			int cnt = 0;
			rep(a,N)if(a != i)
			{
				if(matr[j][a] == '1')
				{
					tot += 1;
					cnt++;
				}
				else if(matr[j][a] == '0')
				{
					cnt++;
				}
			}
			WPT += (tot/cnt);
			WPcnt++;
		}
		OWP[i] = WPT/WPcnt;
	}
	rep(i,N)
	{
		double tot = 0;
		int cnt = 0;
		rep(j,N)
		{
			if(matr[i][j] != '.')
			{
				tot += OWP[j];
				cnt++;
			}
		}
		OOWP[i] = tot/cnt;
	}
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("GCJ1b.txt", "w", stdout);
	int K;
	cin >> K;
	rep(kase,K)
	{
		cin >> N;
		rep(i,N)rep(j,N)
		{
			cin >> matr[i][j];
		}
		calc();
		printf("Case #%d:\n",kase+1);
		rep(i,N)
		{
			printf("%.12f\n",0.25*WP[i] + 0.5*OWP[i] + 0.25*OOWP[i]);
		}
	}
	return 0;
}
