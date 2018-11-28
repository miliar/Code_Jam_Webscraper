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
typedef long long ll;
int arr[100005];
int c[100005];

int main(){
    int test;
    scanf("%d",&test);
    
    for(int tt=1;tt<=test;tt++){
        printf("Case #%d: ",tt);
        int boost,n,nc;
        ll tboost;
        scanf("%d %lld %d %d",&boost,&tboost,&n,&nc);
        
        for(int i=0;i<nc;i++)
            scanf("%d",&c[i]);
        
        for(int i=0;i<n;i++){
            arr[i]=c[i%nc];
            //cout<<arr[i]<<" ";
        }
        //cout<<endl;
        ll res=0;
        
        if(boost==0){
            for(int i=0;i<n;i++)
                res+=arr[i]*2;
        }else if(boost==1){
            res=1000000000000LL;
            for(int i=0;i<n;i++){
                ll temp=0;
                for(int j=0;j<n;j++)
                    if(j==i){
                        if(temp>tboost){
                            temp+=arr[i];
                        }else{
                            int pres=temp+2*arr[i];
                            //cout<<"pres="<<pres<<endl;
                            if(pres<=tboost)
                                temp+=2*arr[i];
                            else{
                                int rem=(tboost-temp)/2;
                                //cout<<"rem="<<rem<<" "<<arr[i]-rem<<endl;
                                temp+=(2*rem+(arr[i]-rem));
                                //cout<<"temp="<<temp<<endl;
                            }
                        }
                    }else{
                        //cout<<"i="<<i<<" temp2="<<temp<<endl;
                        temp+=arr[j]*2;
                    }
                //cout<<i<<" "<<temp<<endl;
                res<?=temp;
            }
        }else{
            res=1000000000000LL;
            for(int i=0;i<n;i++)
            for(int j=i+1;j<n;j++){
                ll temp=0;
                for(int k=0;k<n;k++)
                    if(k==i||k==j){
                        if(temp>tboost){
                            temp+=arr[k];
                        }else{
                            int pres=temp+2*arr[k];
                            if(pres<=tboost)
                                temp+=2*arr[k];
                            else{
                                int rem=(tboost-temp)/2;
                                temp+=(2*rem+(arr[k]-rem));
                            }
                        }
                    }else{
                        temp+=arr[k]*2;
                    }
                res<?=temp;
            }
        }
        printf("%I64d\n",res);    
    }

    return 0;
}
