#include <iostream>
const int maxn = 201;

int T;
int C,N,D;
int p[maxn],v[maxn];

bool can(double k)
{
     double pp = p[0] - k;
     if (2 * k < (v[0] - 1) * D)
        return false;
     pp += v[0] * D;
     double dir = -1;
     for (int i = 1; i < C; ++i)
     {
         if (2 * k < (v[i]-1) * D)
            return false;
         if (pp < p[i] - k)
            pp = p[i] - k ;
         pp = pp + (v[i] - 1) * D;
         if (pp > p[i] + k)
                return false;                  
         pp += D;
     }
     return true;
}

void process()
{
     double max=D*N;
     double min=0;
     double mid;
     while(max - min > 1e-7)
     {
         mid = (max + min) / 2;
         if (can(mid))
            max = mid;
         else min = mid;
     }
     printf("Case #%d: %.8lf\n",T,min);
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int _T;
    scanf("%d",&_T);
    for (T = 1; T <= _T; ++T)
    {
        N = 0;
        scanf("%d %d",&C,&D);
        for (int i = 0; i < C; ++i)
        {
            scanf("%d %d",p+i,v+i);
            N += v[i];
        }
        process();
    }
    
    return 0;
}
