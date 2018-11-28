#include <iostream>
#include <sstream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <deque>
#include <list>
#include <map>
#include <set>
using namespace std;
#define all(a) (a).begin(),(a).end()
#define mset(a,v) memset(a,v,sizeof(a))
#define pb push_back
#define sz(a) a.size()
#define rep(i,n) for(i=0; i<n; i++)
#define forr(i,a,b) for(i=a; i<=b; i++)
#define ford(i,a,b) for(i=a; i>=b; i--)
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define X first
#define Y second
typedef long long ll;
typedef vector<int> VI;

FILE* fi; FILE* fo;
int i,j, u,N, n,a,b,c,d, M;
int x[100000], y[100000];
ll k[3][3], res, v;
int i1,i2,i3, j1,j2,j3;

int main()
{
	fi=fopen("a-large.in","r");
	fo=fopen("a-large.res","w");
	fscanf(fi,"%d",&N);
	rep(u,N)
	{
		fscanf(fi,"%d%d%d%d%d%d%d%d",&n,&a,&b,&c,&d,&x[0],&y[0],&M);
		rep(i,n-1) x[i+1]=(ll(a)*x[i]+b) % M,	y[i+1]=(ll(c)*y[i]+d) % M;
		rep(i,3) rep(j,3) k[i][j]=0;
		rep(i,n) k[x[i]%3][y[i]%3]++;
		res=0;
		rep(i1,3) forr(i2,i1,2) forr(i3,i2,2) if((i1+i2+i3)%3==0)
			rep(j1,3) rep(j2,3) rep(j3,3) if((j1+j2+j3)%3==0)
			{
				if(i1==i2 && j1>j2) continue;
				if(i2==i3 && j2>j3) continue;
				v=(ll)k[i1][j1]; 
				if(i1==i2 && j1==j2)
				{
						v=v*(k[i2][j2]-1)/2;
						if(i2==i3 && j2==j3) v=v*(k[i3][j3]-2)/3;
						else v=v*k[i3][j3];
				}
				else
				{
					v=v*(k[i2][j2]);
					if(i2==i3 && j2==j3) v*(k[i3][j3]-1)/2;
					else v=v*k[i3][j3];
				}
				res+=v;
			}
		cout<<"Case #"<<u+1<<": "<<res<<'\n';
		fprintf(fo,"Case #%d: %I64u\n",u+1,res);
	}
	fclose(fi); fclose(fo);
	getchar();
	return 0;
}
