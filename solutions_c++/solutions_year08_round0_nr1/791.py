#include<iostream>
#include<string>
#include<cstdio>
#include<vector>
using namespace std;

int cou(vector<string> s , vector<string> q)
{ int max=0,k=0,count=0;
  string lasttry="";
  while(k<q.size())
  {  
     for(int i=0;i<s.size();++i)
     { if(lasttry==s[i])
       continue;
       int temp=q.size();
       for(int j=k;j<q.size();++j)
       { if(q[j]==s[i])
         { temp=j;
           break;
         }
       }  
       if(max<temp)
       { max=temp;
         //cout<<max;
       }
        
      }
     
        
   if(max<q.size())
    { ++count;
      lasttry=q[max];
    } 
   k=max+1;
 } 
 return count;
}
int main()
{ freopen("in.IN","r",stdin);
  freopen("output.txt","w",stdout);  
  int n,n1,n2;
  char tem[100];
  
  cin>>n;
  
  for(int i=1;i<=n;++i)
  { vector<string> s1,q1;
    cin>>n1;
    cin.getline(tem,100);
    for(int j=1;j<=n1;++j)
    { 
      cin.getline(tem,100);
      
      s1.push_back(string(tem));
    }
    cin>>n2;
    cin.getline(tem,100);
        
    for(int j=1;j<=n2;++j)
    { cin.getline(tem,100);
      q1.push_back(string(tem));
    }  
    
    
    cout<<"Case #"<<i<<": ";
    cout<<cou(s1,q1)<<endl;
  }
 
}          
