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
typedef pair<char,int> pci; 

int main(){
    int test;
    scanf("%d",&test);
    
    for(int tt=1;tt<=test;tt++){
        printf("Case #%d: ",tt);
        int n,elem,mmin=INF,xo=0,acc=0;
        scanf("%d",&n);
        
        for(int i=0;i<n;i++){
            scanf("%d",&elem);
            acc+=elem;
            mmin=min(mmin,elem);
            xo^=elem;
        }
        
        if(xo) printf("NO");
        else printf("%d",acc-mmin);
        printf("\n");
    }

    return 0;
}
