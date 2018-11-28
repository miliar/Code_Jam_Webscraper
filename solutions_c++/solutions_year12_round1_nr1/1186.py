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
#include <cstdio> 
using namespace std; 
  
#define INF 0x3f3f3f3f
#define ALL(v) v.begin(),v.end() 
typedef pair<char,int> pci; 

double p[1000005];

int main(){
    int test;
    scanf("%d",&test);
    
    for(int tt=1;tt<=test;tt++){
        int A,B;
        scanf("%d %d",&A,&B);
        
        double prod=1.0;
        for(int i=0;i<A;i++){
            scanf("%lf",&p[i]);
            
            prod*=p[i];        
        }
        double giveup=1.0+B+1.0;
        double ct=prod*(B-A+1)+(1-prod)*(B-A+1+B+1);

        prod=1.0;
        double res=1e100;
        for(int i=A,j=0;i>=1;i--,j++){
            double pr=prod*(i+B-A+i+1)+(1-prod)*(i+B-A+i+1+B+1);
            prod*=p[j];
            res=min(res,pr);
        }
        
        printf("Case #%d: %.6lf\n",tt,min(min(res,ct),giveup));
    }

    return 0;
}
