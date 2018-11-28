#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

int main()
{
    int t,n;
    char temp;
    int button;
    int blue[100],orange[100];
    char seq[100];
    //freopen("g:\\A-large.in","r",stdin);
    //freopen("g:\\A-large.out","w",stdout);
    cin>>t;
    for(int i=0;i<t;i++)
    {
        cin>>n;
        int p=0,q=0;
        for(int j=0;j<n;j++)
        {
            cin>>temp>>button;
             seq[j]=temp;
            if(temp=='O')
            {

                orange[q++]=button;
            }
            else
            {
                blue[p++]=button;
            }
        }
        int time[100]={0};
        int bs=0,os=0;
        //deal with sequence
        if(seq[0]=='O')
        {
            time[0]=orange[0];
            os++;
        }
        else
        {
            time[0]=blue[0];
            bs++;
        }
        for(int j=1;j<n;j++)
        {
            if(seq[j]==seq[j-1])
            {
                if(seq[j]=='O')
                {
                    time[j]=abs(orange[os]-orange[os-1])+1;
                    os++;
                }
                else
                {
                    time[j]=abs(blue[bs]-blue[bs-1])+1;
                    bs++;
                }
            }
            else
            {
                int need=0,dif=0,k=1;
                if(seq[j]=='O')
                {
                    if(os>0)
                    {
                        need=abs(orange[os]-orange[os-1]);
                    }
                    else
                    {
                        need=orange[os]-1;
                    }
                    while(j-k>=0&&seq[j-k]=='B')
                    {
                        dif+=time[j-k];
                        k++;
                    }
                    os++;
                }
                else
                {
                    if(bs>0)
                    {
                        need=abs(blue[bs]-blue[bs-1]);
                    }
                    else
                    {
                        need=blue[bs]-1;
                    }
                    while(j-k>=0&&seq[j-k]=='O')
                    {
                        dif+=time[j-k];
                        k++;
                    }
                    bs++;
                }
                if(need>dif)
                {
                    time[j]=need-dif+1;
                }
                else
                {
                    time[j]=1;
                }
            }
        }
        int result=0;
        for(int j=0;j<n;j++)
        {
            result+=time[j];
        }
        cout<<"Case #"<<i+1<<": "<<result<<endl;

    }
    return 0;
}
