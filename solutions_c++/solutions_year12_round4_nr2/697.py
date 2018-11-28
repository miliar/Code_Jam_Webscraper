#include<algorithm>
#include<math.h>
#include<time.h>
#include<iostream>
#include<fstream>
#include<stdio.h>
#include<string.h>
#include<string>
#include<stdlib.h>

using namespace std;
int lll,jj;
double aa[20],bb[20];
int n,t;
int hh,li,ss,jut;
double ssr[2000];

double dis(int i,int j);
int search();

int main()
{
    srand(unsigned(time(0)));
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    cin>>t;
    for ( ss = 1; ss <= t; ++ss)
    {
        cin >> n >> hh >> li;
        jut = 0;
        for ( lll = 1; lll <= n; ++lll )
            cin>>ssr[lll];
        for ( lll = 1; lll <= 10000; ++lll )
        if ( jut == 0 )
            search();
    }
    return 0;
}

double dis(int i,int j)
{
    return  ( aa[i] - aa[j] ) * ( aa[i] - aa[j] ) + ( bb[i] - bb[j] ) * ( bb[i] - bb[j] );
}


int search()
{
    int i,j;
    aa[1]=0; bb[1]=0;
    for ( i = 2; i <= n; ++i )
    {
        for ( j = 1; j <= 1000; ++j )
        {
            int tiao = rand()%628;
            double ta = tiao/100.0;
            int temp;
            temp = rand()%i;
            while ( temp == 0 )
                  temp=rand()%i;
            double rr = sqrt( ( ssr[i] + ssr[temp] ) * ( ssr[i] + ssr[temp] ) ) + 0.1;
            aa[i] = aa[temp] + rr*cos(ta);
            bb[i] = bb[temp] + rr*sin(ta);
            if ( aa[i] < 0 || aa[i] > hh )
                  continue;
            if ( bb[i] < 0 || bb[i] > li ) continue;
            for ( jj = 1; jj < i; ++jj )
                if ( dis(jj,i) < ( ssr[i] + ssr[jj] ) * ( ssr[i] + ssr[jj]) )
                    break;
            if ( jj == i ) break;
        }
        if ( j == 1001 )  break;
    }
    if (i==n+1)
    {
        printf("Case #%d:",ss);
         jut = 1;
        for ( i = 1; i <= n;++i )
            printf(" %.6lf %.6lf",aa[i],bb[i]);
        cout<<endl;
    }
}
