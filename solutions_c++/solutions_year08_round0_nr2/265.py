/*
ID: ferromr1
PROG:
LANG: C++
*/
#include<cstdio>
#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
#include<stack>
#include<queue>
#include<string>
#include<algorithm>
#include<numeric>
#include<cstdlib>
#include<cmath>
#include<set>
#include<map>
#include<ctime>
#include<utility>
using namespace std;

#define pb push_back
#define mp make_pair
#define sz size()
#define all(qq) qq.begin(),qq.end()
#define rall(qq) qq.rbegin(),qq.rend()
#define clr(qq) memset((qq),0,sizeof(qq))
#define fill(qq) memset((qq),0x3F,sizeof(qq))
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define repd(i,n) for(int i=(int)(n-1);i>=0;i--)
#define rep2(i,a,b) for(int (i)=(int)(a);i<(int)(b);i++)
#define fore(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++)
#define rint(qq) int(floor(qq+0.5))
#define sqr(qq) ((qq) * (qq))
#define ll long long
#define inf 999999999
#define fi first
#define se second
#define PRICHOD 0
#define ODCHOD 1
#define A 0
#define B 1

int n,na,nb,t,reta,retb,akta,aktb;
int a[2005],b[2005];

void zapis(string s,int kde,int co)
{
	int cas=0,pom;
	char c;
	stringstream ss(s);
	ss>>cas>>c>>pom;
	cas=cas*60+pom;
	if (kde==A)
	{
		if (co==ODCHOD)	a[cas]++;
		else b[cas+t]--;
	}
	else
	{
		if (co==ODCHOD)	b[cas]++;
		else a[cas+t]--;
	}
}

int main ()
{
	cin>>n;
	rep(i,n)
	{
		clr(a);
		clr(b);
		cin>>t>>na>>nb;
		while(na--)
		{
			string s;
			cin>>s;
			zapis(s,A,ODCHOD);
			cin>>s;
			zapis(s,A,PRICHOD);
		}
		while(nb--)
		{
			string s;
			cin>>s;
			zapis(s,B,ODCHOD);
			cin>>s;
			zapis(s,B,PRICHOD);
		}
		reta=retb=akta=aktb=0;
		rep(j,1500)
		{
			akta+=a[j];
			aktb+=b[j];
			reta=max(reta,akta);
			retb=max(retb,aktb);
		}
		cout<<"Case #"<<i+1<<": "<<reta<<" "<<retb<<endl;
	}
	return 0;
}
