#include <iostream>
#include <string>

using namespace std;

string s;
__int64 ans;
int i,j,t,di[40];

int calc(char c)
{
    if (c<='9') return (int(c)-48);
    else return (int(c)-87);
}

int main()
{
    freopen("gcj1.in","r",stdin);
    freopen("gcj1.out","w",stdout);
    cin>>t;
    for (int ii=1;ii<=t;ii++)
    {
        cin>>s;
        memset(di,0xff,sizeof(di));
        di[calc(s[0])]=1;
        int p=0;
        for (i=1;i<s.size();i++)
            if (di[calc(s[i])]==-1)
            {
               di[calc(s[i])]=p;
               if (p==0) p=2;
               else p++;
            }
        ans=0;
        p=max(2,p);
        long long temp=1;
        for (i=s.size()-1;i>=0;i--)
        {
                ans+=di[calc(s[i])]*temp;
                temp*=p;
        }
        cout<<"Case #"<<ii<<": "<<ans<<endl;
    }
    return 0;
}
