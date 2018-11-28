#include<iostream>
#include<algorithm>
#include<cstring>

using namespace std;

int tc;
char str[70];
int len,cnt,zr;
int check[150],no[150];
__int64 ans,base;
int main(){
	int i,j,k;
	FILE *in=fopen("in.txt","r");
	FILE *out=fopen("out.txt","w");
	fscanf(in,"%d",&tc);
	for(int tcc=1;tcc<=tc;tcc++){
		memset(check,0,sizeof(check));
		memset(no,0,sizeof(no));
		fscanf(in,"%s",&str);
		len=strlen(str);
		cnt=0;
		for(i=0;i<len;i++){
			if (check[str[i]]==0){
				cnt++;
				check[str[i]]=i+1;
			}
		}
		if (cnt==1) cnt=2;
		base = cnt;
		zr=0;
		cnt=0;
		ans=0;
		for(i=0;i<len;i++){
			if (ans*base < ans) printf("eR!");
			ans*=base;
			if (check[str[i]]==i+1){
				if (i!=0 && zr==0){
					zr=1;
					no[str[i]]=0;
				}else{
					no[str[i]]=++cnt;
				}
			}
//			printf("%d",no[str[i]]);
			ans+=no[str[i]];
		}
//		printf("\n");
		fprintf(out,"Case #%d: %I64d\n",tcc,ans);
	}
	return 0;
}