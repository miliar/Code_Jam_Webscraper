#include<iostream>
#include<string>
#include<map>
#include<cmath>
using namespace std;

map<char,long long> m;

int main()
{long long  T;
    
    
    string st;
    freopen("A-small-attempt3.in","r",stdin);
    freopen("tt.out","w",stdout);
   cin>>T;
    for(long long K=1;K<=T;K++)
    {
      m.clear();
      cin>>st; 
      long long vis[50];
      memset(vis,0,sizeof vis);
      long long c=1,i,ttt=0;
      for(i=0;i<st.size();i++)
      {
                              
                              if(m[st[i]])
                              {
                                if(m[st[i]]==-1)vis[i]=0;
                                else
                                vis[i]=m[st[i]];   
                                          
                                          
                              }
                              else
                              {
                                if(ttt==1)
                                {
                                  vis[i]=0;
                                  m[st[i]]=-1;                  
                                                  
                                }
                                else
                                {
                                vis[i]=c;
                                m[st[i]]=c;
                                c++;
                                }
                                ttt++;
                              }
                              
      }  long long ans=0,p=1;       
       for(i=st.size()-1;i>=0;i--)
       {
        //  cout<<vis[i]<<" "<<p<<endl;
          ans+=vis[i]*p;
          p*=c;                        
                                  
                                  
       }
         // cout<<endl;
         cout<<"Case #"<<K<<": "<<ans<<endl;     
              
              
    }
    
    
    
    
    
 return 0;   
}
