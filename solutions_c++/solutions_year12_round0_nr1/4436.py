#include<iostream>
#include<cstdio>
using namespace std;
int t,i;
char c,m[27]="yhesocvxduiglbkrztnwjpfmaq";
int main(){
    freopen("u1.in","r",stdin);
    freopen("u1.out","w",stdout);
    scanf("%d\n",&t);
    for(i=1;i<=t;i++){
        printf("Case #%d: ",i);
        while(scanf("%c",&c)!=EOF&&c!='\n'){
            if(c>='a'&&c<='z'){
                printf("%c",m[c-'a']);
            }
            else printf("%c",c);
        }
        printf("\n");
    }
    return 0;
}
