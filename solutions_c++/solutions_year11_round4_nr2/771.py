#include <iostream>
#include <stdio.h>
#include <string>
#include <cmath>
#define EPS 1e-10

using namespace std;

int main()
{
    freopen("input.txt","rt",stdin);
    freopen("output.txt","wt",stdout);
    int t;
    cin>>t;
    for(int test_case=0;test_case<t;test_case++)
    {
        int r,c,d;
        cin>>r>>c>>d;
        double a[500][500];
        for(int i=0;i<r;i++)
        {
            string s;
            cin>>s;
            for(int j=0;j<c;j++)
                a[i][j]=s[j]-'0'+d;
        }/*
        int k=0;
        for(int i=1;i<r;i++)
            for(int j=1;j<c;j++)
            {
                int max_k=min(min(min(i,j),r-i-1),c-i-1);
                max_k=max_k2+1;
                double sx=0,double sy=0;
                for(int h=3;h<max_k;h+=2)
                {
                    for(int dx=0;dx++;dx<h/2+1)
                    {
                        sx+=(double(dx))*a[i+dx][j-h/2+dx];
                        sy-=(double(dx))*a[i+dx][j-h/2+dx];
                    }
                    for(int dx=1;dx++;dx<h/2+1)
                    {
                        sx+=(double(dx))*a[i+h/2+dx][j+dx];
                        sy+=(double(dx))*a[i+h/2+dx][j+dx];
                    }
                    for(int dx=1;dx++;dx<h/2+1)
                    {
                        sx-=(double(dx))*a[i-dx][j+h/2-dx];
                        sy+=(double(dx))*a[i+dx][j+h/2-dx];
                    }
                    for(int dx=1;dx++;dx<h/2)
                    {
                        sx-=(double(dx))*a[i-h/2+dx][j-dx];
                        sy-=(double(dx))*a[i-h/2+dx][j-dx];
                    }
                    if(sx<EPS&&sy<EPS&&h>k)k=h;

                }
            }
        for(int i=1;i<r;i++)
            for(int j=1;j<c;j++)
            {
                int max_k=min(min(min(i,j),r-i-1),c-i-1);
                max_k=max_k2+1;
                double sx=0,double sy=0;
                for(int h=3;h<max_k;h+=2)
                {
                    for(int dx=0;dx++;dx<h/2+1)
                    {
                        sx+=(double(dx))*a[i+dx][j-h/2+dx];
                        sy-=(double(dx))*a[i+dx][j-h/2+dx];
                    }
                    for(int dx=1;dx++;dx<h/2+1)
                    {
                        sx+=(double(dx))*a[i+h/2+dx][j+dx];
                        sy+=(double(dx))*a[i+h/2+dx][j+dx];
                    }
                    for(int dx=1;dx++;dx<h/2+1)
                    {
                        sx-=(double(dx))*a[i-dx][j+h/2-dx];
                        sy+=(double(dx))*a[i+dx][j+h/2-dx];
                    }
                    for(int dx=1;dx++;dx<h/2)
                    {
                        sx-=(double(dx))*a[i-h/2+dx][j-dx];
                        sy-=(double(dx))*a[i-h/2+dx][j-dx];
                    }
                    if(sx<EPS&&sy<EPS&&h>k)k=h;

                }
            }*/
        int k=min(c,r);
        for(;k>=3;k--)
        {
            bool found=false;
            for(int i=0;i<=r-k;i++)
            {

                for(int j=0;j<=c-k;j++)
                {
                    double sx=0,sy=0;
                    for(int dx=0;dx<k;dx++)
                        for(int dy=0;dy<k;dy++)
                        {
                            if(dx==0&&dy==0||dx==0&&dy==k-1||dx==k-1&&dy==0||dx==k-1&&dy==k-1)
                            {
                                continue;
                            }
                            sx+=(double(dx)+0.5-double(k)/2.0)*a[i+dx][j+dy];
                            sy+=(double(dy)+0.5-double(k)/2.0)*a[i+dx][j+dy];
                        }
                    if(abs(sx)<EPS&&abs(sy)<EPS)
                    {
                        found=true;
                        break;
                    }
                }
                if(found)break;
            }
            if(found)break;
        }
        cout<<"Case #"<<test_case+1<<": ";
        if(k>=3)cout<<k<<endl;else cout<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}
