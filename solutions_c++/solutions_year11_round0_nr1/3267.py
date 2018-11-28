#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int TT,tt=0;
    cin>>TT;
    while(TT--)
    {
        tt++;
        int N,i,j,o=1,b=1,T=0,s,d,pa=-1,pb=-1;
        int a[200];
        char cc,c[200];
        cin>>N;
        for(i=0;i<N;i++)
        {
            scanf("%c%c%d",&cc,&cc,&s);
            a[i] = s, c[i] = cc;
        }
        for(i=0;i<N;i++)
        {
            cc = c[i];
            s = a[i];
            if(cc=='O')
            {
                pa = a[i];
                T+=(abs(s - o) + 1);
                d = abs(s - o) + 1;
                o = s;
                for(j=i+1;j<N;j++)
                {
                    if(c[j]=='B')
                    {
                        break;
                    }
                }
                if(j!=N)
                {
                    if(a[j]>=pb)
                    {
                        if((b+d)>=a[j])
                        b = a[j];
                        else
                        b = b + d;
                    }
                    else
                    if(a[j]<pb)
                    {
                        if((b-d)>=a[j])
                        {
                            b = b - d;
                        }
                        else
                        b = a[j];
                    }
                }
                c[i]='D'; /* Indicating Done */
            }
            else
            if(cc=='B')
            {
                pb = a[i];
                T+=(abs(s - b) + 1);
                d = abs(s - b) + 1;
                b = s;
                for(j=i+1;j<N;j++)
                {
                    if(c[j]=='O')
                    {
                        break;
                    }
                }
                if(j!=N)
                {
                    if(a[j]>=pa)
                    {
                        if((o+d)>=a[j])
                        o = a[j];
                        else
                        o = o + d;
                    }
                    else
                    if(a[j]<pa)
                    {
                        if((o-d)>=a[j])
                        {
                            o = o - d;
                        }
                        else
                        o = a[j];
                    }
                }
                c[i]='D'; /* Indicating Done */
            }
        }
        cout<<"Case #"<<tt<<": "<<T<<endl;
    }
    return 0;
}
