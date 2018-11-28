#include<iostream>
#include<vector>

using namespace std;

bool searchV(vector<string>&sv,string s)
{
  for(int i=0;i<sv.size();i++)
  {
          if(sv[i]==s)
          return 1;
  }     
  return 0;
}


int main()
{
 freopen("out.txt","w",stdout);
   freopen("A-large.in", "r", stdin);

 
 int T;
 cin>>T;
 
 for(int I=1;I<=T;I++)
 {
         int N,M;
         cin>>N>>M;
         
         vector<string> ex;
         
         for(int i=0;i<N;i++)
         {
                 string str;
                 cin>>str;
                 
                 ex.push_back(str);
         }
         int cnt=0;
     
         for(int i=0;i<M;i++)
         {
                    // cout<<"X";
                 string path;
                 cin>>path;
                 
                 string str;
                 str+=path[0];
                 
                 for(int j=1;j<=path.size();j++)
                 {
                         if(j==path.size()&&!searchV(ex,str))
                         {
                                                             
                                                    //         cout<<j<<" "<<str<<endl;
                                                    ex.push_back(str);      
                                                    cnt++;   
                                                    str+=path[0];
                         }
                         if(path[j]==path[0])
                         {
                                             
                                         if(!searchV(ex,str))
                                         {
                                                    //         cout<<j<<" "<<str<<endl;
                                                    ex.push_back(str);      
                                                    cnt++;   
                                                    
                                         } str+=path[0];
                         }
                         else 
                         {
                              str+=path[j];
                         }
                 }
                 
                 
         }
         
         cout<<"Case #"<<I<<": "<<cnt<<endl;
 }
// system("pause");
 
 return 0;   
}
