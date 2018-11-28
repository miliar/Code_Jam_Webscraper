#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<map>
#include<set>
#include<vector>
#include<algorithm>
#include<string>
#include<cmath>
using namespace std;

bool a[200][200];
int v[200][50];
int n,m,i,j,k,l,sol;
int b[1<<16],N;

int bad(int x1,int x2,int y1,int y2)
{
	if(x1==y1 || x2==y2) return true;
	if(x1<y1 && x2>y2) return true;
	if(x1>y1 && x2<y2) return true;
	return false;
}

int bitCount(int x)
{
	int nr = 0,i;
	for(i=0;i<n;++i)
		if(x&(1<<i))
			++nr;
	return nr;
}

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int T,I;
	cin>>T;
	for(I=1;I<=T;++I)
	{
		cin>>n>>m;
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		for(i=1;i<=n;++i)
			for(j=1;j<=m;++j)
				cin>>v[i][j];
		for(i=1;i<n;++i)
			for(j=i+1;j<=n;++j)
			{
				a[i][j]=a[j][i]=false;
				for(k=1;k<m;++k)
				{
					if(bad(v[i][k],v[i][k+1],v[j][k],v[j][k+1]))
					{
						a[i][j] = a[j][i] = true;
						break;
					}
				}
			}

		sol = 0;
		N = 1<<n;
		b[0] = 1;
		for(i=0;i<N;++i)
			if(b[i])
			{
				sol = max(sol,bitCount(i));
				for(j=0;j<n;++j)
				{
					if(i&(1<<j))
						continue;
					for(k=0;k<n;++k)
						if(i&(1<<k))
							if(!a[j+1][k+1]) goto LOOP;
					;
					b[i+(1<<j)]=1;
LOOP:
					;
				}
			}
		cout<<"Case #"<<I<<": "<<sol<<endl;
	}
	return 0;
}
