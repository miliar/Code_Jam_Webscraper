#include<cstdio>
using namespace std;
int t,i,k;
char s[1000],c='0',code[30]={' ','y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d\n",&t);
	for(i=1;i<=t;++i){
		while(c!='\n'){
			scanf("%c",&c);
			if(feof(stdin)){
				break;
			}
			if(c!=' ' && c!='\n'){
			s[++k]=code[int(c)-96];
			}
			else{
				s[++k]=c;
			}
		}
		printf("Case #%d: ",i);
		for(int j=1;j<=k;++j){
			printf("%c",s[j]);
		}
		k=0;
		c='0';
	}
	return 0;
}
