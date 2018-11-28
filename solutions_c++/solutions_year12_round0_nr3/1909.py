#include <iostream>
#include <string>
#include <map>
#define pii pair<int,int>
#define mp(a,b) make_pair(a,b)
using namespace std;
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int t;
    cin>>t;
    map <pii,int> p;
    for (int i=1; i<=t; i++)
    {
        int A,B,res=0;
        cin>>A>>B;
        for (int n=A; n<=B; n++)
        {
            string a;
            int m;
            char q[200];
            itoa(n,q,10);
            a=string(q);
            p.clear();
            for (int j=0; j<a.size(); j++)
                {
                 a+=a[0];
                 a.erase(a.begin(),a.begin()+1);
                 int m=0;
                 for (int k=0; k<a.size(); k++)
                     m=m*10+a[k]-'0';
                 if (m>n && m<=B && p[mp(n,m)]==0)
                    {
                         res++;
                         p[mp(n,m)]++;
                    }
                }
        }
        cout<<"Case #"<<i<<": "<<res<<endl;
    }
    return 0;
}
