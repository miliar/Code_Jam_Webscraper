#include <cstdio>
#include <iostream>
#define MAXN 50
using namespace std;
const int dx [4]= {0, 1, 1, 1};
const int dy [4]= {1, 0, -1, 1};

char a [MAXN + 1][MAXN + 1], b[MAXN + 1][MAXN + 1];
int n,k;
int test, t;
int redWin, blueWin;

void init()
{
	scanf("%d %d", &n, &k);
	for(int i=0; i<n; i++)
		scanf("%s", a[i]);
}

void print()
{
	printf ("Case #%d: ", test + 1);
	if (redWin && blueWin)
		printf("Both\n");
	else if (redWin)
		printf("Red\n");
	else if (blueWin)
		printf("Blue\n");
	else
		printf("Neither\n");
}

void rotate(int x,int y)
{
	int i;
	for(i=x-1;i>=0;i--)
	{
		b[i+1][y]=b[i][y];
	}
	b[0][y]='.';
}

int check(int x,int y,char ch)
{
	int i,j,d,cnt;
	for(d=0;d<4;d++)
	{
		cnt=0;
		i=x;
		j=y;
		while((i>=0)&&(i<n)&&(j>=0)&&(j<n)&&(b[i][j]==ch))
		{
			i=i+dx[d];
			j=j+dy[d];
			cnt++;
		}
		if(cnt>=k)
		{
			return 1;
		}
	}
	return 0;
}

int kJoin(char ch)
{
	for(int i = 0;i < n;i++)
		for(int j = 0;j < n;j++)
			if ( (b[i][j] == ch) && (check (i, j, ch) == 1))
				return 1;
	return 0;
}

void process()
{
	for (int i = 0;i < n;i++)
		for(int j = 0; j < n; j++)
			b[j][n - 1 - i]=a[i][j];

	for (int j = 0; j < n; j++)
		for (int p = 0; p < n; p++)
			for (int i = n - 1; i >= 0; i--)
				if (b[i][j] == '.')
				{
					rotate(i, j);
					break;
				}
	redWin = kJoin('R');
	blueWin = kJoin('B');
}

int main()
{
	freopen ( "A-large.in", "r", stdin);
	freopen ( "A-large.out", "w", stdout);
	scanf ( "%d", &t);
	for(test = 0;test < t; test++)
	{
		init();
		process();
		print();
	}
	return 0;
}
