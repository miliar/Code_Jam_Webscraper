#include <iostream>
using namespace std;
int t,Oc,O_l,Bc,B_l;
int fab(int x)
{
    return x>0?x:-x;
}
void solve(char c,int x)
{
    int tmp=0;
    if(c=='O')
    {
        tmp=fab(x-Oc);
        if(tmp<(t-O_l))t++;
        else
        t+=(tmp-t+O_l+1);
        O_l=t;
        Oc=x;
    }
    else
    {
        tmp=fab(x-Bc);
        if(tmp<(t-B_l))t++;
        else
        t+=(tmp+B_l+1-t);
        B_l=t;
        Bc=x;
    }
    //cout<<"time = "<<t<<"  Oc ="<<Oc<<"  Bc ="<<Bc<<"   B_l="<<B_l<<"  O_l ="<<O_l<<endl;
}
int main()
{
   // freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int i,j,k,n,m;
    char c;
    while(cin>>n)
    {
        for(i=1;i<=n;i++)
        {
            t=0;
            Oc=Bc=1;
            O_l=B_l=0;
            cin>>m;
            for(j=0;j<m;j++)
            {
               cin>>c;
               cin>>k;
               solve(c,k);
            }
            printf("Case #%d: %d\n",i,t);
        }
    }
    return 0;
}
