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

char buff[505];

int main(){
    int test;
    scanf("%d",&test);
    for(int tt=1;tt<=test;tt++){
        printf("Case #%d: ",tt);
        map<string,int> path;
        int n,m,res=0;
        scanf("%d %d",&n,&m);
        for(int i=0;i<n;i++){
            scanf("%s",buff);
            string s(buff);
            int ind=1,ind2;
            while((ind2=s.find('/',ind))!=-1){
                string pa=s.substr(0,ind2);
                
                ind=ind2+1;
                path[pa]=1;
            }
            path[s]=1;
        }
        
         for(int i=0;i<m;i++){
            scanf("%s",buff);
            string s(buff);
            int ind=1,ind2;
            while((ind2=s.find('/',ind))!=-1){
                string pa=s.substr(0,ind2);
                //cout<<pa<<endl;
                ind=ind2+1;
                if(!path.count(pa)){
                    path[pa]=1;
                    res++;
                }
            }
            if(!path[s]){
                path[s]=1;
                res++;
            }
        }  
        printf("%d\n",res);    
    }
    return 0;
}
