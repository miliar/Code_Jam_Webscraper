#include <cstdio>
#include <cstdlib>
#include <cmath>

int r[1010];
double x[1010];
double y[1010];
double a[1010][2];

int cmp(const void * a, const void * b)
{
    if( ((double*)a)[0] < ((double*)b)[0] )return -1;
    if( ((double*)a)[0] > ((double*)b)[0] )return 1;
    if( ((double*)a)[1] < ((double*)b)[1] )return -1;
    if( ((double*)a)[1] > ((double*)b)[1] )return 1;
    return 0;
}

int main()
{

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for(int ti = 1; ti <= tc; ti++)
    {
        int n;
        int w,h;
        scanf("%d%d%d", &n,&w,&h);
        for(int i = 0; i < n; i++)
            scanf("%d", &r[i]);
        for(int i = 0; i < n; i++)
        {
            double lft = 0, rht = w;
            while(rht-lft > 1e-8)
            {
                double m = (lft+rht)/2;
                int xxx = 0;
                for(int j = 0; j < i; j++)
                {
                    if( (r[i]+r[j]+0.01)*(r[i]+r[j]+0.01)-(m-x[j])*(m-x[j]) > 0 )
                    {
                        double xx = sqrt( (r[i]+r[j]+0.01)*(r[i]+r[j]+0.01)-(m-x[j])*(m-x[j]) );
                        a[xxx][0] = y[j]-xx;
                        a[xxx][1] = y[j]+xx;
                        xxx++;
                    }
                }
                qsort(a,xxx,sizeof(a[0]),cmp);
                double up = 0;
                for(int j = 0; j < xxx; j++)
                {
                    if(up < a[j][0])
                    {
                        break;
                    }
                    else
                    {
                        if(a[j][1]>up)up = a[j][1];
                    }
                }
                if(up > h)
                {
                    lft = m+0.00001;
                }
                else rht = m;
            }
            double m = rht;
            int xxx = 0;
            for(int j = 0; j < i; j++)
            {
                if( (r[i]+r[j]+0.01)*(r[i]+r[j]+0.01)-(m-x[j])*(m-x[j]) > 0 )
                {
                    double xx = sqrt( (r[i]+r[j]+0.01)*(r[i]+r[j]+0.01)-(m-x[j])*(m-x[j]) );
                    a[xxx][0] = y[j]-xx;
                    a[xxx][1] = y[j]+xx;
                    xxx++;
                }
            }
            qsort(a,xxx,sizeof(a[0]),cmp);
            double up = 0;
            for(int j = 0; j < xxx; j++)
            {
                if(up < a[j][0])
                {
                    break;
                }
                else
                {
                    if(a[j][1]>up)up = a[j][1];
                }
            }
            x[i] = m;
            y[i] = up;
        }
        printf("Case #%d:", ti);
        for(int i = 0; i < n; i++)
        printf(" %lf %lf",x[i],y[i]);
        printf("\n");
    }

    return 0;
}
