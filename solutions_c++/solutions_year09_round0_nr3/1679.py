#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define maxn 500+5
#define q 10000
char s[19]={'w','e','l','c','o','m','e',' ','t','o',' ','c','o','d','e',' ','j','a','m'};
char st[maxn],c;
int f[maxn][19];
int tn,l;
int n,ans;
int main(){
    int i,j,k;
    freopen("C-large.in","r",stdin);
    freopen("c.out","w",stdout);
    scanf("%d",&tn);
    scanf("%c",&c);
    for (l=1;l<=tn;l++){
        n=0;
        while (scanf("%c",&c),c!='\n'){
              st[n++]=c;
        }
        memset(f,0,sizeof(f));
        for (i=0;i<n;i++)
            if (st[i]==s[0]) f[i][0]=1;
        for (j=1;j<19;j++){
            k=0;
            for (i=0;i<n;i++){
                if (st[i]==s[j]) f[i][j]=k;
                k+=f[i][j-1];
                k%=q;
            }
        }
        ans=0;
        for (i=0;i<n;i++) ans+=f[i][18],ans%=q;
        printf("Case #%d: ",l);
        if (ans<1000) printf("0");
        if (ans<100) printf("0");
        if (ans<10) printf("0");
        printf("%d\n",ans);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
