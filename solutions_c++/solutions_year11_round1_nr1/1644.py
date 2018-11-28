#include<iostream>
#include<string>
#include<cstring>
#include<vector>
#include<cstdio>
#include<queue>
#include<deque>
using namespace std;

//A

long long a,b,c;

int main(void) {
    freopen("in.in","r",stdin);
    freopen("out2.out","w",stdout);
    int n;cin>>n; //n=2;
    for(int i=1;i<=n;i++) {
            cin>>a>>b>>c;
            printf("Case #%d: ",i);
            if( b==c ) {
                puts("Possible");
            }
            else {
                 if( c==0 || c==100 ) {
                     puts("Broken");
                 }
                 else {
                      if( b==0 ) {
                          puts("Possible");
                          continue;
                      }
                      long long l=__gcd( b, 100LL);
                      long long bb=100LL/l;
                      if( bb<=a ) {
                          puts("Possible");
                      }
                      else puts("Broken");
                 }
            }
    }
    return 0;
}
