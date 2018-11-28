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

int main(){
    int test;
    scanf("%d",&test);
    
    for(int tt=1;tt<=test;tt++){
        printf("Case #%d: ",tt);
        
        long long n,pd,pg;
        scanf("%lld %lld %lld",&n,&pd,&pg);
        bool pos=false;
        if(pg==0&&pd==0) {pos=true; goto sal;}
        if(pg==0) goto sal;
        
        for(long long x=1;x<=n&&x<=105;x++)
            if((((x*pd))%100==0)){
                if(pg==100){
                    if(x==n){
                        if(pd==100){
                            pos=true;
                            break;
                        }
                    }
                }else{
                    pos=true;
                    break;
                }
            }
sal:
        if(pos) printf("Possible");
        else printf("Broken");
        printf("\n");
    }

    return 0;
}
