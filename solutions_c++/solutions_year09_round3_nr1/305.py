#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <sstream>
#include <map>
using namespace std;

#define two(x)  (1<<x)
#define twol(x) ((long long)1<<x)
#define sqr(x)  ((x)*(x))

map<char,int> num; 

main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for (int task=1;task<=t;task++)
    {
        string s;
        cin>>s;   
        long long tot=2,cur=1,ans=0;
        bool used=false;
        num.clear();
        num[s[0]]=2;
        for (int i=1;i<s.length();i++)
            if (!num[s[i]])
            {
                num[s[i]]=used?++tot:1;
                used=1;   
            }
        for (int i=s.length()-1;i>=0;i--)
        {
            //cout<<num[s[i]]-1<<endl;
            ans+=(long long)(num[s[i]]-1)*cur;
            if (i)  cur*=tot;
        }
        cout<<"Case #"<<task<<": "<<ans<<endl;
        //printf("Case #%d: %d\n",task,ans);
    }
}
