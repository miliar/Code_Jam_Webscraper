#include <cstdio>
#include <cstring>

const char s[] = "yhesocvxduiglbkrztnwjpfmaq";
char a[100+10];

int main(){
    int noc;
    scanf("%d",&noc);
    fgets(a,100+10,stdin);
    for (int i=1;i<=noc;++i){
        printf("Case #%d: ",i);
        fgets(a,100+10,stdin);
        int len = strlen(a);
        for (int j=0;j<len;++j){
            if (a[j]=='\n'){
                continue;
            }
            if (a[j]>='a'&&a[j]<='z'){
                printf("%c",s[a[j]-'a']);
            } else {
                printf("%c",a[j]);
            }
        }
        printf("\n");
    }
    return 0;
}
