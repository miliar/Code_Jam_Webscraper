#include <iostream>

using namespace std;

int n,k;

char buf[100][100];

void stand()
{
	int i,j;
	for(j=0;j<n;j++)
	{
		int bg=n-1;
		for(i=n-1;i>=0;i--)
		{
			if(buf[i][j]!='.')
			{
				buf[bg--][j]=buf[i][j];
			}
		}
		while(bg>=0)
		{
			buf[bg--][j]='.';
		}
	}
}

char tmp[100][100];

void rotate()
{
	int i,j;
	memcpy(tmp,buf,sizeof(buf));
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			buf[i][j]=tmp[n-1-j][i];
		}
	}
}

bool check(char c,int x,int y,int dx,int dy)
{
	int cnt=0;
	while(x>=0&&x<n&&y>=0&&y<n&&buf[x][y]==c)
	{
		cnt++;
		x+=dx;
		y+=dy;
	}
	return cnt>=k;
}

bool check(char c)
{
	int i,j;
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			if(check(c,i,j,1,0)
				||check(c,i,j,0,1)
				||check(c,i,j,1,1)
				||check(c,i,j,1,-1)) return true;
		}
	}
	return false;
}

int main()
{
	int t;
	scanf("%d",&t);
	int cse=0;
	while(t--)
	{
		cse++;
		scanf("%d%d",&n,&k);
		int i;
		for(i=0;i<n;i++) scanf("%s",buf[i]);
		stand();
		rotate();
		stand();
		bool b1=check('R');
		bool b2=check('B');
		if(b1&&b2) printf("Case #%d: Both\n",cse);
		if(b1&&!b2) printf("Case #%d: Red\n",cse);
		if(!b1&&b2) printf("Case #%d: Blue\n",cse);
		if(!b1&&!b2) printf("Case #%d: Neither\n",cse);
	}
	return 0;
}
