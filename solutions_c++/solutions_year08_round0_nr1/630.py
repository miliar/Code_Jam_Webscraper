#include <iostream>
#include <string>
using namespace std;
string a[110],b[1010];
int main()
{freopen("d:\\A-large.in.txt","r",stdin);
freopen("d:\\out.txt","w",stdout);
    int i,j,k,lj,tt,first,n,s,q,ans;
    cin>>n;
    cin.get();
    for (tt=1;tt<=n;tt++)
    {
        cin>>s;
        cin.get();
        for (i=0;i<s;i++)
            getline(cin,a[i]);
        cin>>q;
        cin.get();
        for (i=0;i<q;i++)
            getline(cin,b[i]);
        ans=0;
        k=0;
        first=0;
        while (1)
        {
            lj=0;
            for (i=0;i<s;i++)
            {
                for (j=first;j<q;j++)
                    if (a[i]==b[j])
                        break;
                if (j>lj)
                    lj=j;
                if (j==q)
                    break;
            }
            if (lj==q)
                break;
            first=lj;
            ans++;
        }
        cout<<"Case #"<<tt<<": "<<ans<<endl;
    }
    return 0;
}