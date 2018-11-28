#include "stdio.h"
#include "string.h"

const char became[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k',
                'r','z','t','n','w','j','p','f','m','a','q'};

int T,total,i;
char st[110];
int main(){
    freopen("a.txt","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&T);
    gets(st);
    total;
    while(T-->0){
        total++;
        gets(st);
        for(i = 0;i <strlen(st);i++)
            if(st[i]>='a' && st[i] <= 'z'){
                st[i] = became[st[i]-'a'];
            }
        printf("Case #%d: ",total);
        for(i = 0;i< strlen(st);i++)printf("%c",st[i]);
        printf("\n");
    }
    return 0;
}
