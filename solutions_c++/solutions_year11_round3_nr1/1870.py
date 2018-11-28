#include<stdio.h>
#define MAX 51

char arr[MAX][MAX];

void solve()
{
	int count = 0;
	int r, c, ic = 0;
	scanf("%d%d", &r, &c);
	
	while(ic < r*c)
	{
		char ch;
		ch=getchar();
		if('#' == ch || '.' == ch )
		{
			arr[ic/c][ic%c] = ch;
			ic++;
			if('#' == ch) count++;
		}
	}
	if(0 != count%4)
	{
		printf("Impossible\n");
		return;
	}
	for(int i = 0 ; i < r; i++)
	{
		for(int j = 0 ; j < c; j++)
		{
			if('#'==arr[i][j])
			{
				if(i+1 < r && j+1 <c 
				&& '#'== arr[i+1][j]
				&& '#'== arr[i][j+1]
				&& '#'== arr[i+1][j+1])
				{
					arr[i][j]='/';
					arr[i][j+1] = 92;
					arr[i+1][j] = 92;
					arr[i+1][j+1] = '/';
					count -= 4;	
				}
			}
		}
	}
	if(0 != count)
	{
		printf("Impossible\n");
		return;
	}
	for(int i = 0 ; i < r; i++)
	{
		for(int j = 0 ; j < c; j++)
		{
			putchar(arr[i][j]);
		}
		putchar('\n');
	}
		
}

int main(int argc, char **argv)
{
	int ncase;

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	//freopen("A-small.in", "r", stdin);
	//freopen("A-small.out", "w", stdout);
	
	scanf("%d", &ncase);
	for(int icase = 0; icase < ncase; icase++)
	{
		printf("Case #%d:\n", icase+1);
	 	solve();
	}	
		
	return 0;
}
