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

int m[1<<12];
int b[1<<12];

void proc(int i,int tot){
    //cout<<i<<" "<<tot<<endl;
    if(i<1) return; 
    if(tot>0)
        proc(i>>1,tot-1);
    else{
        b[i]=1;
        proc(i>>1,0);
    }
}

int main(){
    int test;
    scanf("%d",&test);
    for(int tt=1;tt<=test;tt++){
        printf("Case #%d: ",tt);
        int n;
        scanf("%d",&n);
        //cout<<"n="<<n<<endl;
        for(int  i=1;i<=(1<<n);i++)
            scanf("%d",&m[i]);
        
        int one;
        for(int j=n-1;j>=0;j--)
        for(int  i=1;i<=(1<<j);i++){
            scanf("%d", &one);
            //cout<<one<<">"<<endl;
        }
        
        
        memset(b,0,sizeof(b));
        for(int i=0;i<(1<<n);i++)
            proc(((1<<n)+i)>>1,m[i+1]);
        
        int res=0;
        for(int  i=1;i<=(1<<n);i++)
            if(b[i])
                res++;
                   
        printf("%d",res);
        
        printf("\n");
    }    
}
