#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<string>
#include<vector>
#include<utility>
#include<set>
#include<sstream>
#define fr(a,b,c) for (a=b;a<=c;a++)
#define frr(a,b,c) for (a=b;a>=c;a--)
#define pb push_back
#define mp make_pair
#define psi pair<string,int>
#define F first
#define S second
#define oo 1000111222
using namespace std;

int n,m,re,d[10010],c[255],rpos;
string b,rs;
vector< psi > a[12];

int finish(int len,string s)
{
	int i;
	fr(i,0,a[len].size()-1)
		if (a[len][i].F!=s && !d[i]) return 0;
	return 1;
}

void att(int len,string s,int pos)
{
	int cnt=0,n=a[len].size()-1,i=-1,j,k,num=0;
	char ch;
	memset(d,0,sizeof(d));
	while (!finish(len,s))
	{
		while (1)
		{
			++i;
			fr(ch,'a','z') c[ch]=0;
			fr(j,0,n)
				if (!d[j])
					fr(k,0,len-1)
						c[a[len][j].F[k]]=1;
			if (c[b[i]]) break;
		}
		int right=0;
		fr(k,0,len-1)
			if (s[k]==b[i]) right=1;
		cnt+=(!right);
		fr(j,0,n)
			if (!d[j])
				fr(k,0,len-1)
					if ((a[len][j].F[k]==b[i]) ^ (s[k]==b[i]))
					{
						d[j]=1; break;
					}
	}
	if (cnt>re || (cnt==re && pos<rpos))
	{
		re=cnt; rpos=pos;	rs=s;
	}
}

int main()
{
	freopen("bsmall2.in","r",stdin); freopen("bsmall2.out","w",stdout);
	int test,i,j,it;
	cin >> test;
	fr(it,1,test)
	{
		cin >> n >> m;
		fr(i,1,10) a[i].clear();
		fr(i,1,n) 
		{
			cin >> b;
			j=b.length();
			a[j].pb(mp(b,i));
		}
		cout << "Case #" << it << ":";
		while (m--)
		{
			re=-1;
			cin >> b;
			fr(i,1,10)
				if (!a[i].empty())
					fr(j,0,a[i].size()-1)
						att(i,a[i][j].F,a[i][j].S);
			cout << " " << rs;
		}
		cout << endl;
	}
	fclose(stdin); fclose(stdout);
   return 0;
}
