#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

int a[1000001],b[100000];
int dd[7];
int l = 0;
int pr;

void get(long long &x,long long y,long long &z, long long w)
{
	if (w == 0)
	{
		x = 1;
		z = 0;
	}
	else{
		int r = y % w;
		long long xx;
		long long yy;
		get(xx,w,yy,r);
		x = yy;
		z = (xx - (yy * (y/w))%pr+pr)%pr;
	}
}

int ni(int p, int x)
{
	long long xx; long long yy;
	get(xx,x,yy,p);
	return (xx % p);
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t;
	cin >> t;
	for (int i = 2 ; i < 1000000; i++)
		if (a[i] == 0)
		{
			l++;
			b[l] = i;
			for (int j = 2; j <= 1000000 / i; j++)
				a[i*j] = 1;
		}
	int s = 1;
	for (int i = 1; i < 6; i++)
	{
		s *= 10;
		for (int j = 0; j < l; j++){
			if (b[j] > s) dd[i] = j;
			if (b[j] >s) break;
		}
	}
	dd[6] = l;
	for (int T = 0 ; T < t; T++)
	{
		int d,k;
		cin >> d >>k;
		for (int i = 0; i < k; i++)
			cin >> a[i];			
		cout << "Case #" << T + 1 << ": ";
		if (k <=2) 
		{if (a[1]==a[0]) cout << a[0] <<endl; else cout << "I don't know.\n";	}
		else{
			if (a[1] == a[0]) cout << a[0] << endl;
			else{
				int  ans = -1;
		for (int pp = 0; pp < dd[d]; pp++)
		{
			 int p = b[pp];
			 pr = p;
			 int flag = 0;
			 for (int i = 0 ; i < k ; i++)
			 	if (a[i] >= p)
			 	{
					flag = 1;
				}
			if (flag == 0){
			long long aa = (a[2] - a[1] + p) % p;
			aa = (aa * ni(p,(a[1] -a[0] + p)%p))%p;
			long long bb = (a[1] - (aa * a[0])%p+p)%p;
			int ff = 0;
			for (int i = 2;i < k; i++)
			{
				long long s = (aa * a[i-1] + bb )%p;
				if (s != a[i]) ff = 1;
			}
			if (ff == 0)
			{
				s = (aa * a[k-1] +bb)% p;		
				if (ans == -1)ans = s;
				else{
					if (ans != s) ans = -2;
				}
			}
			}
		}
		if (ans == -2) cout << "I don't know.\n"; else cout << ans << endl;}
	
}
	}
}
