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
                get=num[j];// Ŀ��λ��
                if(get>o)
                    timeo=get-o+1;//��ǰλ�õ�Ŀ��λ�ò����°�ť��ʱ
                else
                    timeo=o-get+1;
                if(timeo-1<=oldb)//��·��ʱС�ڵȴ�blueʱ��
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
                get=num[j];// Ŀ��λ��
                if(get>b)
                    timeb=get-b+1;//��ǰλ�õ�Ŀ��λ�ò����°�ť��ʱ
                else
                    timeb=b-get+1;
                if(timeb-1<=oldo)//��·��ʱС�ڵȴ�orangeʱ��
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
