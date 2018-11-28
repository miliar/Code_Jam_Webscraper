#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std;
int main()
{
     freopen("C://Users//abir//Desktop//Topcoder//a.in","r",stdin);
     freopen("C://Users//abir//Desktop//Topcoder//a.out","w",stdout);
    int t,x,c=1,i,n,m,j;
    string str;
      cin>>t;
      while(t--)
      {
            cin>>n>>m;
            map<string,bool>mt;
            for(i=0;i<n;i++)
            {
                cin>>str;
                for(j=1;j<str.size();j++)
                {
                    if(str[j]=='/')mt[string(str,0,j)]=1;//,cout<<" asdas "<<string(str,0,j)<<endl; 
                }
                mt[str]=1;//,cout<<" asdas "<<str<<endl;
            }
            x=0;
            for(i=0;i<m;i++)
            {
                cin>>str;
                for(j=1;j<str.size();j++)
                {
                    if(str[j]=='/')if(mt[string(str,0,j)]==0)mt[string(str,0,j)]=1,x++; 
                }
                if(mt[str]==0)mt[str]=1,x++; 
            }
            cout<<"Case #"<<c++<<": "<<x<<endl;
            //else cout<<"Case #"<<c++<<"<<endl;
            
       }    
    cin>>i;
    return 0;
}
