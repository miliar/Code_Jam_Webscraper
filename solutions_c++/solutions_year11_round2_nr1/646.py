#include<stdio.h>
#include<iostream>
using namespace std;
#define LL long long
char mp[200][200];
double all[200];
int awin[200];
double wp[200];
double owp[200];
double ans[200];
double oowp[200];
int main()
    {
        freopen("al.in","r",stdin);
        freopen("a.out","w",stdout);
        int T;
        scanf("%d",&T);

        for(int ii = 1 ;ii <=T;ii++)
            {
                printf("Case #%d:\n",ii);
                int  n ;
                scanf("%d",&n);
                getchar();
                for(int i = 0 ; i< n ;i++)
                    gets(mp[i]);
                for(int i = 0 ; i < n ;i++)
                    {
                        double tall = 0;
                        int win = 0;
                        for(int j = 0 ; j < n ; j++)
                            {
                            if(mp[i][j] != '.')
                                tall+=1.0;
                            if(mp[i][j] == '1')
                                win++;
                            }
                        wp[i] = (double)win/tall;
                        awin[i] = win;
                        all[i] = tall;
                    }
                for(int i = 0 ; i < n ; i++)
                    {
                        double sum = 0.0;
                        for(int j = 0 ; j < n;j++)
                            if(mp[i][j] != '.')
                                {
                                    if(mp[i][j] == '0')
                                        sum += (double)(awin[j]-1.0)/(all[j]-1.0);
                                    if(mp[i][j ] == '1')
                                        sum += (double)(awin[j]) /(all[j] -1.0);
                                }
                        owp[i] = sum/all[i];
                    }
                for(int i = 0 ; i < n ; i++)
                    {
                        double sum = 0.0;
                        for(int j = 0 ; j < n;j++)
                            if(mp[i][j] != '.')
                                sum += owp[j];
                        oowp[i] = sum/all[i];
                    }
                for(int i = 0 ; i < n ; i++)
                    {
                        ans[i] =   0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
                        printf("%.12f\n" , ans[i]);
                    }
            }
        return 0;
    }
