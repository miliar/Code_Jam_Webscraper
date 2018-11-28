#include <stdio.h>

int main(){
    int n,caso=1;
    char s[102];
    char s1[102];
    char hash[]={121,104,101,115,111,99,118,120,100,117,105,103,108,98,107,114,122,116,110,119,106,112,102,109,97,113};
    scanf("%d\n",&n);
    while(n--){
        printf("Case #%d: ",caso++);
        gets(s);
        int i=0;
        while('\0'!=s[i]){
            printf("%c",s[i]!=' '?hash[s[i]-'a']:' ');
            i++;
        }
        printf("\n");
    }
}
