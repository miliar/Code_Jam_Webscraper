#include<iostream>
#include<cstring>
#include<cstdlib>

const int dir[8][2]={
	{0,1},
	{0,-1},
	{-1,0},
	{1,0},
	{1,1},
	{-1,-1},
	{1,-1},
	{-1,1},
};



using namespace std;

int s[100][100];
int s1[100][100];
int i,j,k,l,m,n;
int ii,t;




void falldown()
{
	int o,u,y,z;
	for (o=1;o<=n;o++)
	{
		u=n;y=n;
		while (u>=1)
		{
			if (s1[u][o]=='.')
			{
			  while (s1[u][o]=='.' &&  u>=1)
			    u--;
			  if (u>=1)
			  {
			   	  s1[y][o]=s1[u][o];
				  s1[u][o]='.';
				  y--;
			  }
			}
			else {u--;y--;}
		}
	}
}
int check1()
{
	int o,u,x,y,z,p,q;
	int r,b;
	r=0;
	b=0;
	for (o=n;o>=1;o--)
		for (u=n;u>=1;u--)
		if (s1[o][u]=='R' || s1[o][u]=='B')
		 {
			 for (y=0;y<8;y++)
			 {
				 int p1,q1;
                 p=o;q=u;
				 x=0;
                 p1=p+dir[y][0];q1=q+dir[y][1];
                 while (p1>0 && p1<=n && q1>0 && q1<=n && s1[p1][q1] == s1[p][q])
				 {
					 p=p1;
					 q=q1;
					 x++;
					 p1=p+dir[y][0];q1=q+dir[y][1];
				 }
				 if (x==k-1)
				 {
					 if (s1[o][u]=='R') r=1;
					 if (s1[o][u]=='B') b=2;
				 }
			 }
		 }
	return r+b;
}




int main()
{
char tmp[100];
	freopen("tmp.in","r",stdin);
	freopen("tmp.out","w",stdout);
	scanf("%d",&t);
	for (ii=1;ii<=t;ii++)
	{
		memset(s,0,sizeof(s));
		memset(s1,0,sizeof(s1));
		scanf("%d%d",&n,&k);
		for (i=1;i<=n;i++)
		{
			gets(tmp);
			for (j=1;j<=n;j++)
				scanf("%c",&s[i][j]);
		}
		for (i=1;i<=n;i++)
			for (j=1;j<=n;j++)
				s1[j][i]=s[n-i+1][j];
		falldown();
		j=check1();
		printf("Case #%d: ",ii);
		if (j==0) printf("Neither\n");
		if (j==1) printf("Red\n");
		if (j==2) printf("Blue\n");
		if (j==3) printf("Both\n");
	}
}