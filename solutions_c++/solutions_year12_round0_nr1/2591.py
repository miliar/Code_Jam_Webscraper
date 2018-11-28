#include<stdio.h>
#include<stdlib.h>
#include<string.h>

char ch[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
char s[1000000];

int main(){
    freopen("f:\\in.txt","r",stdin);
    freopen("f:\\out.txt","w",stdout);
    int T,cas=0;
    scanf("%d",&T);
    getchar();
    while(T--){
        cas++;
        gets(s);
        int len=strlen(s);
        for(int i=0;i<len;i++){
            if(s[i]!=' ')
                s[i]=ch[s[i]-'a'];
        }
        printf("Case #%d: %s\n",cas,s);
    }
    return 0;
}
