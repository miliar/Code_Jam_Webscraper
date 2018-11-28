#include<iostream>
#include<string>
#include<vector>
using namespace std;

  vector<int> r;
    int T,P,Q,best[10005][10005];
int sol(int s,int e)
{
  //  cout<<s<<" "<<e<<endl;
    if(best[s][e]!=-1)return best[s][e];
    int ans=(1<<30);
    if(s>e)return 0;
    int i;
    bool f=0;
    for(i=0;i<r.size();i++)
    {//cout<<r[i]<<" "<<r[i]-s+e-r[i]<<" "<<s<<" "<<e<<endl;
      if(r[i]>=s&&r[i]<=e)
      {
      ans=min(ans,sol(s,r[i]-1)+sol(r[i]+1,e)+(r[i]-s)+(e-r[i]));
      f=1;
      }                       
                          
    }if(!f)return best[s][e]=0;
    return best[s][e]=ans;
    
    
}


int main()
{
    
    freopen("C-large.in","r",stdin);
    freopen("tt.out","w",stdout);
    cin>>T;
    int i,j,k;
    for(k=1;k<=T;k++)
    {r.clear();
    memset(best,-1,sizeof best);
        cin>>P>>Q;
        for(i=0;i<Q;i++)
        {
          int t;
          cin>>t;
          r.push_back(t);
        }
             
           cout<<"Case #"<<k<<": "<<sol(1,P)<<endl;          
                     
                     
                     
    }
    
    
    
    
    
 return 0;   
}
