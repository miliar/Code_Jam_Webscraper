#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<string>
using namespace std;

char str[300];
char dict[300][300];
char cl[300][300];
int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;++t){
		memset(dict,-1,sizeof(dict));
		memset(cl,-1,sizeof(cl));
		char ans[300],len=0;
		int k;
		scanf("%d",&k);
		while(k--){
			scanf("%s",str);
			dict[str[0]][str[1]]=str[2];
			dict[str[1]][str[0]]=str[2];
		}
		scanf("%d",&k);
		while(k--){
			scanf("%s",str);
			cl[str[0]][str[1]]=1;
			cl[str[1]][str[0]]=1;
		}
		scanf("%d",&k);
		scanf("%s",str);
		ans[len]=str[0];
		for(int i=1;str[i];++i){
			char c=ans[len];
			char s=dict[c][str[i]];
			if(s>0){
				ans[len]=s;
			}else{
				int tag=0;
				for(int j=0;j<=len;++j){
					if(cl[ans[j]][str[i]]==1){
						len=-1;
						tag=1;
						break;
					}
				}
				if(tag==0)ans[++len]=str[i];
			}
		}
		printf("Case #%d: ",t);
		printf("[");
		for(int i=0;i<=len;++i){
			if(i)printf(", ");
			printf("%c",ans[i]);
		}
		printf("]\n");
	}
	return 0;
}
