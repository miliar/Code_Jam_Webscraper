#include<iostream>
#include<math.h>
using namespace std;



int len(int n)
{
 int ans = 0;
 while(n)
 {
  ans++;
  n/=10;        
 }
 return ans;
}


int powr(int k)
{
    int ans = 1;
    for(int i=0;i<k;i++)ans*=10;
    return ans;
        
}

bool vis[2000007];
int arr[2000007];

int main()
{
    
    freopen("C-large.in","r",stdin);
    freopen("tt.out","w",stdout);
    int T;
    cin>>T;
    memset(vis,0,sizeof vis);
    for(int cas = 1 ;cas<=T; ++cas){
            int A,B,i,ans = 0;
            cin>>A>>B;
            for(i=A;i<=B;i++){
                              int r = i;
                              int k = 10;
                              int c = 0;
                              int a = 0,j;
                              int SS = len(r);
                              while(c<=SS)
                              {c++;
                               int m = r%k;
                               int n = r/k; 

                               k*=10; 
                               if(!n||!m)continue;                             
                               int f = m*powr(len(n)) + n;
                           //    cout<<f<<" "<<endl;
                           
                               if(f>=A&&f<=B&&f!=r&&len(r)==len(f))
                                 arr[a++]=f;     
                              } 
                               for(j=0;j<a;j++)
                               {
                                if(!vis[arr[j]])ans++;
                                vis[arr[j]]=1;                
                               }              
                               for(j=0;j<a;j++)
                               {
                                vis[arr[j]]=0;                
                               }                                   
                               
                                              
                              
            }        
            cout<<"Case #"<<cas<<": "<<ans/2<<endl;
            
            
    }
    
    
    
    return 0;    
}
