#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <bitset>
#include <string>
#include <vector>
#include <algorithm>
#include <ctime>
#include <queue>
#include <cstring>
#include <set>
#include <map>
#include <sstream>
#include <cmath>
#include <fstream>
#include <list>
using namespace std;
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
int a[555][555];
int s[555][555];
int dx[555][555];
int dy[555][555];
int n,m,k,tests;
inline int sum(int si,int sj,int fi,int fj,int s[][555])
{
	if (si<=0 && sj<=0)
		return s[fi][fj];
	if (si<=0)
		return s[fi][fj]-s[fi][sj-1];
	if (sj<=0)
		return s[fi][fj]-s[si-1][fj];

	return s[fi][fj]-s[fi][sj-1]-s[si-1][fj]+s[si-1][sj-1];
}
inline int value(int si,int sj,int fi,int fj,int i,int j,int tp)
{
	if (tp==0)
		return sum(si,sj,fi,fj,dx)+sum(si,sj,fi,fj,s)*(si-i);
	else
		return sum(si,sj,fi,fj,dy)+sum(si,sj,fi,fj,s)*(sj-j);
}
inline bool check(int k)
{
	rp(i,n)
		rp(j,m)
		{
			int si=i-k/2;
			int sj=j-k/2;
			if (si<0 || sj<0) continue;
			int fi=i+k/2-(k+1)%2;
			int fj=j+k/2-(k+1)%2;
			if (fi>=n || fj>=m) continue;
			if (k==4 && si==0 && sj==0)
				k=k;
			int dx=0,dy=0;
			for(int pi=si;pi<=fi;++pi)
				for(int pj=sj;pj<=fj;++pj)
				{
						dx+=a[pi][pj]*(2*pj-2*j+(k+1)%2);
						dy+=a[pi][pj]*(2*pi-2*i+(k+1)%2);
				}
			if (dx==a[si][sj]*(2*sj-2*j+(k+1)%2)+a[fi][sj]*(2*sj-2*j+(k+1)%2)+
				a[si][fj]*(2*fj-2*j+(k+1)%2)+a[fi][fj]*(2*fj-2*j+(k+1)%2))
				if (dy==a[si][sj]*(2*si-2*i+(k+1)%2)+a[si][fj]*(2*si-2*i+(k+1)%2)+
					a[fi][sj]*(2*fi-2*i+(k+1)%2)+a[fi][fj]*(2*fi-2*i+(k+1)%2))
					return 1;
		}
	return 0;
}
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>tests;
	for(int test=1;test<=tests;++test)
	{
		cin>>n>>m>>k;
		C(s);
		rp(i,n)
			rp(j,m)
			{
				char ch;
				cin>>ch;
				a[i][j]=ch-'0';
				if (!i && !j)
				{
					s[i][j]=a[i][j];
					dx[i][j]=dy[i][j]=0;
				}
				else
					if (!i)
					{
						s[i][j]=a[i][j]+s[i][j-1];
						dx[i][j]=0;
						dy[i][j]=dy[i][j-1]+a[i][j]*j;
					}
					else
						if (!j)
						{
							s[i][j]=a[i][j]+s[i-1][j];
							dx[i][j]=dx[i-1][j]+a[i][j]*i;
							dy[i][j]=0;
						}
						else
						{
							s[i][j]=a[i][j]+s[i-1][j]+s[i][j-1]-s[i-1][j-1];
							dx[i][j]=a[i][j]*i+dx[i-1][j]+dx[i][j-1]-dx[i-1][j-1];
							dy[i][j]=a[i][j]*j+dy[i-1][k]+dy[i][j-1]-dy[i-1][j-1];
						}

			}
		for(k=min(n,m);k>2 && !check(k);--k);
		cout<<"Case #"<<test<<": ";
		if (k==2)
			cout<<"IMPOSSIBLE\n";
		else
			cout<<k<<endl;

	}
}