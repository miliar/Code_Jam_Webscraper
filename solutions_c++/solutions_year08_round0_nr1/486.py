#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<algorithm>

using namespace std;



int main()
{
 int n;
 cin>>n;
 for(int i=0;i<n;i++)
 {
  cout<<"Case #"<<i+1<<": ";         
  int n1,n2;
  cin>>n1;
  string s;
  getline(cin,s);
  map<string, vector<int> > apps;
  
  string ss;
  
  vector<int> empt(0);
  for(int j=0;j<n1;j++)
  {
    getline(cin,ss);
//    cout<<ss<<endl;
    apps[ss]=empt;
  }
  
  
   
  cin>>n2;
  getline(cin,s);
  for(int j=0;j<n2;j++)
  {
          
   getline(cin,ss);

    apps[ss].push_back(j);
  }
  
 // for(map<string,vector<int> >::iterator it=apps.begin();it!=apps.end();it++)
//  {
//   cout<<(it->first)<<endl;
//   for(int j=0;j<(it->second).size();j++)
//     cout<<(it->second)[j]<<endl;
//  } 
  int pos=-1;
  int its=0; 
  bool b=false;
  while(!b)
  {
    int pos1=pos;
    for(map<string,vector<int> >::iterator it=apps.begin();it!=apps.end();it++)
    {   
     // cout<<its<<" "<<(it->first)<<" "<<pos1<<endl;
      bool c=false;
      
      for(int k=0;k<(it->second).size();k++)
      {
        if( (it->second)[k]>=pos)
        {
//          cout<<"k: "<<pos1<<endl;
          pos1=max(pos1,(it->second)[k]);
          c=true;
          break;
        }      
      }
      if(!c)
       b=true;
    }
    pos=pos1;
    its++;
  }
  cout<<its-1<<endl;

  
  
    
  }  
}
