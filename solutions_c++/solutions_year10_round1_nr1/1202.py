#include <stdio.h>

int N, K;
char b1[55][55], b2[55][55];

void work()
{
	scanf("%d%d", &N, &K);
	int i, j, k, l, m;
	for(i = 0; i < N; i ++)
	{	
		scanf("%s", b1[i]);	
		for(j = 0; j < N; j ++)
			b2[i][j] = '.';		
	}	
	
	for(i = N - 1; i >= 0; i --)
	{
		k = N - 1;
		for(j = N - 1; j >= 0; j --)
		{
			if(b1[i][j] != '.')
			{
				b2[k--][N - 1 - i] = b1[i][j];	
			}
		}	
	}
	
//	for(i = 0; i < N; i ++)
//	{
//		for(j = 0; j < N; j ++)
//		{
//			printf("%c", b2[i][j]);	
//		}
//		printf("\n");
//	}
	

	int cnt = 0;

	bool bflag, rflag;
	bflag = false;
	rflag = false;

	for(i = 0; i < N; i ++)
	{
		k = 0; 
		l = 0;
		for(j = 0; j < N; j ++)
		{
			if(!bflag)
			{
				if(b2[i][j] == 'B')	
				{
					k ++;
					if(k == K)	
					{
						bflag = true;
						break;	
					}
				}
				else	k = 0;
			}			
			if(!rflag)
			{
				if(b2[i][j] == 'R')	
				{
					l ++;
					if(l == K)	
					{
						rflag = true;
						break;	
					}
				}
				else	l = 0;	
			}
		}
		if(bflag && rflag)
			break;
	}
	
	
	for(i = 0; i < N; i ++)
	{
		
		for(j = 0; j < N; j ++)
		{
			k = 0; 
			l = 0;
			for(m = 0; m < N; m ++)
			{
				int a, b;
				a = i + m;
				b = j + m;
				
				if(a < 0 || a >= N || b < 0 || b >= N)
					break;
				
				if(!bflag)
				{
					if(b2[a][b] == 'B')	
					{
						k ++;
						if(k == K)	
						{
							bflag = true;
							break;	
						}
					}
					else	k = 0;
				}			
				if(!rflag)
				{
					if(b2[a][b] == 'R')	
					{
						l ++;
						if(l == K)	
						{
							rflag = true;
							break;	
						}
					}
					else	l = 0;	
				}
			}
			if(bflag && rflag)
				break;
		}
		if(bflag && rflag)
				break;
	}
	
	
	for(i = 0; i < N; i ++)
	{
		k = 0; 
		l = 0;
		for(j = 0; j < N; j ++)
		{
			if(!bflag)
			{
				if(b2[j][i] == 'B')	
				{
					k ++;
					if(k == K)	
					{
						bflag = true;
						break;	
					}
				}
				else	k = 0;
			}			
			if(!rflag)
			{
				if(b2[j][i] == 'R')	
				{
					l ++;
					if(l == K)	
					{
						rflag = true;
						break;	
					}
				}
				else	l = 0;	
			}
		}
		if(bflag && rflag)
			break;
	}
	
	for(i = 0; i < N; i ++)
	{
		
		for(j = 0; j < N; j ++)
		{
			k = 0; 
			l = 0;
			for(m = 0; m < N; m ++)
			{
				int a, b;
				a = i - m;
				b = j + m;
				
				if(a < 0 || a >= N || b < 0 || b >= N)
					break;
				
				if(!bflag)
				{
					if(b2[a][b] == 'B')	
					{
						k ++;
						if(k == K)	
						{
							bflag = true;
							break;	
						}
					}
					else	k = 0;
				}			
				if(!rflag)
				{
					if(b2[a][b] == 'R')	
					{
						l ++;
						if(l == K)	
						{
							rflag = true;
							break;	
						}
					}
					else	l = 0;	
				}
			}
			if(bflag && rflag)
				break;
		}
		if(bflag && rflag)
				break;
	}
	
	if(rflag && bflag)
	{
		printf("Both\n");
		return;
	}
	
	if(rflag)
	{
		printf("Red\n")	;
		return;
	}
		
	if(bflag)
	{
		printf("Blue\n");
		return;
	}
	
	printf("Neither\n");
	return;
}





int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int kase;
	int t;
	scanf("%d", &t);
	for(kase = 1; kase <= t; kase ++)
	{
		printf("Case #%d: ", kase);
		work();
	}	

	return 0;	
	
}
