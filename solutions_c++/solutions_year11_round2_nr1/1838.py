#include<cstdio>
#include<iostream>
#include<memory.h>

using namespace std;

int rpi(int);

int main()
{
    int T;
    cin >>T;
    for (int num=1; num<=T; ++num)
        rpi(num);
    return 0;
}

int rpi(int num)
{
    int n,i,j;
    cin >>n;
    char ch;
    ch = getchar();
    int a[101][101];
    memset(a,0,sizeof(a));
    for (i=0; i<n; i++)
    {
        for (j=0; j<n; j++)
        {
            ch = getchar();
            if (ch=='.')
                a[i][j]=-1;
            else
                a[i][j]=(int)ch-int('0');
        }
        ch = getchar();
    }

    //wp
    double wp[101],owp[101],oowp[101];
    for (i=0; i<n; i++)
    {
        double sum = 0.;
        int count = 0;
        for (j=0; j<n; j++)
            if (a[i][j]>=0)
            {
                sum += a[i][j];
                count++;
            }
        wp[i] = sum / count;
    }

    //owp
    
    int k;
    for (j=0; j<n; j++)
    {
        double x = 0.;
        int m = 0;
        for (i=0; i<n; i++)
            if (a[i][j]>=0)
            {
                double sum = 0.;
                int count=0;
                for (k=0; k<n; k++)
                    if (a[i][k]>=0 && k!=j)
                    {
                        count++;
                        sum += a[i][k];
                    }
                x += sum / count;
                m++;
            }
        owp[j] = x / m;
    }
    
    /*
    int k;
    double temp[101];
    memset(temp,0,sizeof(temp));
    for (j=0; j<n; j++)
    {
        for (i=0; i<n; i++)
        {
            double sum=0.;
            int count=0;
            for (k=0; k<n && k!=j; k++)
                if (a[i][k]>=0)
                {
                    sum+=a[i][k];
                    count++;
                }
            temp[i]=sum/count;
        }
            double sum=0.;
            int count=0;
        for (i=0; i<n; i++)
        {
                if (a[i][j]>=0)
                {
                    sum+=temp[j];
                    count++;
                }
        }
        owp[j] = sum / count;
    }
    */

    //oowp
    for (i=0; i<n; i++)
    {
        double sum=0.;
        int count=0;
        for (j=0; j<n; j++)
            if (a[i][j]>=0)
            {
                sum+=owp[j];
                count++;
            }
        oowp[i] = sum / count;
    }
/*
    cout <<"wp\n";
    for (i=0; i<n; i++)
        cout <<wp[i] <<endl;
    cout <<"owp\n";
    for (i=0; i<n; i++)
        cout <<owp[i] <<endl;
    cout <<"oowp\n";
    for (i=0; i<n; i++)
        cout <<oowp[i] <<endl;
*/
    printf("Case #%d:\n",num);
    double ans;
    for (i=0; i<n; i++)
    {
        ans = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
        printf("%lf\n",ans);
    }
    return 0;
}

