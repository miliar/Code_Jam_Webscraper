#include <cstdio>
#include <cstring>

char m[30];
char sss[]="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
char cov[]="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
char s[200];
int T;

int main(){
    memset(m,0,sizeof m);
    int l=strlen(sss);
    for (int i=0;i<l;++i)
        if (sss[i]!=' ')
            m[sss[i]-'a']=cov[i];
    m[25]='q';
    m['q'-'a']='z';
    scanf("%d",&T);
    gets(s);
    for (int i=1;i<=T;++i){
        printf("Case #%d: ",i);
        gets(s);
        int l=strlen(s);
        for (int j=0;j<l;++j){
            if (s[j]!=' ')
                s[j]=m[s[j]-'a'];
            printf("%c",s[j]);
        }
        printf("\n");
    }
}
