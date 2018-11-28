#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <map>
#include <set>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef long long ll;

#define sz size()
#define pb push_back
#define MAX 0x3FFFFFFF
#define all(x) (x).begin(),(x).end()
#define For(i,n) for(int i=0, _n=(n);i<_n;++i)
#define For2(i,a,b) for(int i=(a), _n=(b);i<_n;++i)
#define Forit(it,x) for(typeof((x).begin()) it=(x).begin(), ed=(x).end();it!=ed;++it)

int n;
ll a[64][9997];
int b[64];
char p[64];

int mod(int x, int y, int m)
{
	int t = 0;
	For2(i,x,y+1) t = (t*10+b[i])%m;
	return t;
}

ll cal(int m)
{
	memset(a, 0, sizeof(a));
	For(i,n) 
	{
		a[i][mod(0,i,m)%m] = 1;
		For(j,i) For(k,m) if(a[j][k])
		{
			a[i][(k+mod(j+1,i,m))%m] += a[j][k];
			a[i][abs(k-mod(j+1,i,m))%m] += a[j][k];
		}
	}
	ll ans = a[n-1][0];
	For2(i,1,210) if(i%2==0 || i%3==0 || i%5==0 || i%7==0) ans += a[n-1][i];
	return ans;
}

int main()
{
	int tn;
	int ti = 0;
	FILE *in = fopen("B-large.in","r");
	FILE *out = fopen("output.txt","w");
	//in = stdin;
	//out = stdout;
	fscanf(in,"%d",&tn);
	while(tn--)
	{
		fscanf(in,"%s",p);
		n = strlen(p);
		For(i,n) b[i] = p[i] - '0';
		ll ans = 0;
		ans = cal(210);
		fprintf(out,"Case #%d: %lld\n", ++ti, ans);
	}
}

/*
4
1
9
011
12345

*/
