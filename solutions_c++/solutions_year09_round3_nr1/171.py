#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int tn,cp;
int n;
unsigned long long m;
char s[100];
int a[100];
int t[300];
int main(){
    int i,j;
    freopen("A.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&tn);
    for (cp=1;cp<=tn;cp++){
        scanf("%s",&s);
        n=strlen(s);
        memset(t,-1,sizeof(t));
        int f=0;
        m=1;
        a[0]=1;
        t[s[0]]=1;
        for (i=1;i<n;i++){
            if (t[s[i]]!=-1) a[i]=t[s[i]];else{
               if (f==0) {f=1;t[s[i]]=0;}else t[s[i]]=++m;
               a[i]=t[s[i]];
            }
        }
        m++;
        unsigned long long ans=0,k=1,tmp;
        for (i=n-1;i>=0;i--){
            tmp=a[i];
            ans+=tmp*k;
            k*=m;
        }
        printf("Case #%d: %I64d\n",cp,ans);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
