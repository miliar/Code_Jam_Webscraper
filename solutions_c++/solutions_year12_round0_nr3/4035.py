#include <cstdlib>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <sstream>
#define N 2000010

using namespace std;

string s,t[10];
string u,v;
stringstream ss;
int o;

int fc(int n)
{
    int i,j,k;
    int l;
    l=s.length();
    k=0;
    for(i=0,j=n;j<l;j++,i++)
    {
        if(!k&&s[i]!=s[j])
            k=1;
        if(s[j]<s[i])
            break;
        if(s[j]>s[i])
            return 0;
        
    }
    if(j>=l)
    {
        for(j=0;i<l;i++,j++)
        {
            if(!k&&s[i]!=s[j])
                k=1;
            if(s[j]<s[i])
                break;
            if(s[j]>s[i])
                return 0;
            
        }
        if(!k)
        return 0;
    }
    for(i=0,j=n;j<l;j++,i++)
    {
        if(s[j]>u[i])
            break;
        if(s[j]<u[i])
            return 0;
    }
    if(j>=l)
    {
        for(j=0;i<l;i++,j++)
        {
            if(s[j]>u[i])
                break;
            if(s[j]<u[i])
                return 0;
        }
    }  
    t[o]=s.substr(n,l)+s.substr(0,n);  
    o++;
    return 1;
}

int main(int argc, char *argv[])
{
    freopen("C-large.in","r",stdin);
    freopen("c.out","w",stdout);
    int n,m;
    int i,j,k;
    int x,y;
    int l; 
    long long int ans;
    cin>>n;
    for(m=1;m<=n;m++)
    {
        cin>>x>>y;
        ss.clear();
        ss<<x;
        u.clear();
        ss>>u;
        ss.clear();
        ss<<y;
        v.clear();
        ss>>v;
        l=u.length();
        for(i=x+1,ans=0;i<=y;i++)
        {
           ss.clear(); 
           ss<<i;
           s.clear();
           ss>>s;
           for(j=1,o=0;j<l;j++)
           {
                if(fc(j))
                {
                    if(o)
                    {
                        for(k=0;k<o-1;k++)
                        {
                            if(t[o-1]==t[k])
                                break;
                        }
                        if(k<o-1)
                            continue;
                    }
                    ans++;
                }
           }
           
        }
        cout<<"Case #"<<m<<": "<<ans<<endl;
    }
   // system("PAUSE");
    return 0;
}
