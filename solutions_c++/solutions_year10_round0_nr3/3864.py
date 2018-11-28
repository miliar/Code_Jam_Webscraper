#include<iostream>
#include<algorithm>
using namespace std;
#define get cin>>
#define put cout<<
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-out.out","w",stdout);
    int t,i,j,seats=0,s=0,gi=0;
    get t;
    for(i=1;i<=t;i++)
    {
        int r,max,g,temp=0;
        get r>>max>>g;
        int q[g],money=0;
        for(int j=0;j<g;j++)
        {get q[j];temp+=q[j];}
        if(max>=temp)
        {money+=temp*r; put "Case #"<<i<<": "<<money<<endl; continue;}
        for(int j=0;j<r;j++)
        {
            for(;;)
            {
                if(s==g){s=0;}
                if(seats+q[s]<=max)
                {seats+=q[s];s++;}
                else
                {money+=seats;seats=0;break;}
            }
        }
            put "Case #"<<i<<": "<<money<<endl;
            money=0;s=0;
    }
}
