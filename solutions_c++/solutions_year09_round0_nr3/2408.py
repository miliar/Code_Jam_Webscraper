#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <malloc.h>
#define N 1001

char dic[20] = {"welcome to code jam"};
char str[1000]; 
int len;
int cnt;
int DFS(int pos, int t)
{
	int i;
	if(t == 19)
	{
		cnt++;
		return 0;
	}
	for(i = pos; i < len; i++)
	{
		if(str[i] == dic[t])
		{
			DFS(i+1, t+1);
		}
	}
	return 0;
}
	
int main()
{
    int i, j;
    int T;
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out","w", stdout);    
    scanf("%d", &T);
    getchar();
    int cases = 1;
    int n;
    int tmp;
    int num[10], tot;
    while(T--)
    {
    	gets(str);
    	len = strlen(str);
    	cnt = 0;
    	DFS(0, 0);
    	printf("Case #%d: ", cases++);
    	n = 4;
    	while(n--)
    	{
    		num[n] = cnt % 10;
    		cnt = cnt/10;
    	}
    	for(i = 0; i < 4; i++)
    	    printf("%d", num[i]);
    	printf("\n");
    	
    }
    	
    	


    return 0;
}
