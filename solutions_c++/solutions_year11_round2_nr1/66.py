#pragma comment(linker,"/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <map>
#include <set>
#include <ctime>
#include <algorithm>
#include <memory.h>

using namespace std;

#define WR printf
#define RE scanf
#define PB push_back
#define SE second
#define FI first

#define FOR(i,k,n) for(int i=(k); i<=(n); i++)
#define DFOR(i,k,n) for(int i=(k); i>=(n); i--)
#define SZ(a) (int)((a).size())
#define FA(i,v) FOR(i,0,SZ(v)-1)
#define RFA(i,v) DFOR(i,SZ(v)-1,0)
#define CLR(a) memset(a, 0, sizeof(a))

#define LL long long
#define VI  vector<int>
#define PAR pair<int ,int>
#define o_O 1000000000 
void __never(int a){printf("\nOPS %d", a);}
#define ass(s) {if (!(s)) {__never(__LINE__);cout.flush();cerr.flush();abort();}}

int n;
char T[128][128];
double WP[128];
double OWP[128];
double OOWP[128];

void sol()
{
	FOR(a,1,n)
	{
		int cnt=0, ones=0;
		FOR(b,1,n)
			if (T[a][b]=='1')
			{
				cnt++;
				ones++;
			}
			else if (T[a][b]=='0') cnt++;
		WP[a] = (double)ones/(double)cnt;
	}

	FOR(a,1,n)
	{
		int cnt=0;
		double sum=0.;
		FOR(b,1,n) if (T[a][b]!='.')
		{
			int cnt2=0, ones2=0;
			FOR(c,1,n) if (c!=a)
			{
				if (T[b][c]=='1')
				{
					ones2++;
					cnt2++;
				}
				else if (T[b][c]=='0') cnt2++;
			}
			sum += (double)ones2/cnt2;
			cnt++;
		}
		OWP[a] = sum/cnt;
	}

	FOR(a,1,n)
	{
		int cnt=0;
		double sum=0;
		FOR(b,1,n) if (T[a][b]!='.')
		{
			sum += OWP[b];
			cnt++;
		}
		OOWP[a] = sum/cnt;
	}

	FOR(a,1,n) WR("%.10lf\n", 0.25*WP[a] + 0.5*OWP[a] + 0.25*OOWP[a]);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin >> t;
	FOR(a,1,t)
	{
		cin >> n;
		gets(T[0]);
		FOR(b,1,n) gets(&T[b][1]);
		cout << "Case #" << a << ":\n";
		sol();
	}
	return 0;
}