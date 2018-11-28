#include<cstdio>
#include<cstring>
#define MAX_LEN 105

int t,i,j;
char c;
char code[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main(){
    scanf("%d",&t);
    getchar();
    for(i=1; i<=t; ++i){
	printf("Case #%d: ",i);
	while(c=getchar()){
	    if(c==' '){
		printf(" ");
		continue;
	    }
	    if(c=='\n'){
		printf("\n");
		break;
	    }
	    printf("%c",code[c-'a']);
	}
    }
    return 0;
}



