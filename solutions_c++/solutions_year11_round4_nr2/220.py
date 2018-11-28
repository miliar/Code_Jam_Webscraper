#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define N 555
int n,m,d,a[N][N],s[N][N],s1[N][N],s2[N][N],s3[N][N],s4[N][N],S;
int askW(int(*s)[N],int x1,int x2,int y1,int y2)
{
	return s[x2][y2]-s[x2][y1-1]-s[x1-1][y2]+s[x1-1][y1-1];
}
int askJ1(int x1,int x2,int y1,int y2)
{
	return askW(s1,x1,x2,y1,y2);
}
int askJ2(int x1,int x2,int y1,int y2)
{
	return askW(s2,x1,x2,y1,y2);
}
int askJ3(int x1,int x2,int y1,int y2)
{
	return askW(s3,x1,x2,y1,y2);
}
int askJ4(int x1,int x2,int y1,int y2)
{
	return askW(s4,x1,x2,y1,y2);
}
int askS(int x1,int x2,int y1,int y2)
{
	return askW(s,x1,x2,y1,y2);
}
int askL1(int x1,int x2,int y1,int y2)
{
//	printf("L%d %d %d %d\n",x1,x2,y1,y2);
//	printf("%d %d\n",askJ2(x1,x2,y1,y2),askS(x1,x2,y1,y2)*(m-y2));
	return askJ2(x1,x2,y1,y2)-askS(x1,x2,y1,y2)*(m-y2)-(a[x1][y1]+a[x2][y1])*(y2-y1+1);
}
int askR1(int x1,int x2,int y1,int y2)
{
//	printf("R%d %d %d %d\n",x1,x2,y1,y2);
	return askJ1(x1,x2,y1,y2)-askS(x1,x2,y1,y2)*(y1-1)-(a[x1][y2]+a[x2][y2])*(y2-y1+1);
}
int askU1(int x1,int x2,int y1,int y2)
{
//	printf("U%d %d %d %d\n",x1,x2,y1,y2);
	return askJ4(x1,x2,y1,y2)-askS(x1,x2,y1,y2)*(n-x2)-(a[x1][y1]+a[x1][y2])*(x2-x1+1);
}
int askD1(int x1,int x2,int y1,int y2)
{
//	printf("D%d %d %d %d\n",x1,x2,y1,y2);
	return askJ3(x1,x2,y1,y2)-askS(x1,x2,y1,y2)*(x1-1)-(a[x2][y1]+a[x2][y2])*(x2-x1+1);
}
int askL2(int x1,int x2,int y1,int y2)
{
//	printf("L%d %d %d %d\n",x1,x2,y1,y2);
	return askJ2(x1,x2,y1,y2)*2-askS(x1,x2,y1,y2)*((m-y2+1)*2-1)-(a[x1][y1]+a[x2][y1])*((y2-y1+1)*2-1);
}
int askR2(int x1,int x2,int y1,int y2)
{
//	printf("R%d %d %d %d\n",x1,x2,y1,y2);
	return askJ1(x1,x2,y1,y2)*2-askS(x1,x2,y1,y2)*(y1*2-1)-(a[x1][y2]+a[x2][y2])*((y2-y1+1)*2-1);
}
int askU2(int x1,int x2,int y1,int y2)
{
//	printf("U%d %d %d %d\n",x1,x2,y1,y2);
	return askJ4(x1,x2,y1,y2)*2-askS(x1,x2,y1,y2)*((n-x2+1)*2-1)-(a[x1][y1]+a[x1][y2])*((x2-x1+1)*2-1);
}
int askD2(int x1,int x2,int y1,int y2)
{
//	printf("D%d %d %d %d\n",x1,x2,y1,y2);
	return askJ3(x1,x2,y1,y2)*2-askS(x1,x2,y1,y2)*(x1*2-1)-(a[x2][y1]+a[x2][y2])*((x2-x1+1)*2-1);
}
bool canB(int x,int y,int c)
{
//	printf("%d %d %d %d\n",askU1(x-c+1,x-1,y-c+1,y+c-1),askD1(x+1,x+c-1,y-c+1,y+c-1),askL1(x-c+1,x+c-1,y-c+1,y-1),askR1(x-c+1,x+c-1,y+1,y+c-1));
//	return 0;
	return
		askU1(x-c+1,x-1,y-c+1,y+c-1) == askD1(x+1,x+c-1,y-c+1,y+c-1) &&
		askL1(x-c+1,x+c-1,y-c+1,y-1) == askR1(x-c+1,x+c-1,y+1,y+c-1);
}
bool canC(int x,int y,int c)
{
	//printf("%d %d %d %d\n",askU2(x-c+1,x,y-c+1,y+c),askD2(x+1,x+c,y-c+1,y+c),askL2(x-c+1,x+c,y-c+1,y),askR2(x-c+1,x+c,y+1,y+c));
	//return 0;
	return
		askU2(x-c+1,x,y-c+1,y+c) == askD2(x+1,x+c,y-c+1,y+c) &&
		askL2(x-c+1,x+c,y-c+1,y) == askR2(x-c+1,x+c,y+1,y+c);
}
int chkB(int x,int y)
{
	int S=-1;
	for(int T=2;1<=x-T+1&&x+T-1<=n&&1<=y-T+1&&y+T-1<=m;T++)
		if(canB(x,y,T))S=max(S,T*2-1);
	return S;
}
int chkC(int x,int y)
{
	int S=-1;
	for(int T=2;1<=x-T+1&&x+T<=n&&1<=y-T+1&&y+T<=m;T++)
		if(canC(x,y,T))S=max(S,T*2);
	return S;
}
int main()
{
	int _;scanf("%d",&_);
	for(int __=1;__<=_;__++)
	{
		scanf("%d%d%d",&n,&m,&d);
		for(int i=1;i<=n;i++)
		{
			char s[N];
			scanf("%s",s);
			for(int j=1;j<=m;j++)
				a[i][j]=s[j-1]-'0';
		}
		S=-1;
		//preCalc
		memset(s,0,sizeof s);
		memset(s1,0,sizeof s1);
		memset(s2,0,sizeof s2);
		memset(s3,0,sizeof s3);
		memset(s4,0,sizeof s4);
		for(int i=1;i<=n;i++)
			for(int j=1;j<=m;j++)
				s[i][j]=s[i-1][j]+s[i][j-1]-s[i-1][j-1]+a[i][j];
		for(int i=1;i<=n;i++)
			for(int j=1;j<=m;j++)
				s1[i][j]=s1[i-1][j]+s1[i][j-1]-s1[i-1][j-1]+a[i][j]*j;
		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++)
				s2[i][j]=s2[i-1][j]+s2[i][j-1]-s2[i-1][j-1]+a[i][j]*(m-j+1);
		for(int i=1;i<=n;i++)
			for(int j=1;j<=m;j++)
				s3[i][j]=s3[i-1][j]+s3[i][j-1]-s3[i-1][j-1]+a[i][j]*i;
		for(int i=1;i<=n;i++)
			for(int j=1;j<=m;j++)
				s4[i][j]=s4[i-1][j]+s4[i][j-1]-s4[i-1][j-1]+a[i][j]*(n-i+1);
		//printf("%d\n",canC(2,2,2));return 0;
		//printf("%d\n",canB(4,4,3));return 0;
		//checkBlock
		for(int i=1;i<=n;i++)
			for(int j=1;j<=m;j++)
			{
				S=max(S,chkB(i,j));
				//if(chkB(i,j)==7)printf("%d %d\n",i,j);
			}
		//check~Block
		for(int i=1;i<n;i++)
			for(int j=1;j<m;j++)
				S=max(S,chkC(i,j));
		printf("Case #%d: ",__);
		if(S==-1)puts("IMPOSSIBLE");
		else printf("%d\n",S);
	}
	return 0;
}

