#include<cstdio>

int t;
char map[27]="yhesocvxduiglbkrztnwjpfmaq";
char buf[1000];

int main(){
    int i,j;
    scanf("%d\n",&t);
    for(int lt=1;lt<=t;lt++){
        gets(buf);
        for(i=0;buf[i];i++)
            if(buf[i]!=' ')
                buf[i]=map[buf[i]-'a'];
        printf("Case #%d: %s\n",lt,buf);
    }
    return 0;
}
