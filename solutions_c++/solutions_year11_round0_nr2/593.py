#include<stdio.h>
#include<math.h>
#include<vector>
#include<string.h>
#include<iostream>
using namespace std;

int maze[256][256];
int maze1[256][256];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("1.out","w",stdout);
	
	int t;
	int c,d;
	int n;
	char s[110];
	char ans[110];
	int len;
	int cas = 1;

	scanf("%d",&t);
	while(t--){
		memset(maze,-1,sizeof(maze));
		memset(maze1,-1,sizeof(maze1));

		len = 0;
		scanf("%d",&c);
		while(c--){
			scanf("%s",&s);
			maze[s[0]][s[1]] = maze[s[1]][s[0]] = s[2];
		}
		scanf("%d",&d);
		while(d--){
			scanf("%s",&s);
			maze1[s[0]][s[1]] = maze1[s[1]][s[0]] = -2;
		}
		scanf("%d",&n);
		scanf("%s",&s);
		ans[0] = s[0];
		len ++;
		for(int i = 1; i < n; i ++){
			//ans[len] = '\0';
			//puts(ans);
			ans[len++] = s[i];
			while(len > 1 && maze[ans[len-1]][ans[len-2]] >= 0)
			{
				ans[len-2] = maze[ans[len-1]][ans[len-2]];
				len --;
			}
			for(int j = len -2; j >= 0; j --){
				if(maze1[ans[len-1]][ans[j]] == -1) continue;
				if(maze1[ans[len-1]][ans[j]] == -2)
				{	len = 0;
					break;
				}
			}
		}
		printf("Case #%d: [",cas++);
		for(int i = 0 ; i < len; i ++){
			printf("%c",ans[i]);
			if(i != len-1) printf(", ");
		}
		printf("]\n");
	}
	return 0;
	
}