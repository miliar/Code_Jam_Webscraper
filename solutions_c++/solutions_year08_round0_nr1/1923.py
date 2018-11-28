#include<stdio.h>
#include<stdlib.h>
#include<string.h>
char used[121];
int q,s;
int check(){
	int i,num = 0;
	for(i=0;i<s;i++){
		if(used[i] == 0){
			num++;
		}
	}
	if(num == 1)
		return 1;
	return 0;
}
int main(){
	int ca,te,i,j;
	char name[121][121];
	int cm[1024],ans;
	char str[121];
	scanf("%d",&ca);
	for(te =0;te<ca;te++){
		scanf("%d ",&s);
		for(i=0;i<s;i++){
			gets(name[i]);
		}
		scanf("%d ",&q);
		for(i=0;i<q;i++){
			gets(str);
			for(j=0;j<s;j++){
				if(strcmp(str,name[j]) == 0){
					cm[i] = j;
					break;
				}
			}
		}
		ans = 0;
		for(i=0;i<121;i++)
			used[i] = 0;
		for(i=0;i<q;i++){
			if(check() == 1 && used[cm[i]] == 0){
				for(j=0;j<121;j++)
					used[j] = 0;
				ans++;
			}
			used[cm[i]] = 1;
		}
		printf("Case #%d: %d\n",te+1,ans);
	}
	return 0;
}
