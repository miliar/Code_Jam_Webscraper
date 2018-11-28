#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;
int th[350][350],tw[350][350];
int main(){
	int i,j,cas,n;
	int cou=1;
	char str[400];
	char ans[400];
	freopen("C:\\Users\\lenovo\\Desktop\\B-small-attempt3.in","r",stdin);
    freopen("C:\\Users\\lenovo\\Desktop\\stdout.txt","w",stdout);
	scanf("%d",&cas);
	while(cas--){
		memset(tw,0,sizeof(tw));
		memset(th,0,sizeof(th));
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%s",str);
			th[str[0]][str[1]]=th[str[1]][str[0]]=str[2];
		}
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%s",str);
			tw[str[0]][str[1]]=tw[str[1]][str[0]]=1;
		}
		scanf("%d%s",&n,str);
		int len=0;
		for(i=0;i<n;i++){
			ans[len++]=str[i];
			while(len-2>=0){
				if(th[ans[len-1]][ans[len-2]]!=0){
					ans[len-2]=th[ans[len-1]][ans[len-2]];
					len--;
				}
				else break;
			}
			for(j=0;j<len-1;j++){
				if(tw[ans[len-1]][ans[j]]==1){
					len=0;
				}
			}
		}
		printf("Case #%d: [",cou++);
		for (i = 0; i < len; i++)
            if (i != len-1) printf("%c, ", ans[i]);
            else printf("%c", ans[i]);
        printf("]\n");
	}
	return 0;
}
