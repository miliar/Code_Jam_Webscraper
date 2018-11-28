#include<iostream>
#include<stdio.h>
using namespace std;
int seq[110];
char rb[110];
int n;
void reset(char c,int &a,int b)
{
    while(b<=100 && rb[b]!=c) b++;
    a=seq[b];
}
void move(int &a,int b)
{
    if(a<b) a++;
    else if(a>b) a--;
}
int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-ans.txt","w",stdout);
    int t,i,j,k,m,p,ti;
    int dirofo,dirofb;
    char c;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cout<<"Case #"<<i<<": ";
        cin>>n;
        for(j=1;j<=n;j++)
        {
            cin>>c>>p;
            seq[j]=p;
            rb[j]=c;
           // cout<<rb[j]<<' '<<seq[j]<<endl;
        }
        j=k=p=1;
        m=1;
        ti=0;
        reset('O',dirofo,1);
        reset('B',dirofb,1);
        while(p<=n)
        {
           // cout<<j<<' '<<k<<' '<<dirofo<<' '<<dirofb<<' '<<p<<endl;
            if(rb[p]=='O' && j==seq[p])
            {
                p++;
                reset('O',dirofo,p);
                move(k,dirofb);
            }
            else if(rb[p]=='B' && k==seq[p])
            {
                p++;
                reset('B',dirofb,p);
                move(j,dirofo);
            }
            else
            {
                move(j,dirofo);
                move(k,dirofb);
            }
            ti++;
        }
        cout<<ti<<endl;
    }
}
