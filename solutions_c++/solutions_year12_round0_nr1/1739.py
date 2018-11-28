#include<stdio.h>
#include<string.h>
int g[30];
char s[3][200],t[3][200];
char str[200];
int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int i,j,ca,cc=0;
    memset(g,-1,sizeof(g));
    strcpy(s[0],"ejp mysljylc kd kxveddknmc re jsicpdrysi");
    strcpy(s[1],"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
    strcpy(s[2],"de kr kd eoya kw aej tysr re ujdr lkgc jv");
    strcpy(t[0],"our language is impossible to understand");
    strcpy(t[1],"there are twenty six factorial possibilities");
    strcpy(t[2],"so it is okay if you want to just give up");  
    for (i=0;i<3;i++)
        for (j=0;j<strlen(s[i]);j++)
            if (s[i][j]!=' ') g[s[i][j]-'a']=t[i][j]-'a';
    g[16]=25;
    g[25]=16;
    scanf("%d",&ca);
    while (ca--){
        cc++;
        printf("Case #%d: ",cc);
        scanf("\n%[^\n]s",str);
        for (i=0;i<strlen(str);i++){
            if (str[i]!=' ') printf("%c",(char)(g[str[i]-'a']+'a'));
            else printf(" ");
        }
        printf("\n");
    }
    return 0;
}
