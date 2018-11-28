#include<iostream>
using namespace std;
int main2()
{
    int r,k,n;
    int q1[1000],q2[1000],q3[1000],qcost[1000];
    scanf("%d%d%d",&r,&k,&n);
    for(int i=0;i<n;i++)
    {
        scanf("%d",&q1[i]);
        q3[i]=0;
    }
    for(int i=0;i<n;i++)
    {
        int sum=q1[i],mk=1;
        for(int j=1;sum+q1[(i+j)%n]<=k && ((i+j)%n)!=i;j++)
        {
            sum+=q1[(i+j)%n];
            mk++;
        }
        q2[i]=mk;
        qcost[i]=sum;
    }
    int round=0,cost=0,qwe;
    for(int i=0,j=0;i<r;i++)
    {
        //if(q3[j]!=1)
        {
            q3[j]=1;
            cost+=qcost[j];
            j=(j+q2[j])%n;
        }/*else
        {
            round=j;
            qwe=i;
            break;
        }
        */
    }

cout<<cost<<"\n";
    return 0;
}
int main()
{
 int t;
 scanf("%d",&t);
 for(int i=0;i<t;i++)
 {
     cout<<"Case #"<<(i+1)<<": ";
     main2();
 }
}
