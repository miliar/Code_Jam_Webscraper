#include<stdio.h>
#include<algorithm>
#include<cmath>
#include<iostream>
using namespace std;
#define LL long long
const double eps = 0.0000001;
struct NODE
    {
        double x;
        int cnt;
    };
NODE arr[300];
int n;
double D;
bool cmp(const NODE &a , const NODE &b)
    {
        return a.x < b.x;
    }
bool EQ(double a)
    {
        return fabs(a) <eps;
    }
bool judge(double t)
    {
        double mx = 1e5+t+100.0;
        for(int p = n-1 ; p>=0 ; p--)
            {
                for(int i = 1; i<= arr[p].cnt;i++)
                    {
                        if(EQ(mx - arr[p].x))
                            mx -=D;
                        else if(mx > arr[p].x)
                            {
                                if(arr[p].x + t < mx)
                                    mx = arr[p].x+t - D;
                                else mx -=D;
                            }
                        else if(mx < arr[p].x)
                            {
                                if(EQ(arr[p].x - t))
                                    mx -=D;
                                if(arr[p].x -t > mx)
                                    return false;
                                mx -= D;
                            }

                    }
            }
        return true;
    }
int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int T;
    scanf("%d",&T);

    for(int ii = 1 ; ii <=T; ii++)
    {


        scanf("%d%lf",&n,&D);
        for(int i = 0 ; i < n ; i++)
            scanf("%lf%d",&arr[i].x , &arr[i].cnt);
        sort(arr , arr+ n , cmp);
        double low = 0.0 , high = 2047483678.0;
        while(high - low > 1e-8)
            {
                double mid = (high + low) /2.0;
                if(judge(mid))
                    high = mid;
                else low = mid;
            }
        printf("Case #%d: ",ii);printf("%.10f\n",low);
    }
}
