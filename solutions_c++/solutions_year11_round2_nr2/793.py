#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
using namespace std;

int T,C,V[205];
double D,P[205];

int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("a.out","w",stdout);
    cin>>T;
    for(int ca=1;ca<=T;ca++)
    {
        cin>>C>>D;
        for(int i=1;i<=C;i++)
        {
            scanf("%lf%d",P+i,V+i);
        }
        double right=10e20,left=0;
        double esp=10e-12;
        while(fabs(right-left)>esp)
        {
            double mid=(right+left)/2;
            double leftmost=-10e10;
            bool ch=true;
            for(int i=1;i<=C;i++)
            {
                for(int j=1;j<=V[i];j++)
                {
                    double tmp=leftmost+D;
                    if(fabs(tmp-P[i])<=mid)
                    {
                        leftmost=tmp;
                    }
                    else
                    {
                        if(tmp<P[i])
                        {
                            leftmost=P[i]-mid;
                        }
                        else
                        {
                            ch=false;
                            break;
                        }
                    }
                }
                if(!ch)
                {
                    break;
                }
            }
            if(ch)
            {
                right=mid;
            }
            else
            {
                left=mid;
            }
        }
        printf("Case #%d: %.10f\n",ca,right);
    }
    return 0;
}
