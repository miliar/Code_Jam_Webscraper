#include <stdio.h>
#define maxn 50
char s[maxn][maxn];
int n;
int tn,cp;
int ans;
int p(int k){
    int i;
    for (i=n-1;i>=0;i--)
        if (s[k][i]=='1') return i;
    return -1;
}
int main(){
    int i,j,k,l;
    freopen("A.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&tn);
    for (cp=1;cp<=tn;cp++){
        scanf("%d",&n);
        for (i=0;i<n;i++) scanf("%s",&s[i]);
        ans=0;
        for (i=0;i<n;i++)
            if (p(i)>i){
               for (j=i+1;j<n;j++)
                   if (p(j)<=i){
                      ans+=j-i;
                      for (k=j;k>i;k--)
                          for (l=0;l<n;l++) s[k][l]=s[k-1][l];
                      break;
                   }
            }
        printf("Case #%d: %d\n",cp,ans);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
