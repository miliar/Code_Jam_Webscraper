// Gcodejam.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include<cstdio>
#include<map>
#include<vector>
#include<string>

#define REP(i,n) for(int i=0;i<(int)(n);++i)
using namespace std;
int h[1001][101];
int main() {
    int n;
    char p[200];
    gets(p);
    sscanf(p,"%d",&n);
    REP(xxx,n) {
        int s,q;
        map<string,int> Sengines;
        vector<int> Qs;
        gets(p);
        sscanf(p,"%d",&s);
        REP(i,s) {
            gets(p);
            Sengines[p]=i;
        }
        gets(p);
        sscanf(p,"%d",&q);
        REP(i,q) {
            gets(p);
            Qs.push_back(Sengines[p]);
        }

        for(int i=q-1;i>=0;--i){
            REP(j,s) {
                if(Qs[i]!=j)  {
                     h[i][j]=i+1<q?h[i+1][j]:0;
                } else {
                    int tmp=0;
                    if(i+1<q) {
                        tmp=h[i+1][0];
						if(j==0) tmp=h[i+1][1];
                        REP(k,s) if(k!=j &&  h[i+1][k]<tmp ) tmp=h[i+1][k];
                    }
                    h[i][j] = 1+ tmp;
                }
            }
        }
       printf("Case #%d: ",xxx+1);
        if(q==0) printf("0\n"); else {
            int tmp=h[0][0];
            REP(i,s) if(tmp>h[0][i]) tmp=h[0][i];
            printf("%d\n",tmp);
        }
		/*
        printf("Debug:\n");
        REP(i,s) {
            REP(j,q) printf("%2d",h[j][i]);
            printf("\n");
        }*/

    } //end case
}


