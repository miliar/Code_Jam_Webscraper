#include <iostream>
#include <vector>
#include <stdio.h>
#include <string>
#include <math.h>
#include <algorithm>
#include <set>
#include <math.h>
#include <time.h>
#include <stdio.h>
#define rep(i,k,n) for(int (i) = (k); (i) < (n); (i)++)
#define sqr(r) (r)*(r)
#define ii pair<int,int>
#define vii vector<ii>
#define vi vector<int>
#define vvi vector<vi>
using namespace std;


set<long long> si;
long long mod;
long long n,m,k,d,l,c,r, INF = 10000009;

int ma, mi;


int main()
{
	freopen("in","r", stdin);
	freopen("out", "w", stdout);
	cin >> n;
	
	long long sp;
	rep(i,1,n+1)
	{
		sp = 0;
		cin >> m >> c >> r;
		rep(j,0,m)
		{
			cin >> k;
			if(k%3 == 0)
			{
				mi = k/3;
				ma = k/3+1;
			}
			else
			{
				mi = k/3+1;
				ma = k/3+k%3;
			}
			if ( mi >= r )
			{
				sp++;
			}
			else if(c && ma >= r && k != 0 && k < 29)
			{
				sp++;
				c--;
			}

		}
		cout << "Case #" << i << ": " << sp << "\n";
		
	}
	

	return 0;
}
