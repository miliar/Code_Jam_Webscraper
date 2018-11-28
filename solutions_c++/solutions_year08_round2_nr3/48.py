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
/*
int A,B,P;
int i,j,k;
int m[1001][1001];
int u[1001];
inline bool prime(int x)
{
	for(int i=2;i*i<=x;i++)
		if (x%i==0)
			return false;
	return true;
}
void dfs(int v)
{
	u[v]=true;
	for(int i=A;i<=B;i++)
		if (!u[i]&&m[v][i])
			dfs(i);
}

	cin>>A>>B>>P;
		C(m,0);
		for(i=A;i<B;i++)
			for(j=i+1;j<=B;j++)
			{
				k=P;
				while(k<=i&&!(prime(k)&&i%k==0&&j%k==0))
					k++;
				if (k<=i)
				{
					m[i][j]=1;
					m[j][i]=1;
				}
			}
		int rez=0;
		C(u,0);
		for(i=A;i<=B;i++)
			if (!u[i])
			{
				rez++;
				dfs(i);
			}
*/
int n,k;
int a[1000000];
int p[100];
int i,j,l;
class tree_vertex
{
public:
	int a,m;
};
typedef tree_vertex tree_arr[10000000];
tree_arr t;
void change_sum_tree(tree_arr &a,int v,int l,int r,int lx,int rx,int d)
{
	if (lx>=rx)
		return;
	if (l==lx&&r==rx)
	{
		a[v].a+=d;
		a[v].m+=(rx-lx)*d;
		return;
	}
	int mid=(l+r+1)/2;
	change_sum_tree(a,2*v+1,l,mid,lx,min(mid,rx),d);
	change_sum_tree(a,2*v+2,mid,r,max(mid,lx),rx,d);
	a[v].m+=(rx-lx)*d;
}
int get_sum(tree_arr &a,int v,int l,int r,int lx,int rx)
{
	if (lx>=rx)
		return 0;
	if (l==lx&&r==rx)
		return a[v].m;
	int mid=(l+r+1)/2;
	return (rx-lx)*a[v].a+get_sum(a,2*v+1,l,mid,lx,min(mid,rx))+get_sum(a,2*v+2,mid,r,max(mid,lx),rx);
}
int low,high,h,sm;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>cnt;
	for(cc=1;cc<=cnt;cc++)
	{
		cin>>n;
		cin>>k;
		for(i=0;i<k;i++)
			cin>>p[i];
		for(i=0;i<n;i++)
			a[i]=-1;
		for(i=0;i<10*n;i++)
		{
			t[i].a=0;
			t[i].m=0;
		}
		change_sum_tree(t,0,0,n,0,n,1);
		i=0;
		for(j=1;j<=n;j++)
		{
			sm=j;
			h=get_sum(t,0,0,n,i,n);
			if (h<sm)
			{
				i=0;
				sm-=h;
				h=get_sum(t,0,0,n,i,n);
				if (h<sm)
				{
					sm=sm%h;
					if (sm==0)
						sm=h;
				}
			}
			low=i;
			high=n-1;
			while(high-low>1)
			{
				h=(low+high)/2;
				if (get_sum(t,0,0,n,i,h+1)<sm)
					low=h+1;
				else
					high=h;
			}
			if (get_sum(t,0,0,n,i,low+1)==sm)
				i=low;
			else
				i=high;
			a[i]=j;
			change_sum_tree(t,0,0,n,i,i+1,-1);
		}
	//	for(i=0;i<n;i++)
	//		cout<<a[i]<<" ";
	//	cout<<endl;
		cout<<"Case #"<<cc<<": ";
		for(i=0;i<k;i++)
			cout<<a[p[i]-1]<<" ";
		cout<<endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}