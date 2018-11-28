/* 
 * File:   main.cpp
 * Author: perpetuity
 *
 * Created on 2011年5月22日, 上午12:16
 */

#include <cstdlib>
#include<cstdio>
#include<iostream>

using namespace std;

char table[101][101];
int cnt[101];
double wp[101],owp[101],oowp[101],rpi[101];
/*
 * 
 */
int main(int argc, char** argv) {
    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++){
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%s",table[i]);
        for(int i=0;i<n;i++){
            int wcnt=0,lcnt=0;
            for(int j=0;j<n;j++){
                if(table[i][j]=='1'){
                    wcnt++;
                }
                else if(table[i][j]=='0'){
                    lcnt++;
                }
            }
            cnt[i]=wcnt+lcnt;
            wp[i]=wcnt/(double)(wcnt+lcnt);
        }
        for(int i=0;i<n;i++){
            double sum=0;
            for(int j=0;j<n;j++){
                if(table[i][j]=='1'){
                    sum+=(wp[j]*cnt[j])/(cnt[j]-1);
                }
                else if(table[i][j]=='0'){
                    sum+=(wp[j]*cnt[j]-1)/(cnt[j]-1);
                }
            }
            owp[i]=sum/cnt[i];
        }
        for(int i=0;i<n;i++){
            double sum=0;
            for(int j=0;j<n;j++){
                if(table[i][j]=='1'||table[i][j]=='0'){
                    sum+=owp[j];
                }
            }
            oowp[i]=sum/cnt[i];
        }
        printf("Case #%d:\n",cas);
        for(int i=0;i<n;i++){
            rpi[i]=0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
            //printf("%f %f %f\n",wp[i],owp[i],oowp[i]);
            cout<<rpi[i]<<endl;
        }
    }
    return 0;
}

