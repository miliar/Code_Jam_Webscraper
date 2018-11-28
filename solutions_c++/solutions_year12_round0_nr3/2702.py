#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
    int t,x,y,i,j,l;
    string a,b,n,m,s[6];
    char temp;
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    cin>>t;
    for (x=1;x<=t;x++)
    {
        cin>>a>>b;
        l=a.size();
        y=0;
        n=a;
        while (n<b)
        {
            m=n;
            for (i=0;i<l-1;i++)
            {
                temp=m[l-1];
                for (j=l-1;j>0;j--) m[j]=m[j-1];
                m[0]=temp;
                s[i]=m;
            }
            sort(s,s+l-1);
            if (s[0]>n&&s[0]<=b) y++;
            for (i=1;i<l-1;i++)
            {
                if (s[i]==s[i-1]) continue;
                if (s[i]>n&&s[i]<=b) y++;
            }
            for (i=l-1;i>=0;i--)
            {
                if (n[i]<'9') {n[i]++;break;}
                else n[i]='0';
            }
        }
        cout<<"Case #"<<x<<": "<<y<<endl;
    }
    return 0;
}
