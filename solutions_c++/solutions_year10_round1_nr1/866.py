#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>
#include<algorithm>
using namespace std;

const int N=100;
char a[N][N],b[N][N];
int dx[]={1,0,1,1},dy[]={0,1,1,-1};
int n;
int cnt(char c,int x,int y,int dir)
{
	if(b[x][y]!=c) return 0;
	int s=0;
	int i;
	int tx,ty;
	for(i=0;;i++)
	{
		tx=x+i*dx[dir];
		ty=y+i*dy[dir];
		if(tx>=0&&tx<n&&ty>=0&&ty<n&&b[tx][ty]==c)
			s++;
		else break;
	}
	return s;
}


int main()
{
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	int t,K,k,i,j;
	scanf("%d",&t);
	int cs=0;
	while(t--)
	{
		cs++;
		scanf("%d%d",&n,&K);
		for(i=0;i<n;i++)
			scanf("%s",a[i]);

		for(i=0;i<n;i++)
			for(j=0;j<n;j++) b[i][j]=a[n-1-j][i];

        int m;
		for(j=0;j<n;j++)
		{
			vector<char> c(0);
			for(i=n-1;i>=0;i--) if(b[i][j]!='.') c.push_back(b[i][j]);
//			printf("x=%d\n",c.size());
			m=n-1;
			for(i=0;i<c.size();i++) b[m--][j]=c[i];
			for(;m>=0;m--) b[m][j]='.';
		}

		int s1=0,s2=0;
		for(i=0;i<n;i++)
			for(j=0;j<n;j++) 
			  for(k=0;k<4;k++) 
			  {
				  s1=max(s1,cnt('B',i,j,k));
				  s2=max(s2,cnt('R',i,j,k));
			  }
		printf("Case #%d: ",cs);
		if(s1>=K&&s2>=K) printf("Both\n");
		if(s1>=K&&s2<K) printf("Blue\n");
		if(s1<K&&s2>=K) printf("Red\n");
		if(s1<K&&s2<K) printf("Neither\n");
	}
	return 0;
}
		

		




		


