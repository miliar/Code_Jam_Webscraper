#include<iostream>
#include<algorithm>
#include<cmath>
using namespace std;
double dist(double x1,double y1,double x2,double y2)
{
    return sqrt((y2-y1)*(y2-y1)+(x2-x1)*(x2-x1));
}
double ans;
double c,n;
double x[41];
double y[41];
double r[41];
double st[1000];
int main()
{
    cin>>c;
    for(int i=1;i<=c;i++)
    {
        cin>>n;
        for(int j=1;j<=n;j++)
        {
            cin>>x[j];
            cin>>y[j];
            cin>>r[j];
        }
        if(n==1)
        {
            ans=r[1];
        }
        if(n==2)
        {
            if(r[1]>=r[2])
            {
                ans=r[1];
            }
            else
            {
                ans=r[2];
            }
        }
        if(n==3)
        {
           /*for(int j=1;j<=3;j++)
            {
                int p1=(j+1)%3;
                int p2=(j+2)%3;*/
                st[1]=max((dist(x[2],y[2],x[3],y[3])+r[2]+r[3])/2,r[1]);
                st[2]=max((dist(x[1],y[1],x[3],y[3])+r[1]+r[3])/2,r[2]);
                st[3]=max((dist(x[2],y[2],x[1],y[1])+r[2]+r[1])/2,r[3]);                
                //cout<<dist(x[p1],y[p1],x[p2],y[p2])<<endl;
            //}
            ans=99999999;
            for(int j=1;j<=3;j++)
            {
                if(st[j]<ans)
                {
                    ans=st[j];
                }
            }
        }
        printf("Case #%d: %.6lf\n",i,ans);
    }
    ///////////////////
  system("pause");
  return 0;
}
