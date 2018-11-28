#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main(){
	int i;
	char inp[2000]="zqejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
	char out[2000]="qzour language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
	int change[26];
	for(i=0;i<26;i++){
		change[i]=i;
	}
		int l=strlen(inp);
		int j=0;
		int n,m;
		for(j=0;j<l;j++){
			n=inp[j]-97;
			m=out[j]-97;
			if(m>=0&&n>=0&&m<=25&&n<=25){
				change[n]=m;
			}
		}
//	for(i=0;i<26;i++){
//		printf("%d--->%d\n",i,change[i]);
//	}
	int t;
	char str[101];
	scanf("%d",&t);
		getchar();
	for(i=0;i<t;i++){
		scanf("%[^\n]",str);
		getchar();
		l=strlen(str);
		printf("Case #%d: ",i+1);
		for(j=0;j<l;j++){
			if(str[j]-97>=0&&str[j]-97<=25)
				str[j]=change[str[j]-97]+97;
			printf("%c",str[j]);
		}
	printf("\n");
		
	}
	return 0;
}
