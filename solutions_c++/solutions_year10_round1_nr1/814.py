#include<cstdio>
int t,n,k,red,blue,ok;
char r[55][55],c[55][55],tmp;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A_large_output.out","w",stdout);
    scanf("%d",&t);
    for (int tt=1; tt<=t; ++tt){
        scanf("%d%d",&n,&k);
        for (int i=n-1; i>=0; i--){
            scanf("%*c");
            for (int j=n-1; j>=0; j--)
                scanf("%c",&c[j][i]);    
        }
        for (int i=0; i<n; i++)
            for (int j=0; j<n; j++)
                if (c[i][j]!='.'){
                   int u=i;
                   while (u-1>=0&&c[u-1][j]=='.')
                         tmp=c[u][j],c[u][j]=c[u-1][j],c[u-1][j]=tmp,--u;
                }
        red=blue=0;
        for (int i=0; i<n; i++)
            for (int j=0; j<n; j++){
                if (i+k-1<n){
                   ok=1;
                   for (int u=i; u<i+k; u++)
                       if (c[u][j]!=c[i][j]){
                          ok=0; break;                      
                       }
                   if (ok&&c[i][j]=='R') red=1;
                   else if (ok&&c[i][j]=='B') blue=1;
                }    
                if (j+k-1<n){
                   ok=1;
                   for (int u=j; u<j+k; u++)
                       if (c[i][u]!=c[i][j]){
                          ok=0; break;                      
                       }
                   if (ok&&c[i][j]=='R') red=1;
                   else if (ok&&c[i][j]=='B') blue=1;             
                }
                if (i+k-1<n&&j+k-1<n){
                   ok=1;
                   for (int u=1; u<k; u++){
                       if (c[i+u][j+u]!=c[i][j]){
                          ok=0; break;                          
                       }    
                   }                  
                   if (ok&&c[i][j]=='R') red=1;
                   else if (ok&&c[i][j]=='B') blue=1;                                    
                }
                if (i+k-1<n&&j-k+1>=0){
                   ok=1;
                   for (int u=1; u<k; u++)
                       if (c[i+u][j-u]!=c[i][j]){
                          ok=0; break;                          
                       }
                   if (ok&&c[i][j]=='R') red=1;
                   else if (ok&&c[i][j]=='B') blue=1;                                         
                }
            }
        printf("Case #%d: ",tt);
        if (red&&blue) printf("Both\n");
        else if (red) printf("Red\n");
        else if (blue) printf("Blue\n");
        else printf("Neither\n");
    }
    return 0;    
}
