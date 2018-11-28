#include<iostream>
#include<cstdio>
using namespace std;
char a[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
char s[200];
int main(){
	//freopen("A-small-attempt2.in","r",stdin);
	//freopen("out.txt","w",stdout);
	int T,i;
	scanf("%d",&T);
	getchar();
	for(i=1;i<=T;i++){
		gets(s);
        printf("Case #%d: ",i);
		int j=0;
		while(s[j]){
			if(s[j]==' '){
				j++;
				printf(" ");
				continue;
			}
			printf("%c",a[s[j]-'a']);
			j++;
		}
		printf("\n");
	}
	return 0;
}
    	


