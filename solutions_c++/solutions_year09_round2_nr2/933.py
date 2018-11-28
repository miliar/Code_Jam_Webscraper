#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <cstdlib>
typedef long long LL;
using namespace std;

bool les(char *a,char *b){
	int i;
	for(i=0;a[i];i++){
		if(a[i]>b[i]) return 0;
		if(a[i]<b[i]) return 1;
	}
	return 1;
}

bool spc(char *a){
	int i;
	for(i=1;a[i];i++) if(a[i]!='0') return 0;
	return 1;
}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int ic,i,cas;
	scanf("%d",&cas);
	char str[100];
	char tmp[100];
	for(ic=1;ic<=cas;ic++){
		scanf("%s",str);
		for(i=0;i<=strlen(str);i++) tmp[i]=str[i];
		next_permutation(str,str+strlen(str));
		//printf("%s,%s\n",str,tmp);
		if(les(str,tmp)) {
			if(str[0]=='0'){
				for(i=1;str[i]=='0';i++);
				printf("Case #%d: %c",ic,str[i]);
				str[i]='0';
				printf("%s\n",str);
			}
			else 
				printf("Case #%d: %c%c%s\n",ic,str[0],'0',str+1);
		}
		else
			printf("Case #%d: %s\n",ic,str);
	}
    return 0;
}
