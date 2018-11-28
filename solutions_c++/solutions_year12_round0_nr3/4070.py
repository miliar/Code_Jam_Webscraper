#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <cmath>
#include <sstream>
using namespace std;
int s2i(string s)
{
  //  cout<<"string to convert "<<s<<endl;
    int res=0;
    for (int i =0; i<s.length(); i++)
        res+=int(s[i]-'0')*pow(10,(s.length()-1-i));
      //  cout<<"done "<<res<<endl;
    return res;
}
string i2s (int n)
{
    string res="";
    while (n>0)
    {
        res=char(n%10+'0')+res;
        n/=10;
    }
    return res;
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("p3small0.out","w",stdout);
    int T;
    cin>>T;
    for (int asd=0; asd<T; asd++)
    {
        int A,B;
        cin>>A>>B;
       // cout<<A<<" "<<B<<endl;
        int tot=0;
        for(int i =A; i<B; i++)
        {
            string s=i2s(i);
           // cout<<s<<endl;
            int first =int(s[0]-'0');
            for (int j=1; j<s.length(); j++)
            {
                if (int(s[j]-'0')>=first)
                {
                    int val=s2i(s.substr(j,s.length())+s.substr(0,j));
                   // cout<<"val "<<val<<endl;
                    if (val>i and val<=B){
                        tot++;
                      //  cout<<i<<" "<<val<<endl;
                    }
                }
            }
        }
        cout<<"Case #"<<asd+1<<": "<<tot<<endl;
    }
}
