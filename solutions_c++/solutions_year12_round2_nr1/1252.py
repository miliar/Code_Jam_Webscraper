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

const double EPS=1e-9;

int si[1005];
double mi[1005];

int main(){
    int test;
    scanf("%d",&test);
    
    for(int tt=1;tt<=test;tt++){      
        printf("Case #%d:",tt);
        int n;
        scanf("%d",&n);
        int s=0;
        int mmax=0;
        for(int i=0;i<n;i++){
            scanf("%d",&si[i]);
            s+=si[i];
        }
        
        for(int i=0;i<n;i++){
            double l=0,u=1.0,m;
            while(fabs(u-l)>=EPS){
                m=(l+u)/2.0;
                double resto=1.0-m;
                double acs=0.0;
                double tar=si[i]+m*s;
                for(int j=0;j<n;j++)
                    if(i!=j&&si[j]<tar){
                        double toget=double(tar-si[j])/double(s);
                        acs+=toget;                     
                    }
                if(fabs(acs-resto)<=EPS){
                    break;
                }else if(acs>resto){
                    u=m;                
                }else{
                    l=m;                
                }                
            }
            printf(" %.8lf",m*100);
        }
       printf("\n");
    }

    return 0;
}
