#include <vector>
#include <string>
#include <iostream>
using namespace std;

int n;
vector <string> v;
void init()
{
     int l,d;
     cin>>l;
     cin>>d;
     cin>>n;
     for(int i=0;i<d;i++)
     {
             string t;
             cin>>t;
             v.push_back(t);
     }
}
int ncase(string x)
{
 int k=0;
 for(int i=0;i<v.size();i++)
  {
         bool b=1;
         int ind=0;
         for(int j=0;j<v[i].size()&&b==1;j++)
           {if(x[ind]!='('&&x[ind]!=v[i][j])b=0;
            if(x[ind]=='(')
             {
             ind++;
             bool h=0;
             while(x[ind]!=')')
              {if(x[ind]==v[i][j])h=1;
               ind++;
              }
             if(h==0)b=0;
             }
            ind++;
           }
         if(b==1)k++;  
   }
   
   return k;
}
int main()
{
    
    vector <int> sol;
    init();
    for(int i=0;i<n;i++)
    {
     string t;
     cin>>t;
     sol.push_back(ncase(t));
    }
    
    for(int i=0;i<sol.size();i++)
     cout<<"Case #"<<i+1<<": "<<sol[i]<<endl;
    return 0;
}
