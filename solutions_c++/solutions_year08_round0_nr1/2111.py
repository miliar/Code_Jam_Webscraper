#include<iostream>
#include<vector>
#include<string>
#include<sstream>
using namespace std;
#define MAX 150

int find(vector<string> v,string s)
    {
    int z=v.size();
    for(int j=0;j<z;j++)
        if(v[j]==s) return j;    
    return -1;
    }

int main()
{
bool saw[MAX];    
vector<string> search;    
string s;
int n,q,z,cur,cnt,nos;
    
      getline(cin,s);
      stringstream sa1(s);   
     sa1>>n;
    
    for(int i=0;i<n;i++)
        {
      getline(cin,s);
      stringstream sa2(s);   
      sa2>>z;
    
        search.clear();
        for(int j=0;j<z;j++) { 
                                getline(cin,s); search.push_back(s); 
                               // cout<<s<<endl; 
                             }
                             
        //cout<<"collected "<<z<<" elements"<<endl;               
        
         getline(cin,s);
         stringstream sa3(s);   
         sa3>>q;
    
        cnt=0; nos=0;
        for(int j=0;j<MAX;j++) saw[j]=0;
        
        //cout<<"Getting "<<q<<" queries...."<<endl;
        
        for(int j=0;j<q;j++)
                    {
                    
                    getline(cin,s);
                    cur=find(search,s);
                    if(cur==-1) cout<<"Err........"<<endl;
                    else 
                            {
                         if(saw[cur]==0) 
                                    {
                                    saw[cur]=1;
                                    nos++;
                                    } 
                         if(nos==z)
                                {
                                nos=0;    
                                cnt++;
                                for(int k=0;k<MAX;k++) saw[k]=0;
                                saw[cur]=1; nos=1;
                                }
                         }                            
                    }
                    
         cout<<"Case #"<<i+1<<": "<<cnt<<endl;
         }
         
return 0;    
}
