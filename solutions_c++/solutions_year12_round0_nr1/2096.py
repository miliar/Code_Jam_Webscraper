#include<stdio.h>

char line[1010];
char replace[]={'y','h','e','s','o','c','v','x','d','u','i','g','l',
                'b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main(){
    int N;
    scanf("%d",&N);
    gets(line);
    for(int i=1;i<=N;i++){
        gets(line);
        printf("Case #%d: ",i);
        for(int j=0;line[j];j++)
            if(line[j]!=' ') printf("%c",replace[line[j]-'a']);
            else printf(" ");
        printf("\n");
    }
    return 0;
}
