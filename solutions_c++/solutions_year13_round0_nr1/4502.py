#include<stdio.h>
#include<stdlib.h>
#include<cmath>
#include<ctype.h>
#include<string>
#include<cstring>
#include<iostream>

#include<algorithm>
#include<stack>
#include<queue>
#include<vector>
#include<map>
#include<bitset>
#include<set>
#include<list>
#include<complex>

#define GC getchar_unlocked
#define MAX(a,b) ({a>b?a:b;})
#define MIN(a,b) ({a>b?b:a;})
#define P(x) printf("%d\n",x);
#define PLL(x) printf("%lld\n",x);
#define MP make_pair
#define PB push_back
#define SZ size()
#define CL clear()
#define X first
#define Y second
#define MOD 1000000007
#define max 100000

using namespace std;
typedef long long int LL;
typedef unsigned long long int ULL;
typedef vector<int> VI;
typedef vector<double> VD;
typedef pair<int,int> PII;
typedef pair<double,double> PDD;
typedef vector<pair<int,int> > VPII;
typedef stack<int> SI;

template<class T>inline T input(T x){char c=GC();x=0;T s=1;while(c<48||c>57){if(c=='-')s=-1;c=GC();}while(c>=48&&c<=57){x=(x<<3)+(x<<1)+c-48;c=GC();}return x*s;}
template<class T>inline void output(T a){if(a){T v=a%10;output(a/10);putchar((char)(v+'0'));}}
template<class T>inline T gcd(T a,T b){return b?gcd(b,a%b):a;}
template<class T>inline T modinv(T a,T n){T i=n,v=0,d=1;while(a>0){T t=i/a,x=a;a=i%x;i=x;x=d;d=v-t*x;v=x;}return (v+n)%n;}
LL modpow(LL n ,LL k,LL mod){LL ans=1;while(k>0){if(k&1)ans=(ans*n)%mod;k>>=1;n=(n*n)%mod;}return ans%mod;}

int a[4][4];
int numDot = 0;
void update(int i,int j,char c)
{
	if(c == 'X')
		a[i][j] = 1;
	else if(c == 'O')
		a[i][j] = 0;
	else if(c == 'T')
		a[i][j] = 2;
	else
		numDot++;
}

int check()
{
	int i,j;
	//Horizontal
	for(i=0;i<4;i++)
	{
		int tPos = -1;
		for(j=0;j<4;j++)
			if(a[i][j] == 2)
				tPos = j;
		int c = 1;
		int x = (tPos == 0)?a[i][1]:a[i][0];
		for(j=0;j<4;j++)
			if( j!=tPos && a[i][j] != x )
				c = 0;
		if(c && ( x == 1 || x == 0) )
			return x;
	}
	//Vertical
	for(i=0;i<4;i++)
	{
		int tPos = -1;
		for(j=0;j<4;j++)
			if(a[j][i] == 2)
				tPos = j;
		int c = 1;
		int x = (tPos == 0)?a[1][i]:a[0][i];
		for(j=0;j<4;j++)
			if( j!=tPos && a[j][i] != x )
				c = 0;
		if(c && ( x == 1 || x == 0) )
			return x;
	}
	//Diagonal 1
	int tPos = -1;
	for(i=0;i<4;i++)
		if(a[i][i] == 2)
			tPos = i;
	int c = 1;
	int x = (tPos == 0)?a[1][1]:a[0][0];
	for(j=0;j<4;j++)
		if( j!=tPos && a[j][j] != x )
			c = 0;
	if(c && ( x == 1 || x == 0) )
		return x;
	//Diagonal 2
	tPos = -1;
	for(i=0;i<4;i++)
		if(a[i][3-i] == 2)
			tPos = i;
	c = 1;
	x = (tPos == 0)?a[1][2]:a[0][3];
	for(j=0;j<4;j++)
		if( j!=tPos && a[j][3-j] != x )
			c = 0;
	if(c && ( x == 1 || x == 0) )
		return x;
	//Else
	return numDot?3:2;
}

int main()
{
	int test,t;
	scanf("%d%*c",&test);
	for(t=1;t<=test;t++)
	{
		int i,j;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				a[i][j] = -1;
		numDot = 0;
		char str[10];
		for(i=0;i<4;i++)
		{
			scanf("%s",str);
			update(i,0,str[0]);
			update(i,1,str[1]);
			update(i,2,str[2]);
			update(i,3,str[3]);
		}
		int p = check();
		printf("Case #%d: ",t);
		if(p == 0)
			printf("O won\n");
		else if(p == 1)
			printf("X won\n");
		else if(p == 2)
			printf("Draw\n");
		else if(p == 3)
			printf("Game has not completed\n");
	}
	return 0;
}
