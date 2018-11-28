#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

int n,m,d;
double a[505][505],si[505][505],sj[505][505],s[505][505];
int ans;

void solve(){
     
     scanf("%d%d%d\n",&n,&m,&d);
     for (int i=1;i<=n;i++) {
         for (int j=1;j<=m;j++) {
             char c;
             scanf("%c",&c);
             a[i][j]=double(c-'0')+1;
         }
         scanf("\n");
     }
     
     for (int i=0;i<=n;i++)
         for (int j=0;j<=m;j++) { 
             s[i][j]=0;
             si[i][j]=0;
             sj[i][j]=0;
         }
         
     for (int i=1;i<=n;i++)
         for (int j=1;j<=m;j++) {
             s[i][j]=s[i-1][j]+s[i][j-1]-s[i-1][j-1]+a[i][j];
             si[i][j]=si[i-1][j]+si[i][j-1]-si[i-1][j-1]+a[i][j]*i;
             sj[i][j]=sj[i-1][j]+sj[i][j-1]-sj[i-1][j-1]+a[i][j]*j;
         }
     
     ans=0;
     for (int i=1;i<=n;i++)
         for (int j=1;j<=m;j++)
             for (int len=3;len<=min(n,m);len++) {
                 if (i+len-1>n||j+len-1>m) continue;
                 double midi=double(i+i+len-1)/double(2);
                 double midj=double(j+j+len-1)/double(2);
                 int ni=i+len-1,nj=j+len-1;
                 double sumi=0,sumj=0,sumw=0;
                 sumi+=si[ni][nj]-si[i-1][nj]-si[ni][j-1]+si[i-1][j-1];
                 sumj+=sj[ni][nj]-sj[i-1][nj]-sj[ni][j-1]+sj[i-1][j-1];
                 sumw+=s[ni][nj]-s[i-1][nj]-s[ni][j-1]+s[i-1][j-1];
                 
                 int ii,jj;
                 ii=i,jj=j;
                 sumi-=a[ii][jj]*ii; sumj-=a[ii][jj]*jj; sumw-=a[ii][jj];
                 ii=i,jj=nj;
                 sumi-=a[ii][jj]*ii; sumj-=a[ii][jj]*jj; sumw-=a[ii][jj];
                 ii=ni,jj=j;
                 sumi-=a[ii][jj]*ii; sumj-=a[ii][jj]*jj; sumw-=a[ii][jj];
                 ii=ni,jj=nj;
                 sumi-=a[ii][jj]*ii; sumj-=a[ii][jj]*jj; sumw-=a[ii][jj];
                 
                 double nowi=sumi/sumw,nowj=sumj/sumw;
                 if ((abs(midi-nowi)<1e-8)&&(abs(midj-nowj)<1e-8)) ans=max(ans,len);
             }
     if (ans==0) printf("IMPOSSIBLE\n");
        else printf("%d\n",ans);
     
}

int main(){
    
    freopen("b.in","r",stdin);
    freopen("b_LL.out","w",stdout);
    
    int test;
    scanf("%d\n",&test);
    for (int tot=1;tot<=test;tot++) {
        printf("Case #%d: ",tot);
        solve();
    }
    
    
    return 0;
}
