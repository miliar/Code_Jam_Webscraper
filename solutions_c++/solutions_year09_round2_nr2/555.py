#include<iostream>
#include<string>
#include<sstream>
#include<cassert>
#include<algorithm>
using namespace std;

int main()
{
    int T;
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    cin>>T;
    int K=T;
    getchar();
    while(T--)
    {
              string s;
              cin>>s;
              s="0"+s;
              next_permutation(s.begin(),s.end());
              if(s[0]=='0')
                s=s.substr(1);
              cout<<"Case #"<<K-T<<": "<<s<<"\n";
    }
}    
    

                  
