#include <iostream>
using namespace std;

char a[110][110];
char b[110][110];

int N,K;

int check1(char x)
{
	for(int i=0;i<N;i++)
	{
		int count1 = 0;
		int count2 = 0;
		for(int j=0;j<N;j++)
		{
			if(b[i][j]==x)
				count1++;
			else
				count1 = 0;
			if(b[j][i]==x)
				count2++;
			else
				count1 = 0;
			if(count1 == K || count2 == K)
				return 1;
		}
	}
	return 0;
}

int check3(int x,int y,char t)
{
	int dir[4][2] = {{-1,1},{1,1},{0,1},{1,0}};
	int tx=x;
	int ty=y;
	
	for(int d=0;d<=3;d++)
	{
		int result = true;
		tx = x;
		ty = y;
		for(int i=0;i<K;i++)
		{
			if(tx<0 || tx>N-1 || ty<0 || ty>N-1)
			{
				result = false;
			}
			if(b[tx][ty] != t) result = false;

			tx += dir[d][0];
			ty += dir[d][1];
		}
		if(result == true) return 1;
	}
	return 0;
}

int check2(char x)
{
	for(int i=0;i<N;i++)
	{
		for(int j=0;j<N;j++)
		{
			if(b[i][j] == x && check3(i,j,x))
				return 1;
		}
	}
	return 0;
}

int check(char x)
{
	printf("check1:%c=%d\n",x,check1(x));
	printf("check2:%c=%d\n",x,check2(x));
	if(check1(x)||check2(x))
		return 1;
	return 0;
}

void solve()
{
	memset(a,0,sizeof(a));

	scanf("%d%d",&N,&K);
	gets(a[0]);
	for(int i=0;i<N;i++)
	{
		scanf("%s",a[i]);
	}

	memset(b,0,sizeof(b));
	for(int i=0;i<N;i++)
	{
		int k = 0;
		//for(int j=N;j>=0;j--)
		for(int j=0;j<N;j++)
		{
			char cur = a[N-i-1][N-j-1];
			if(cur == 'R' || cur=='B')
			{
				b[k][i] = cur;
				k++;
			}
		}
	}
/*
	puts("---");
	for(int i=N-1;i>=0;i--)
	{
		for(int j=0;j<N;j++)
		{
			if(b[i][j])
			{
				printf("%c",b[i][j]);
			}
			else
			{
				printf(" ");
			}
		}
		puts("");
	}
	puts("---");
*/
	int cb = check2('B');
	int cr = check2('R');
	if(cb && cr)
		puts("Both");
	else if( cb)
		puts("Blue");
	else if(cr)
		puts("Red");
	else
		puts("Neither");

}

int main()
{
	int Ti,T;
	scanf("%d",&T);
	for(Ti = 1; Ti <= T; Ti++)
	{
		printf("Case #%d: ",Ti);
		solve();
	}
}
