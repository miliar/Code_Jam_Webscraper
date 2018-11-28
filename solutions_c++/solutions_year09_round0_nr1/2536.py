#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <malloc.h>

char dic[5005][505];
int L, D, N;
char str[100000];
int len;
typedef struct { int st, ed;}Node;
Node node[100000];
int tot;
int ans;
int DFS(int t, int cnt, int num[505]) 
{
	int i, j;
	int rcnt, rnum[505];
	if(cnt == 0) return 0;
	if(t == L)
	{
		ans = ans + cnt;
		return 0;
	}	
	for(i = node[t].st; i <= node[t].ed; i++)
	{
		rcnt = 0;
		for(j = 1; j <= cnt; j++)
			if(str[i] == dic[num[j]][t]) rnum[++rcnt] = num[j];
		DFS(t+1, rcnt, rnum);
	}
	return 0;
}
		
int main()
{
    int i, j;
    int cnt, num[505];
   // freopen("A-small-attempt0.in", "r", stdin);
   // freopen("A-small-attempt0.out", "w", stdout);
    int cases = 1;
    int flag;
    while(scanf("%d %d %d", &L, &D, &N) != EOF)
	{
		for(i = 1; i <= D; i++)
		    scanf("%s", dic[i]); 
        for(i = 1; i <= N; i++)
        {
        	scanf("%s", str);
        	len = strlen(str);    	
        	for(j = 1; j <= D; j++)
        	    num[j] = j;
    	    cnt = D;
    	    tot = 0;
    	    flag = 0;
        	for(j = 0; j < len; j++)
        	{
        		if(flag == 0 && str[j] != '(' && str[j] != ')') 
        		{
        			node[tot].st = j;
        			node[tot++].ed = j;
        		}
        		if(str[j] == '(') 
				{
				    node[tot].st = j+1;
				    flag = 1;
				}
        		if(str[j] == ')') 
				{
				    node[tot++].ed = j-1;
				    flag = 0;
				}
				
        	}
        	ans = 0;
        	if(tot >= L) DFS(0, cnt, num);
        	printf("Case #%d: %d\n", cases++, ans);
        }
	} 
    return 0;
}
