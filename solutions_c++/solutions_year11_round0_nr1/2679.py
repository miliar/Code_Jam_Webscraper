#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
int main()
{
    int t,n,time,o,b,get,timeo,timeb,num[105],oldo,oldb;
    char s[105];
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        timeo=timeb=time=oldo=oldb=0;
        o=b=1;
        cin>>n;
        for(int j=0;j<n;j++)
            cin>>s[j]>>num[j];
        for(int j=0;j<n;j++)
        {
            if(s[j]=='O')
            {
                get=num[j];// 目标位置
                if(get>o)
                    timeo=get-o+1;//当前位置到目标位置并按下按钮需时
                else
                    timeo=o-get+1;
                if(timeo-1<=oldb)//走路需时小于等待blue时间
                {
                    time++;
                    oldb=0;
                    oldo=1;
                }
                else
                {
                    timeo-=oldb;
                    oldo+=timeo;
                    time+=timeo;
                    oldb=0;
                }
                o=get;
            }
            else
            {
                get=num[j];// 目标位置
                if(get>b)
                    timeb=get-b+1;//当前位置到目标位置并按下按钮需时
                else
                    timeb=b-get+1;
                if(timeb-1<=oldo)//走路需时小于等待orange时间
                {
                    time++;
                    oldo=0;
                    oldb=1;
                }
                else
                {
                    timeb-=oldo;
                    oldb+=timeb;
                    time+=timeb;
                    oldo=0;
                }
                b=get;
            }
        }
        cout<<"Case #"<<i<<": "<<time<<endl;
    }
    return 0;
}
