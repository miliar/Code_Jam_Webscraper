#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
using namespace std;
int a[110];
int main()
{
    //freopen("B-large.in","r",stdin);
   // freopen("B-large.out","w",stdout);
    int T,n,s,p;
    cin>>T;
    for(int i=1; i<=T; i++)
    {
        int count=0,sur=0,flag=0;
        cin>>n>>s>>p;
        for(int j=0; j<n; j++)
            cin>>a[j];
        for(int j=0; j<n; j++)
        {
            int temp=a[j]/3;
            int tmp=a[j]%3;
            if(temp>=p)
            {
                count++;
                if(tmp==2||tmp==0)
                    flag++;
            }
            else
            {
                if(tmp==1)
                {
                    if(temp+1>=p)
                    {
                        count++;
                        continue;
                    }
                }
                if(tmp==2)
                {
                    if(temp+1>=p)
                        count++;
                    else if(temp+2>=p)
                    {
                        if(sur!=s)
                        {
                            count++;
                            sur++;
                        }
                    }
                }
                if(tmp==0&&temp>0)
                {
                    if(sur!=s)
                    {
                        if(temp+1>=p)
                            {
                                count++;
                                sur++;
                            }
                    }
                }
            }
        }
        cout<<"Case #"<<i<<": "<<count<<endl;
    }
    return 0;
}
