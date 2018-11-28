#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string>
#include<string.h>

using namespace std;

int t,i,j,n,k,Q,a[99],fix[999],v;
long long p,x;
string s;

main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&t);
    for(Q=1;Q<=t;Q++)
    {
        cin>>s;
        n=s.size();
        memset(a,0,sizeof(a));
        memset(fix,0,sizeof(fix));
        k=1; v=0;
        for(i=0;i<n;i++)
        {
            if(!fix[s[i]])
            {
                v++;
                for(j=0;j<n;j++)
                    if(s[j]==s[i])
                        a[j]=k;
                fix[s[i]]=true;
                if(k==1)k=0; else
                if(k==0)k=2; else k++;
            }
        }
        p=0; if(v==1)v=2; x=1;
        for(i=n-1;i>=0;i--)
        {
            p+=a[i]*x;
            x*=v;
        }
        printf("Case #%d: ",Q);
        cout<<p<<endl;
    }
}
