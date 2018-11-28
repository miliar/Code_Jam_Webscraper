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


int t, n, m, k;
ifstream fin("A-large.in");
ofstream fou("A-large.out");
//#define fin cin
//#define fou cout

int main()
{
	fin >> t;
	fab(T, 1, t)
	{
		fin >> n >> m;
		bool ok = true;
		rep(i, n)
		{
			if (!(m&1))
			{
				ok = false;
				break;
			}
			m /= 2;
		}
		fou << "Case #" << T << ": ";
		if (ok) fou << "ON\n"; else fou << "OFF\n";
	}
}


/****************************\
*            EOF             *
\****************************/



