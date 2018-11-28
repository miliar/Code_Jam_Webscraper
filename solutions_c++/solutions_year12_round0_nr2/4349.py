#include<iostream>
using namespace std;
int main()
{
    int tstcss,lp,n,sn,tg,sum,i,x,t1,t2;
    cin>>tstcss;
    for (lp=0;lp<tstcss;lp++)
    {
        cin>>n>>sn>>tg;
        sum=0;
        for (i=0;i<n;i++)
        {
            cin>>x;
            if (x%3==0)
            {
                t1=x/3;
                t2=x/3+1;
            }
            if (x%3==1)
            {
                t1=x/3+1;
                t2=x/3+1;
            }
            if (x%3==2)
            {
                t1=x/3+1;
                t2=x/3+2;
            }
            if (x==0)
            {
                t1=0;
                t2=0;
            }
            if (x==1)
            {
                t1=1;
                t2=1;
            }
            if (t1>=tg)
            {
                sum++;
                continue;
            }
            if (sn==0) continue;
            if (t2>=tg)
            {
                sum++;
                sn--;
                continue;
            }
        }
        cout<<"Case #"<<lp+1<<": "<<sum<<endl;
    }
    return 0;
}
