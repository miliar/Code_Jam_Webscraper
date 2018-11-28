#include <cstdio>
#include <cstring>

int n,m,ans,len[300];
char s[300][200];

int Go(int n1,int n2) {
    int i;
    for (i = 0; i<len[n2]; i++)
      if (s[n1][i] != s[n2][i]) break;
    if ((i==len[n1] || s[n1][i]=='/') && i==len[n2]) return i;  
    if (i==len[n2] && i!=len[n1] && s[n1][i]!='/') i--;  
    if (i==len[n1] && s[n2][i]!='/' && i!=len[n2]) i--;
    while (s[n2][i] != '/') i--;  
    return i;  
}
int main() {
    int test,tt,i,j,k;
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&test);
    for (tt = 1; tt<=test; tt++) {
        ans = 0; 
        scanf("%d %d",&n,&m);
      //  if (tt == 16) printf("%d %d\n",n,m);
        for (i = 1; i<=n; i++) 
            scanf("%s",s[i]),len[i] = strlen(s[i]);
        for (i = 1; i<=m; i++) {
            scanf("%s",s[++n]);
            len[n] = strlen(s[n]);
            int now = 0;
            for (j = 1; j<n; j++)
              if (Go(j,n)>now) now = Go(j,n);
       //     printf("%d  ",now);  
            for (j=now; j<len[n]; j++) 
              if (s[n][j] == '/') ans++;    
       //     printf("%d\n",ans);    
        }
      //  if (tt == 16)
      //  for (i = 1; i<=n; i++)
       //   printf("%s\n",s[i]);
        printf("Case #%d: %d\n",tt,ans);
    }
}
