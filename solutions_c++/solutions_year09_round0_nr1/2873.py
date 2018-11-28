#include <iostream>

using namespace std;

int l,d,n;
string s[5100],st;
bool b[5100],bt[26];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d %d %d",&l,&d,&n);
    for (int i=0;i<d;i++) cin>>s[i];
    for (int i=0;i<n;i++)
    {
        memset(b,true,sizeof(b));
        cin>>st;
        int j=0;
        for (int k=0;k<l;k++)
        {
            memset(bt,false,sizeof(bt));
            if (st[j]=='(')
            {
                j++;
                while (st[j]!=')')
                {
                    bt[st[j]-'a']=true;
                    j++;
                }
                j++;
            }
            else
            {
                bt[st[j]-'a']=true;j++;
            }
            for (int w=0;w<d;w++) if (!bt[s[w][k]-'a']) b[w]=false;
        }
        int ans=0;
        for (int j=0;j<d;j++) if (b[j]) ans++;
        cout<<"Case #"<<i+1<<": "<<ans<<endl;
    }
}
