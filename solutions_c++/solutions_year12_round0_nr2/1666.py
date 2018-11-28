#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

#define F(i,a,b) for(i=a;i<=b;++i)

int x[111],memo[111][111][111];

int MAX(int a,int b)
{
	if(a>b) return a;
	return b;
}

int calc(int n,int s,int p)
{
	int i,j,k,y;
	memset(memo,-1,sizeof(memo));

	memo[0][0][0] = 0;

	F(i,1,n){
		F(j,0,i-1){
			k = (i-1)-j;
			if(memo[i-1][j][k]==-1) continue;

			//printf("%d %d %d\n",i,j,k);

			if(x[i]>1&&x[i]<29){
				y = (x[i]+1)/3+1;
				//printf("a %d -> %d\n",x[i],y);
				if(y>=p) memo[i][j+1][k] = MAX(memo[i-1][j][k]+1,memo[i][j+1][k]);
				else memo[i][j+1][k] = MAX(memo[i-1][j][k],memo[i][j+1][k]);
			}

			y = x[i]/3;
			if(x[i]%3) y++;
			//printf("b %d -> %d\n",x[i],y);
			if(y>=p) memo[i][j][k+1] = MAX(memo[i-1][j][k]+1,memo[i][j][k+1]);
			else memo[i][j][k+1] = MAX(memo[i-1][j][k],memo[i][j][k+1]);
		}
		//printf("\n");
	}

	return memo[n][s][n-s];	
}

int main()
{
	//freopen("B-large.in","r",stdin);
	//freopen("B-large.out","w",stdout);

	int t,cs=0,i,n,s,p;
	scanf("%d",&t);
	while(t--){
		scanf("%d%d%d",&n,&s,&p);
		F(i,1,n) scanf("%d",&x[i]);
		printf("Case #%d: %d\n",++cs,calc(n,s,p));
	}

	return 0;
}