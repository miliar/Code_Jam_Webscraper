/* 
 * File:   main.cpp
 * Author: Mi
 *
 * Created on 2011年5月22日, 上午12:14
 */

#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <map>
#include <vector>
#include <stdlib.h>
#include <iomanip>
#include <iostream>
using namespace std;

/*
 * 
 */
char str[105][105];
double wp[105],owp[105],oowp[105],rpi[105];
int main(int argc, char** argv) 
{
        freopen("A-large.in","r",stdin);
        freopen("A-large.out","w",stdout);
        int t,n,Case=1;
        scanf("%d",&t);
        while(t--)
        {
                scanf("%d",&n);
                for(int i=0;i<n;i++)
                {
                        double w=0,z=0;
                        scanf("%s",str[i]);
                        for(int j=0;j<n;j++)
                        {
                                if(str[i][j]!='.')
                                        z++;
                                if(str[i][j]=='1')
                                        w++;
                        }
                        wp[i]=w/z;
                }
                for(int i=0;i<n;i++)
                {
                        double cnt=0;
                        owp[i]=0;
                        for(int j=0;j<n;j++)
                        {                        
                                if(str[i][j]!='.')
                                        cnt++;
                                double w=0,z=0;
                                if(i==j)
                                        continue;
                                if(str[i][j]=='.')
                                        continue;
                                for(int k=0;k<n;k++)
                                        if(i==k)
                                                continue;
                                        else
                                        {
                                                if(str[j][k]=='.')
                                                        continue;
                                                if(str[j][k]!='.')
                                                        z++;
                                                if(str[j][k]=='1')
                                                        w++;
                                        }
                           //     printf("%lf %lf\n",w,z);
                                owp[i]+=(w/z);
                        }
                        owp[i]/=cnt;
                }
                for(int i=0;i<n;i++)
                {
                        double cnt=0;
                        oowp[i]=0;
                        for(int j=0;j<n;j++)
                        {
                                if(i==j)
                                        continue;
                                if(str[i][j]=='.')
                                        continue;
                                if(str[i][j]!='.')
                                        cnt++;
                                oowp[i]+=owp[j];
                        }
                        oowp[i]/=(double)cnt;
                }
                for(int i=0;i<n;i++)
                        rpi[i]=0.25*wp[i]+0.50*owp[i]+0.25*oowp[i];
                printf("Case #%d:\n",Case++);
                for(int i=0;i<n;i++)
                        //cout<<fixed<<setprecision(12)<<rpi[i]<<endl;
                        printf("%f\n",rpi[i]);
        }
        return 0;
}

