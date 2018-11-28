#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#define MAX_N 2000000

//int used[MAX_N+1];

int main(void){
	int T,t;
	scanf("%d\n",&T);
	for (t=1;t<=T;t++){
		int A,B;
		scanf("%d %d\n",&A,&B);
		int ret=0;
		//memset(used,0,sizeof(used));
		int i;
		for (i=A;i<=B;i++){
			//fprintf(stderr,"%d:\n",i);
			char i_str_org[100],i_str[100];
			int i_str_len;
			/*if (used[i])continue;
			used[i]=1;*/
			sprintf(i_str_org,"%d",i);
			i_str_len=strlen(i_str_org);
			strcpy(i_str,i_str_org);
			while (1){
				//1つずらす
				char c0=i_str[i_str_len-1];
				memmove(&i_str[1],&i_str[0],sizeof(char)*(i_str_len-1));
				i_str[0]=c0;
				//fprintf(stderr,"%s\n",i_str);
				//抜ける条件
				if (strcmp(i_str,i_str_org)==0)break;
				//先頭が0なら無視
				if (i_str[0]=='0')continue;
				//数字に変換
				int i2=atoi(i_str);
				//assert(used[i2]==0);
				if (A<=i2 && i2<=B){
					//used[i2]=1;
					ret++;
				}
			}
		}
		assert(ret%2==0);
		printf("Case #%d: %d\n",t,ret/2);
	}
	return 0;
}
