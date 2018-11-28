#include<stdio.h>
#include<string.h>
#define MAXN 505
struct Combination
{
	char first;
	char second;
	char comb;
}com[MAXN];
struct Opposed
{
	char first;
	char second;
}opp[MAXN];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	char str[MAXN];
	char invoke[MAXN];
	int cn, dn, n, ansn;
	scanf("%d",&T);
	for(int t = 1; t <= T; t++){
		scanf("%d",&cn);
		for(int i = 0; i < cn; i++){
			scanf("%s",str);
			com[i].first = str[0];
			com[i].second = str[1];
			com[i].comb = str[2];
		}
		scanf("%d",&dn);
		for(int i = 0; i < dn; i++){
			scanf("%s",str);
			opp[i].first = str[0];
			opp[i].second = str[1];
		}
		scanf("%d",&n);
		scanf("%s",str);
		ansn = 0;
		for(int i = 0; i < n; i++)
		{
			invoke[ansn++] = str[i];
			int flag = 0;
			if(ansn>=2)
			{
				for(int j = 0; j < cn; j++){
					if(invoke[ansn-1] == com[j].first && invoke[ansn-2] == com[j].second ||
						invoke[ansn-1] == com[j].second && invoke[ansn-2] == com[j].first){
							invoke[ansn-2] = com[j].comb;
							ansn -= 1;
							flag = 1;
							break;
						}
				}
			}
			if(ansn < 2)continue;
			flag = 0;
			for(int k = ansn-2; k >= 0; k--){
				for(int j = 0; j < dn; j++){
					if(invoke[k] == opp[j].first && invoke[ansn-1] == opp[j].second ||
						invoke[k] == opp[j].second && invoke[ansn-1] == opp[j].first){
							ansn = 0;
							flag = 1;
							break;
						}
				}
				if(flag)break;	
			}
		}
		printf("Case #%d: [", t);
		if(ansn > 0)
			printf("%c",invoke[0]);
		for(int i = 1; i < ansn; i++){
			printf(", %c", invoke[i]);
		}
		printf("]\n");
	}
	return 0;
}
