#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <stdio.h>
using namespace std;

long long nod(long long a,long long b)
{
    while(a&&b)
        if(a>b) a=a%b; else b=b%a;
    return a+b;
}

int main()
{
	int T;
	long long n,d,g;
	cin>>T;
    for(int t=1;t<=T;t++)
    {
        printf("Case #%d:\n",t);
        cin>>n;
        char a[105][105];
        double wp[105];
        double owp[105];
        double oowp[105];
       for(int i=0;i<n;i++)
          cin>>a[i];

    for(int i=0;i<n;i++)
    {
        int nn=0,ww=0;
        for(int j=0;j<n;j++)
        if(a[i][j]!='.')
        {
            nn++;
            if(a[i][j]=='1')
            ww++;
        }
        wp[i]=ww*1.0/nn;
        //cout<<i<<" "<<wp[i]<<endl;
    }

    for(int i=0;i<n;i++)
    {
        owp[i]=0;
        int cc=0;
        for(int j=0;j<n;j++)
        {
            if(a[i][j]!='.')
            {
                cc++;
                int nn=0,ww=0;
                for(int t=0;t<n;t++)
                {
                    if(t==i)
                    continue;
                    if(a[j][t]=='1')
                        ww++;
                    if(a[j][t]=='1'||a[j][t]=='0')
                    nn++;
                }
                owp[i]+=ww*1.0/nn;
            }
        }

        owp[i]/=cc;
        //cout<<i<<" "<<owp[i]<<endl;

    }
    for(int i=0;i<n;i++)
    {
        int nn=0;
        oowp[i]=0;
        for(int j=0;j<n;j++)
        {
            if(a[i][j]!='.')
            {
            oowp[i]+=owp[j];
            nn++;
            }
        }
        oowp[i]/=nn;
    }

    for(int i=0;i<n;i++)
        printf("%.12lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);

    }

	return 0;
}

