#include <string> 
#include <vector> 
#include <map> 
#include <utility> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <queue> 
#include <stack> 
#include <set> 
#include <sstream> 
#include <algorithm> 
#include <iostream> 
#include <iomanip> 
using namespace std; 
  
#define INF 0x3f3f3f3f
#define ALL(v) v.begin(),v.end() 
typedef pair<int,int> pii; 

pii chick[55];

int main(){
    int test;
    scanf("%d",&test);
    for(int tt=1;tt<=test;tt++){
        printf("Case #%d: ",tt);
        int n,k,b,t;
        scanf("%d %d %d %d",&n,&k,&b,&t);
        
        for(int i=0;i<n;i++) scanf("%d",&chick[i].first);
        for(int i=0;i<n;i++) scanf("%d",&chick[i].second);
        
        reverse(chick,chick+n);
        
        int sw=0,res=0;
        for(int i=0;i<n&&k>0;i++){
            double tt=double(b-chick[i].first)/double(chick[i].second);
            if(tt>t) sw++;
            else {
                res+=sw;
                k--;
            }
        }
        
        if(k==0)       
            printf("%d\n",res);
        else 
            printf("IMPOSSIBLE\n");
    }
    return 0;
}
