#include <iostream>
#include <stdio.h>
using namespace std;

double cyc[1111];

int N;
int A[1111];
int V[1111];
void test()
{
    cin>>N;
    int i;
    for(i=0;i<N;i++)
    {
        cin>>A[i];
        A[i]--;
        V[i]=0;
    }
    double ans=0;

    int x,cnt;

    for(i=0;i<N;i++) if(!V[i])
    {
        cnt=0;
        x=i;
        while(!V[x])
        {
            cnt++;
            V[x]=1;
            x=A[x];
        }
        ans+=cyc[cnt];
    }
    cout<<ans;
}

void precalc()
{
    cyc[0]=cyc[1]=0;
    int i;
    double sum=0,dv;

    for(i=2;i<1100;i++)
    {
        dv=i-1;
        cyc[i]=(sum+double(i))/dv;
        cyc[i]=i;
        sum+=cyc[i];
    }
    //for(i=1;i<30;i++)
      //  cout<<i<<":"<<cyc[i]<<endl;

}
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int i,T;
    cin>>T;
    precalc();
    for(i=0;i<T;i++)
    {
      cout<<"Case #"<<i+1<<": ";
      test();
      cout<<endl;
    }
    return 0;
}
