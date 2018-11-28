/* Asyamov Igor
e-mail: igor9669@gmail.com*/

#include <iostream>
#include <deque>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <map>
#include <fstream>
#include <cstdlib>
#include <queue>
#include <bitset>
#include <set>
#include <stack>
#include <utility>
#include<cassert>
using namespace std;
#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)
#define CLR(x,a) memset(x,a,sizeof(x))
#define MP make_pair
#define PB push_back
#define A first
#define B second
#define Len(a) (int)a.length()
#define Sz(a) (int)a.size()
typedef long long LL;
typedef long double LD;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<VI > VVI;
#define MAXN 150
const double Eps=1e-9;
const double Pi=2*acos(0.0);
const int inf=1000*1000*1000;
//map<string,int>coll;
vector<vector<string> >a(MAXN*MAXN);
char s[MAXN];
int cnt=0,kol;
void Do()
{
	int len=strlen(s);
	string cur="";
	s[len]='/';
	int pos=0;
	FR(i,1,len+1)
	{
		if(s[i]=='/')
		{
			//coll[cur]=pos++;
			a[kol].PB(cur);
			cur="";
		}
		else cur+=s[i];
	}
	kol++;
}
void Do2()
{
	int len=strlen(s);
	string cur="";
	s[len]='/';
	int pos=0;
	vector<string>tmp;
	FR(i,1,len+1)
	{
		if(s[i]=='/')
		{
			tmp.PB(cur);
			pos++;
			cur="";
		}
		else cur+=s[i];
	}
	int Max=0;
	FOR(i,kol)
	{
		int l=0;
		FOR(j,min(Sz(a[i]),Sz(tmp)))
		{
			if(a[i][j]!=tmp[j])break;
			else l++;			
		}
		Max=max(Max,l);
	}
	if(Max<Sz(tmp))
	{
		a[kol++]=tmp;
		cnt+=Sz(tmp)-Max;
	}
}
int main()
{
	freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	FOR(cur,t)
	{
		int n,m;
		cnt=0;
		kol=0;
		a.clear();
		a.resize(MAXN*MAXN);
		scanf("%d%d",&n,&m);
		FOR(i,n)
		{
			scanf("%s",&s);
			Do();
		}
		FOR(i,m)
		{
			scanf("%s",&s);
			Do2();
		}
		printf("Case #%d: %d\n",cur+1,cnt);
	}
	return 0;
}