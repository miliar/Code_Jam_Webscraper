#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;

struct node
{
    string s;
    int v;
} a[50];

void Swap(int i,int j)
{
    string tmp1=a[i].s;
    a[i].s=a[j].s;
    a[j].s=tmp1;
    int tmp2=a[i].v;
    a[i].v=a[j].v;
    a[j].v=tmp2;
    return;
}

int main()
{
    int T,n,i,j,k,res,cas;
    
    freopen("d://in.txt","r",stdin);
    freopen("d://out.txt","w",stdout);
    cin>>T;
    for (cas=1;cas<=T;cas++)
    {
        cin>>n;
        for (i=0;i<n;i++)
        {
            cin>>a[i].s;
            a[i].v=0;
            for (j=0;j<a[i].s.length();j++)
            {
                if (a[i].s[j]=='1') a[i].v=j;
            }
        }
        res=0;
        for (i=0;i<n;i++)
        {
            if (a[i].v>i)
            {
                for (j=i+1;j<n;j++)
                {
                    if (a[j].v<=i)
                    {
                        for (k=j;k>i;k--)
                        {
                            Swap(k,k-1);
                            res++;
                        }
                        break;
                    }
                }
            }
        }
        cout<<"Case #"<<cas<<": "<<res<<endl;
    }
    return 0;
}
