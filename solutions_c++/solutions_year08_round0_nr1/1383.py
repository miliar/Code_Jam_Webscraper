#include<string>
#include<map>
#include<iostream>

using namespace std;

char buf[1000];

map<string,int> deref;

int n;
int ns;

int seq[1050];
int dp[1050][120];

int solve(int id,int s)
   {
      // cout<<"dd";
      if(id==n)return 0;
      if(dp[id][s]!=-1)return dp[id][s];
      
      int &ret = dp[id][s];
      //cout<<"hd";
      if(seq[id]!=s)
         {
            ret=solve(id+1,s);
         }
      else
         {
            //cout<<"haha";
            ret=5000;
            
            for(int i=0;i<ns;i++)
               {
                  if(s==i)continue;
                  ret=min(ret,1+solve(id+1,i));
               }
         }
      return ret;
   }

int main()
   {
      int m;
      cin>>m;
      cin.get();
      
      string temp;
      
      for(int caseid=0;caseid<m;caseid++)
         {
            memset(dp,-1,sizeof(dp));
            cin>>ns;
            cin.get();
            
            for(int i = 0;i<ns;i++)
               {
                  cin.getline(buf,1000);
                  temp=string(buf);
                  deref[temp]=i;
                  //  cout<<buf;
               }
            
            cin>>n;
            cin.get();
            
            for(int i=0;i<n;i++)
               {
                  cin.getline(buf,1000);
                  temp=string(buf);
                  seq[i]=deref[temp];
                  //   cout<<seq[i];
               }
            
            int res = 5000;
            
            for(int i=0;i<ns;i++)
               {
                  res=min(res,solve(0,i));
               }
            
            cout<<"Case #"<<(caseid+1)<<": "<<res<<endl;
         }
   }
