#include <stdio.h>
#include <string.h>

typedef __int64 big;

char str[100];

int hash[300];

bool flag[100];

int base[100];
int top;

int main()
{
		freopen("A-large.in","r",stdin);
		freopen("out.txt","w",stdout);
	
	int T;
	int C;
	int i;
	scanf("%d ",&T);
	for (C = 1; C <= T; C ++) {
		
		top = 0;
		
		printf("Case #%d: ",C);
		
		memset(hash,-1,sizeof(hash));
		
		gets(str);
		
		memset(flag,0,sizeof(flag));
		
		int len = strlen(str);
		int num = 0;
		for (i = 0; i < len; i ++) {
			if (i == 0) {
				base[top ++] = 1;
				hash[str[i]] = 1;
				flag[1] = true;
			} else {
				
				if (hash[str[i]] != -1) {
					base[top ++] = hash[str[i]];
				} else {
					
					base[top ++] = num;
					hash[str[i]] = num;
					num ++;
				}
				
				flag[num] = true;
				
				//	num ++;
				if (num == 1) num ++;
			}
		}
		big bb = 1;
		big ans = 0;

		if (num == 0) num =2 ;
		
		for (i = top - 1; i >= 0; i --) {
			ans = ans + base[i] * bb;
			bb = bb * num;
		}
		printf("%I64d\n",ans);
		
		
		
		
		
	}
	
	
	
	return 0;
}
