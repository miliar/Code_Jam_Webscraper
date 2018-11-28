#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <fstream>
using namespace std;
#define pb push_back
#define ppb pop_back
#define mp make_pair
//#define pi 2*acos(0.0)
#define mp make_pair
//#define x first
//#define y second
#define sqr(a) (a)*(a)
#define pii pair<int,int>
#define pdd pair<double,double>
#define sz(c) (int)((c).size())
#define inf 1000000000
#define all(c) (c).begin(), (c).end()
#define vi vector<int>
#define vpii vector< pii >
#define vpdd vector< pdd >
#define L(s) (int)((s).end()-(s).begin())
#define ll long long
#define C(a,b) memset((a),(b),sizeof((a)))
int cnt,cc;
int a[30001];
int a2[30001];
int v[30001];
bool c[30001];
int r[2][30001];
vi ch;
int n,i,j,tp;
int rezz;
void rec(int lv)
{
	int i=lv;
	if (lv==0)
	{
		if (a2[1]==tp)
			rezz=min(rezz,L(ch));
		return;
	}
		if (a[i]==1)
			a2[i]=a2[2*i]&a2[2*i+1];
		else
			a2[i]=a2[2*i]|a2[2*i+1];
		rec(lv-1);
		if (c[i]!=1)
			return;
	if (a[i]==1)
	{
		ch.pb(0);
		a2[i]=a2[2*i]|a2[2*i+1];
		rec(lv-1);
		ch.ppb();
	}
	else
	{
		ch.pb(0);
		a2[i]=a2[2*i]&a2[2*i+1];
		rec(lv-1);
		ch.ppb();
	}
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>cnt;
	for(cc=1;cc<=cnt;cc++)
	{
		cin>>n>>tp;
		for(i=1;i<=(n-1)/2;i++)
			cin>>a[i]>>c[i];
		for(i=((n-1)/2)+1;i<=n;i++)
		{
			cin>>v[i];
			a2[i]=v[i];
		}
		for(i=1;i<=n;i++)
		{
			r[0][i]=inf;
			r[1][i]=inf;
		}
		for(i=((n-1)/2)+1;i<=n;i++)
			r[v[i]][i]=0;
		for(i=(n-1)/2;i>0;i--)
		{
				if (a[i]==1)
				{
					r[0][i]=min(r[0][i],r[0][2*i]+r[0][2*i+1]);
					r[0][i]=min(r[0][i],r[0][2*i]+r[1][2*i+1]);
					r[0][i]=min(r[0][i],r[1][2*i]+r[0][2*i+1]);
					r[1][i]=min(r[1][i],r[1][2*i]+r[1][2*i+1]);
				}
				else
				{
					r[0][i]=min(r[0][i],r[0][2*i]+r[0][2*i+1]);
					r[1][i]=min(r[1][i],r[0][2*i]+r[1][2*i+1]);
					r[1][i]=min(r[1][i],r[1][2*i]+r[0][2*i+1]);
					r[1][i]=min(r[1][i],r[1][2*i]+r[1][2*i+1]);
				}
				if (c[i]!=1)
					continue;
				if (a[i]==1)
				{
					r[0][i]=min(r[0][i],1+r[0][2*i]+r[0][2*i+1]);
					r[1][i]=min(r[1][i],1+r[0][2*i]+r[1][2*i+1]);
					r[1][i]=min(r[1][i],1+r[1][2*i]+r[0][2*i+1]);
					r[1][i]=min(r[1][i],1+r[1][2*i]+r[1][2*i+1]);
				}
				else
				{
					r[0][i]=min(r[0][i],1+r[0][2*i]+r[0][2*i+1]);
					r[0][i]=min(r[0][i],1+r[0][2*i]+r[1][2*i+1]);
					r[0][i]=min(r[0][i],1+r[1][2*i]+r[0][2*i+1]);
					r[1][i]=min(r[1][i],1+r[1][2*i]+r[1][2*i+1]);
				}
		}
		cout<<"Case #"<<cc<<": ";
		if (r[tp][1]==inf)
			cout<<"IMPOSSIBLE\n";
		else
			cout<<r[tp][1]<<endl;
		ch.clear();
		rezz=inf;
	//	rec((n-1)/2);
	//	cout<<rezz<<endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}