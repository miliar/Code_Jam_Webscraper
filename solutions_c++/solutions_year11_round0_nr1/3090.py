#include<cstdio>
#define pb push_back
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int abs(int g)
{
    if(g<0) return -g;
    return g;
}
int main()
{
    int t;
    scanf("%d",&t);
    for(int k=1;k<=t;k++)
    {
        int n;
        scanf("%d",&n);
        char prev;
        int opos=1,otime=0,bpos=1,btime=0;
        int time=0;
        vector<int>v1;
        vector<char>v2;
        char c;
        int x;
        for(int i=1;i<=n;i++)
        {
            cin>>c>>x;
            if(i==1)
            {
                if(c=='O')
                {
                    prev='O';
                    otime=x;
                    opos=x;
                    time=x;
                }
                else
                {
                    prev='B';
                    btime=x;
                    bpos=x;
                    time=x;
                }
            }
            else
            {
                v1.pb(c);
                v2.pb(x);
            }
        }
        for(int i=0;i<v1.size();i++)
        {
            char ch=v1[i];
            int  pos=v2[i];
            if(prev==ch)
            {
                if(ch=='O')
                {
                    int diff=abs(opos-pos);
                    time+=diff+1;
                    opos=pos;
                    otime=time;
                }
                else
                {
                    int diff=abs(bpos-pos);
                    time+=diff+1;
                    bpos=pos;
                    btime=time;
                }
            }
            else
            {
                if(ch=='O')
                {
                    int diff1=abs(time-otime);
                    int diff2=abs(opos-pos);
                    if(diff1>=diff2)
                    {
                        time++;
                    }
                    else
                    {
                        time+=diff2-diff1+1;
                    }
                    otime=time;
                    opos=pos;
                    prev='O';
                }
                else
                {
                    int diff1=abs(time-btime);
                    //int diff1=time;
                    int diff2=abs(bpos-pos);
                    if(diff1>=diff2)
                    {
                        time++;
                    }
                    else
                    {
                        time+=diff2-diff1+1;
                    }
                    btime=time;
                    bpos=pos;
                    prev='B';
                }
            }
        }
        printf("Case #%d: %d\n",k,time);
    }
    return 0;
}
