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

int arr[100005];

int main(){
    int test;
    scanf("%d",&test);
    
    for(int tt=1;tt<=test;tt++){
        printf("Case #%d: ",tt);
        int n,l,h;
        scanf("%d %d %d",&n,&l,&h);
        
        for(int i=0;i<n;i++)
            scanf("%d",&arr[i]);
        bool pr=false;
        for(int i=l;i<=h;i++){
            bool pos=true;
            for(int j=0;j<n;j++)
                if(!(arr[j]%i==0||i%arr[j]==0)){
                    pos=false;
                    break;
                }
            if(pos){
                pr=true;
                printf("%d",i);
                break;
            }
        }
        if(!pr){
            printf("NO");
        }
        printf("\n");
    }

    return 0;
}
