#include<iostream>
#include<stdio.h>
#include<string>
#include<cstring>
using namespace std;
string com[90],op[80];
string vk;
char ans[200];
int isin[30];
int main()
{
   // freopen("B-small-attempt1.in","r",stdin);
    //freopen("ain.txt","r",stdin);
    //freopen("B-large.in","r",stdin);
  // freopen("A-ans.txt","w",stdout);
    int t,c,d,n,i,j,k,p;
    bool f0,f1;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cout<<"Case #"<<i<<": ";
        cin>>c;
        k=0;
        for(j=0;j<c;j++)
        {
            string s;
            cin>>s;
            com[k++]=s;
            char ch=s[0];
            s[0]=s[1];
            s[1]=ch;
            com[k++]=s;
        }
        cin>>d;
        k=0;
        for(j=0;j<d;j++)
        {
            string s;
            cin>>s;
            op[k++]=s;
            char ch=s[0];
            s[0]=s[1];
            s[1]=ch;
            op[k++]=s;
        }
        cin>>n>>vk;
        memset(isin,0,sizeof(isin));
        p=0;
        for(j=0;j<n;j++)
        {
            ans[p++]=vk[j];
            isin[vk[j]-'A']++;
            if(p>=2)
            {
                string s;
                s+=ans[p-1];
                s+=ans[p-2];
                f0=false;
                for(k=0;k<c*2;k++)
                {
                    if(s==com[k].substr(0,2))
                    {
                        f0=true;
                        isin[s[0]-'A']--;
                        isin[s[1]-'A']--;
                        ans[p-2]=com[k][2];
                        p--;
                        break;
                    }
                }
                f1=false;
                if(!f0)
                {
                    for(k=0;k<d*2;k++)
                    {
                        if(vk[j]==op[k][0] && isin[op[k][1]-'A'])
                        {
                            p=0;
                            memset(isin,0,sizeof(isin));
                        }
                    }
                }
            }
        }
        cout<<'[';
        for(j=0;j<p;j++)
        {
            if(j==p-1) cout<<ans[j];
            else
            cout<<ans[j]<<", ";
        }
        cout<<']'<<endl;
    }
}
