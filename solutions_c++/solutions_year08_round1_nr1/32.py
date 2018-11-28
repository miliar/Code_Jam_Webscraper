#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

#define rep(i,n) for(i=0;i<(n);i++)
#define foru(i,a,b) for(i=(a);i<=(b);i++)
#define ford(i,a,b) for(i=(a);i>=(b);i--)

long long a[1000],b[1000];
int n;

int main(){
    freopen("input2.in","r",stdin);
    freopen("output.txt","w",stdout);
    int i,j,k,test,cases;
    
    cases=0;
    scanf("%d",&test);
    while (test){
          test--;
          cases++;
          scanf("%d",&n);
          rep(i,n) {
                   scanf("%d",&k);
                   a[i]=k;
          }
          rep(i,n){
                   scanf("%d",&k);
                   b[i]=k;
          }
          sort(a,a+n);
          sort(b,b+n);
          long long ans=0;
          rep(i,n){
              ans+=a[i]*b[n-i-1];
          }
          cout<<"Case #"<<cases<<": "<<ans<<endl;
    }
    return 0;
}
