#include<iostream>
using namespace std;
int main()
{
     freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int t,one=1;
    scanf("%d",&t);
    while(t-- >0)
    {
        int x[100],y[100],n;
        int i,j,k,count=0;
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%d%d",&x[i],&y[i]);
        }
        for(i=0;i<n;i++)
        {
            for(j=i+1;j<n;j++)
            {
                if(x[i]>x[j] && y[i]<y[j])
                count++;
                else
                if(x[i]<x[j] && y[i]>y[j])
                count++;
            }
        }
        cout<<"Case #"<<one++<<": "<<count<<endl;
    }
    return 0;
}
