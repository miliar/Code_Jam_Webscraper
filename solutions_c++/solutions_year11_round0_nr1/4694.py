#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int T,n;
int o[105],b[105];
struct goal
{
    char M;
    int bb;
}ob[105];
int step_o;
int step_b;
int t;
int g_o,g_b,g_ob;
int Abs(int a)
{
    return a>=0?a:-a;
}
int min(int a,int b)
{
    return a<b?a:b;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int cas=0;
    int i,j_o,j_b;
    char m;
    int s;
    cin>>T;
    while(T--)
    {
        cin>>n;
        j_o=j_b=1;
        for(i=1;i<=n;i++)
        {
            cin>>m>>s;
            ob[i].M=m;
            ob[i].bb=s;
            //cout<<s<<endl;
            if(m=='O')
                o[j_o]=s,j_o++;
            else
                b[j_b]=s,j_b++;
        }
        step_o=step_b=1;
        t=0;
        g_o=g_b=g_ob=1;
        while(g_ob<=n)
        {
            if(ob[g_ob].M=='O')
            {
                t+=(Abs(step_o-ob[g_ob].bb));
                if(g_b<j_b)
                    step_b=step_b<=b[g_b]?(step_b+min(Abs(step_o-ob[g_ob].bb)+1,(b[g_b]-step_b))):(step_b-min(Abs(step_o-ob[g_ob].bb)+1,(step_b-b[g_b])));
                t++;
                step_o=ob[g_ob].bb;
                g_ob++;g_o++;
            }
            else
            {
                t+=(Abs(step_b-ob[g_ob].bb));
                if(g_o<j_o)
                    step_o=step_o<=o[g_o]?(step_o+min(Abs(step_b-ob[g_ob].bb)+1,(o[g_o]-step_o))):(step_o-min(Abs(step_b-ob[g_ob].bb)+1,(step_o-o[g_o])));
                t++;
                step_b=ob[g_ob].bb;
                g_ob++;g_b++;
            }
        }
        printf("Case #%d: %d\n",++cas,t);
    }
    //system("pause");
    return 0;
}
