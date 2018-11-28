// Gcodejam.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include<cstdio>
#include<algorithm>
#include<queue>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)(n);++i)
int rt() {
    int a,b;
    scanf("%d:%d",&a,&b);
    return a*60+b;
}
int main() {
    int n;
    scanf("%d",&n);

    REP(xxx,n) {
        priority_queue< pair<int,pair<int,int > > > Q;
        int res[2]={0,0};
        int stav[2]={0,0};
        int T;
        scanf("%d",&T);
        int nb,na;
        scanf("%d %d",&na,&nb);
        REP(i,na) {
            int x=rt();
            int y=rt();
            Q.push(make_pair(-x ,make_pair(-1,0)));
            Q.push(make_pair(-y-T ,make_pair(1,1)));
        }
        REP(i,nb) {
            int x=rt();
            int y=rt();
            Q.push(make_pair(-x ,make_pair(-1,1)));
            Q.push(make_pair(-y-T ,make_pair(1,0)));
        }
        while(!Q.empty()) {
            pair<int,int> e=Q.top().second;
            Q.pop();
            stav[e.second]+=e.first;
            if(stav[e.second]<0) {res[e.second]++;stav[e.second]++;}
        }

    printf("Case #%d: %d %d\n",xxx+1,res[0],res[1]);
    }// end case


}
