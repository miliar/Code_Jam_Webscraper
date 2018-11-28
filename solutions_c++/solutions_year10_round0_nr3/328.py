/******************\
*    CPP source    *
*     By HPFDF     *
\******************/
#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>
#include <iomanip>
#include <cstdio>
#include <string>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <complex>
#include <vector>
#include <map>
#include <set>
#define rep(i,n)   for(int i=0;i<(n);++i)
#define fab(i,a,b) for(int i=(a);i<=(b);++i)
#define fba(i,b,a) for(int i=(b);i>=(a);--i)
#define fec(i,a)   for(typeof(a.end())i=a.begin();i!=a.end();++i)
#define fpc(i,v)   for(int i=a[v];i;i=nx[v])
#define fil(a)     memset(a,0,sizeof(a))
#define all(a)     a.begin(),a.end()
#define rdm        srand(time(NULL))
using namespace std;
const int HX = 0x3F3F3F3F;
/****************************\
*            MAIN            *
\****************************/


ifstream fin("C-large.in");
ofstream fou("C-large.out");
//#define fin cin
//#define fou cout

long long a[1111], nx[1111][30], cn[1111][28];
long long ans, tot, m, k;
int n, t;

int main()
{
	fin >> t;
	fab(T, 1, t)
	{
		fin >> m >> k >> n;
		tot = ans = 0;
		rep(i, n) fin >> a[i], a[n + i] = a[i], tot += a[i];
		if (k >= tot) ans = m * tot; else
		{
			rep(i, n)
			{
				tot = a[i];
				fab(j, i + 1, n * 2 - 1)
					if (tot + a[j] > k)
					{
						nx[i][0] = j % n;
						cn[i][0] = tot;
						break;
					} else tot += a[j];
			}

			rep(i, n) nx[i][0] %= n;

			rep(j, 27) rep(i, n)
				cn[i][j + 1] = cn[i][j] + cn[nx[i][j]][j],
				nx[i][j + 1] = nx[nx[i][j]][j];
			k = 0;
			rep(i, 28) if (m>>i&1)
			{
				ans += cn[k][i];
				k = nx[k][i];
			}
		}
		fou << "Case #" << T << ": " << ans << endl;
	}
}


/****************************\
*            EOF             *
\****************************/



