#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <ctime>
#include <set>
#include <map>
#include <cmath>

using namespace std;

#define INP_FILE "C-small-attempt0.in"
#define OUT_FILE "output.txt"

#define rp(i,n) for(int (i)=0;(i)<(n);++(i))
#define pb push_back
#define L(s) (int)s.size()
#define mp make_pair
#define pii pair<int,int>
#define x first 
#define y second
#define inf 1000000000
#define VI vector<int>
#define ll long long
#define all(s) (s).begin(),(s).end()
#define C(u) memset((u),0,sizeof((u)))
#define ull unsigned ll
#define uint unsigned int

int a[10001];
int n,l,h;
int mn;

double xgcd(double a,double b)
{
	double t,z;
	if (b>a) { t=a; a=b; b=t; }
	while (b>0)
	{
		t= floor (a/b);
		z=b;
		b=a-t*z;
		a=z;
	}
	return a;
}

int check(int a,int b)
{
	return (a%b==0 || b%a==0);
}

int main()
{
	freopen( INP_FILE , "r" , stdin );
	freopen( OUT_FILE , "w" , stdout );
	int tstCnt;
	cin>>tstCnt;

	for(int tst=1;tst<=tstCnt;tst++)
	{
		cin>>n>>l>>h;

		cin>>a[0]; mn=a[0];

		for(int i=1;i<n;i++)
		{
			cin>>a[i];
			if (a[i]<mn) mn=a[i];
		}
		bool f=false;
		int i;
		for(i=l;i<=h;i++)
		{
			f=true;
			for(int j=0;j<n;j++)
				f = f && check(i,a[j]);
			if (f)
				break;
		}
		if (f)
		{
			printf("Case #%d: %d\n",tst,i);
		}else{
			printf("Case #%d: NO\n",tst);
		}	

		//printf("Case #%d: ",tst);
	}
	return 0;
}