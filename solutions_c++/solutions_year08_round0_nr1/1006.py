#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <map>

using namespace std;

#define rep(i,n) for(i=0;i<(n);i++)
#define foru(i,a,b) for(i=(a);i<=(b);i++)
#define ford(i,a,b) for(i=(a);i>=(b);i--)


map<string,int> name;
string s;
int a[1100];
int f[1100][110],n,m;

int main(){
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int i,j,k,test,cases;
    cin>>test;
    cases=0;
    while (test){
         test--; cases++;
         scanf("%d\n",&n);
         name.clear();
         rep(i,n) {
                  getline(cin,s);
                  name[s]=i+1;
         }
         scanf("%d\n",&m);
         foru(i,1,m){
            getline(cin,s);
            if (name.count(s)) a[i]=name[s];
            else a[i]=0;
         }
         memset(f,60,sizeof(f));
         int infinite=f[0][0];
         
         foru(i,1,n) f[0][i]=0;
         foru(i,0,m-1)
           foru(j,1,n) if (f[i][j]!=infinite)
               foru(k,1,n) if (a[i+1]!=k) {
                   if (k==j) f[i+1][k]=min(f[i+1][k],f[i][j]);
                   else      f[i+1][k]=min(f[i+1][k],f[i][j]+1);
               }
         int ans=infinite;
         foru(i,1,n) ans=min(ans, f[m][i]);
         printf("Case #%d: %d\n",cases,ans);
    }
    return 0;
}
