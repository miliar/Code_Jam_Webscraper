#include <iostream>
#include <string>

using namespace std;

int l,d,n,i,j,k;
bool b[15][26];
string a[5000];

int main()
{
    freopen("gcj1.in","r",stdin);
    freopen("gcj1.out","w",stdout);
    cin>>l>>d>>n;
    for (i=0;i<d;i++)
        cin>>a[i];
    for (i=0;i<n;i++)
    {
        string s;
        cin>>s;
        memset(b,false,sizeof(b));
        j=0;
        int p=0;
        while (j<s.size())
        {
            if (s[j]=='(')
            {
                          ++j;
                          while (s[j]!=')')
                          {
                                b[p][int(s[j])-97]=true;
                                j++;
                          }
                          ++j;++p;
                          continue;
            }
            b[p][int(s[j])-97]=true;
            ++j;++p;
        }
        int ans=0;
        for (j=0;j<d;j++)
        {
            bool bo=true;
            for (k=0;k<l;k++)
                if (!b[k][int(a[j][k])-97])
                {
                                     bo=false;
                                     break;
                }
            if (bo) ans++;
        }
        cout<<"Case #"<<i+1<<": "<<ans<<endl;
    }
    return 0;
}
