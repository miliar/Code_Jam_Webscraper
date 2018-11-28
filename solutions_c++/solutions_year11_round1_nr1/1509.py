#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>

using namespace std;
#define sz(a) (a).size()
#define all(a) (a).begin(),(a).end()
#define REP(i,n) for(int i=0;i<(n);++i)
int main(){

    freopen("A-small-attempt2.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,n,a,b;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        scanf("%d%d%d",&n,&a,&b);
        bool ans=true;
        if ( b==100 && a!=100)
            ans=false;
        if(b==0 && a!=0)
            ans=false;
        int x=a,y=100;
        for(int j=2;j<=x;j++){
            while(x && x%j==0 && y%j==0){
                x/=j;
                y/=j;
            }
        }
        if(a==0)
            y=1;
        if(y>n)
            ans=false;
        if(ans==false)
            printf("Case #%d: Broken\n",i);
        else
            printf("Case #%d: Possible\n",i);
       }
       return 0;
}
