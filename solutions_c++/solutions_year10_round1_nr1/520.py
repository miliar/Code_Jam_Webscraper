#include<iostream>
#include<iostream>
using namespace std;
char str[100][100],str1[100][100];
int n,k;
struct stu
{
	int x,y;
};
int ar[8]={0,0,1,-1,1,1,-1,-1},br[8]={1,-1,0,0,1,-1,1,-1};
bool sech(int x,int y)
{
	int i,xx,yy;
	for(i=1;i<k;i++)
	{
		xx=x+ar[0]*i;
		yy=y+br[0]*i;
		if(xx<0||yy<0||xx>=n||yy>=n)break;
		if(str1[xx][yy]!=str1[x][y])break;
	}
	if(i==k)return 1;

	for(i=1;i<k;i++)
	{
		xx=x+ar[1]*i;
		yy=y+br[1]*i;
		if(xx<0||yy<0||xx>=n||yy>=n)break;
		if(str1[xx][yy]!=str1[x][y])break;
	}
	if(i==k)return 1;

	for(i=1;i<k;i++)
	{
		xx=x+ar[2]*i;
		yy=y+br[2]*i;
		if(xx<0||yy<0||xx>=n||yy>=n)break;
		if(str1[xx][yy]!=str1[x][y])break;
	}
	if(i==k)return 1;

	for(i=1;i<k;i++)
	{
		xx=x+ar[3]*i;
		yy=y+br[3]*i;
		if(xx<0||yy<0||xx>=n||yy>=n)break;
		if(str1[xx][yy]!=str1[x][y])break;
	}
	if(i==k)return 1;

	for(i=1;i<k;i++)
	{
		xx=x+ar[4]*i;
		yy=y+br[4]*i;
		if(xx<0||yy<0||xx>=n||yy>=n)break;
		if(str1[xx][yy]!=str1[x][y])break;
	}
	if(i==k)return 1;

	for(i=1;i<k;i++)
	{
		xx=x+ar[5]*i;
		yy=y+br[5]*i;
		if(xx<0||yy<0||xx>=n||yy>=n)break;
		if(str1[xx][yy]!=str1[x][y])break;
	}
	if(i==k)return 1;

	for(i=1;i<k;i++)
	{
		xx=x+ar[6]*i;
		yy=y+br[6]*i;
		if(xx<0||yy<0||xx>=n||yy>=n)break;
		if(str1[xx][yy]!=str1[x][y])break;
	}
	if(i==k)return 1;

	for(i=1;i<k;i++)
	{
		xx=x+ar[7]*i;
		yy=y+br[7]*i;
		if(xx<0||yy<0||xx>=n||yy>=n)break;
		if(str1[xx][yy]!=str1[x][y])break;
	}
	if(i==k)return 1;
	return 0;
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,i,j,a,g=0;
	
	scanf("%d",&t);
	bool rflag,bflag;
	while(t--)
	{
		g++;
		rflag=0;bflag=0;
		scanf("%d %d",&n,&k);
		for(i=0;i<n;i++)
		{
			scanf("%s",str[i]);
		}
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			{
				str1[j][n-i-1]=str[i][j];
			}
		}
		char st;
		for(j=0;j<n;j++)
		{
			a=n-1;
			for(i=n-1;i>=0;i--)
			{
				if(str1[i][j]!='.')
				{
					st=str1[i][j];
					str1[i][j]='.';
					str1[a][j]=st;
					a--;
				}
			}
		}
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			{
				if(str1[i][j]=='.')continue;
				if(str1[i][j]=='R')
				{
					if(sech(i,j))rflag=1;
				}
				if(str1[i][j]=='B')
				{
					if(sech(i,j))bflag=1;
				}
			}
		}
		printf("Case #%d: ",g);
		if(rflag&&bflag)printf("Both\n");
		else if(rflag) printf("Red\n");
		else if(bflag) printf("Blue\n");
		else printf("Neither\n");
	}
	return 0;
}