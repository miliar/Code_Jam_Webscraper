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

int pre[25]={1,2,3,5,8,14,24,43,77,140,256,472,874,1628,3045,5719,10780,20388,38674,73562,140268,268066,513350,984911,1892875};

#define M 100003

int main(){
    int test;
    scanf("%d",&test);
    for(int tt=1;tt<=test;tt++){
        int n;
        scanf("%d",&n);
        printf("Case #%d: %d\n",tt,pre[n-2]%M);
        
    }
    return 0;
}
