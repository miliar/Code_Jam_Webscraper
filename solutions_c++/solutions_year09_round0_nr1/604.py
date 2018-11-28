#include<iostream>
#include<string.h>
using namespace std;

long l,d,n;
char str[20000];
bool map[17][27];
char ask[5001][17];

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	long i,j,k,v;
	scanf("%ld%ld%ld",&l,&d,&n);
	for(i=1;i<=d;i++){
		scanf("%s",ask[i]);
	}
	for(i=1;i<=n;i++){
		scanf("%s",str);
		memset(map,0,sizeof(map));
		k=0;
		for(j=0;j<strlen(str);j++){
			if(str[j]=='('){
				while(str[++j]!=')'){
					map[k][str[j]-'a']=1;
				}
			}else	map[k][str[j]-'a']=1;
			k++;
		}
		k=0;
		for(j=1;j<=d;j++){
			for(v=0;v<l;v++){
				if(map[v][ask[j][v]-'a']==0)break;
			}
			if(v==l)k++;
		}
		printf("Case #%ld: %ld\n",i,k);
	}
	return 0;
}