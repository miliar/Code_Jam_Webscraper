#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

int n, m;
int board[600][600];
int flag[600][600];
int num[600];

bool Go(int a, int b, int len)
{
	int i, j;
	int k = board[a][b];
	for(i = a; i < a + len; i ++)
	{
		for(j = b; j < b + len; j ++)
		{
			if(flag[i][j] != 0)	return false;
			if(i == a && j == b)	continue;
			if( j == b)
			{
				if(board[i][j] == board[i-1][j])	return false;	
			}
			else
			{
				if(board[i][j] == board[i][j-1])	return false;	
			}				
		}	
	}
	
	for(i = a; i < a + len; i ++)
	{
		for(j = b; j < b + len; j ++)
		{
			flag[i][j] = len;			
		}	
	}	
	num[len] ++;
	return true;
}



void Check(int len)
{
	int i, j;
	for(i = 0; i <= m - len; i ++)
	{
		for(j = 0; j <= n - len; j ++)
		{
			Go(i, j, len);
		}		
	}	
	
}

void work()
{
	scanf("%d %d", &m, &n);
	int i, j;
	char str[600];
	memset(board, 0, sizeof(board));
	memset(flag, 0, sizeof(flag));
	memset(num, 0, sizeof(num));
	for(i = 0; i < m; i ++)
	{
		scanf("%s", str);
		for(j = 0; j < n/4; j ++)
		{
			if(str[j] >= '0' && str[j] <= '9')	str[j] -= '0';
			if(str[j] >= 'A' && str[j] <= 'F')	str[j] = str[j] - 'A' + 10;
			
			if(str[j] >= 8)
			{
				board[i][j * 4] = 1;
				str[j] -= 8;	
			}	
			
			if(str[j] >= 4)
			{
				board[i][j * 4 + 1] = 1;
				str[j] -= 4;	
			}
			
			if(str[j] >= 2)
			{
				board[i][j * 4 + 2] = 1;
				str[j] -= 2;	
			}
			
			if(str[j] >= 1)
			{
				board[i][j * 4 + 3] = 1;
				str[j] -= 1;	
			}		
		}		
	}
//	for(i = 0; i < m; i ++)
//	{
//		for(j = 0; j < n; j ++)
//		{
//			printf("%d ", board[i][j])	;
//		}	
//		printf("\n\n\n\n");
//	}
	
	int st = m > n ? n : m;
	
	while(st)
	{
		Check(st--);	
	}	
	
	
//	for(i = 0; i < m; i ++)
//	{
//		for(j = 0; j < n; j ++)
//		{
//			printf("%d ", flag[i][j])	;
//		}	
//		printf("\n");
//	}
	
	
	st = m > n ? n : m;
	int cnt = 0;
	for(i = 0; i <= st; i ++)
	{
		if(num[i] != 0)
			cnt ++;
	}
	
//	scanf("%d", &a);
	printf("%d\n", cnt);
	for(i = st; i >= 0; i --)
	{
		if(num[i] != 0)
			printf("%d %d\n", i, num[i]);
	}	
}


int main()
{
//	freopen("C.txt","r",stdin);
	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
//	freopen("C-small-attempt1.in","r",stdin);freopen("C-small-attempt1.out","w",stdout);
//	freopen("C-small-attempt2.in","r",stdin);freopen("C-small-attempt2.out","w",stdout);
//	freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);


	int kase;
	int t;
	scanf("%d", &t);
	for(kase = 1; kase <= t; kase ++)
	{
		printf("Case #%d: ", kase);
		work();
	}	
//while(1);
	return 0;
	
}
