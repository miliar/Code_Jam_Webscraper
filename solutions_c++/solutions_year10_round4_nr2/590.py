#include <stdio.h>
#include<iostream>
#include<string>
#include<vector>
#include<map>
using namespace std;

const int maxn = 1030;

int c[maxn][maxn],m[maxn];
int P,size,N;
int v[4000];
int d[4000][20];

int ret;

void solve(int p,int l,int r)
{
	int c=p*2;
	int i,j,k;
	if( l==r ){
		if( m[l] )
		{
			ret += v[p];
		}
		return ;
	}

	int mid = (l+r)/2;
	
	for(i=l;i<=r;i++){
		if( m[i] )break;
	}
	if( i<=r )
	{

		ret += v[p];
		for(j=l;j<=r;j++)if( m[j] )m[j]--;
		solve(c,l,mid);
		solve(c+1,mid+1,r);

	}
	else return ;

}

void update(int &x,int v)
{
	if( x==-1 || x>v )x=v;
}

void dp(int u,int l,int r,int lev)
{
	if( l==r )
	{
		
		if( m[l] ){
			/*d[u][ m[l]-1 ] = v[u];
		}
		else if( m[l]!=0 ){
			d[u][ m[l]-1 ] = v[u];*/

			d[u][ m[l] ] = 0;
		}
		else if( m[l]==0 )
		{
			d[u][0]=0;
		}		
		return ;
	}
	

	int c=u*2,ln,rn,cn;
	int mid = (l+r)/2;
	dp(c,l,mid,lev+1);
	dp(c+1,mid+1,r,lev+1);

	for(int i=0;i<=P;i++)
	{
		if( d[c][i] != -1)
		for(int j=0;j<=P;j++)
		if( d[c+1][j]!= -1 ){
			int n = max(i,j);
			if( n >= lev )// bi xuan
			{
				update(d[u][n-1],d[c][i]+d[c+1][j]+v[u]);
			}
			else if(n!=0){
				update(d[u][n-1],d[c][i]+d[c+1][j]+v[u]);
				update(d[u][n],d[c][i]+d[c+1][j]);
			}
			else {
				update(d[u][n],d[c][i]+d[c+1][j]);
			}

		}
	}

	
}

int main(){
	//freopen("B-large.in","r",stdin);
	//freopen("B-large.out","w",stdout);
	int i,j,k;
	int T;
	scanf("%d",&T);
	for(int ca=1;ca<=T;ca++)
	{
		ret = 0;
		scanf("%d",&P);
		size = 1<<P;
		for(i=0;i<size;i++)
		{
			cin>>m[i];
			m[i]=P-m[i];
		}
		k=size;
		for(i=1;i<=P;i++)
		{
			k/=2;
			for(j=0;j<k;j++)cin>>c[i][j];
		}
		N=0;
		k=1;
		for(i=P;i>=1;i--)
		{
			
			for(j=0;j<k;j++)v[++N]=c[i][j];
			k*=2;
		}

		memset(d,-1,sizeof(d));
		dp(1,0,size-1,1);
		printf("Case #%d: %d\n",ca,d[1][0]);
	}
}

/*
3
2
2 2 0 0
1 1
1

3
1
1 1
100

3
3 
1 2 3 2 1 0 1 3 
100 150 50 90 
500 400 
800 
*/