#include <stdio.h>
#include <set>
#pragma optimize("O2",on)
using namespace std;

multiset<pair<int,int> > A[2];

int main (){
#ifndef ONLINE_JUDGE
	//freopen( "input.txt", "r", stdin);
	freopen( "B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
#endif
    int n; scanf("%d",&n);
    for (int o=1; o<=n; o++) {
        int t,na,nb;
        scanf("%d%d%d",&t,&na,&nb);
        A[0].clear(); A[1].clear();
        for (int i=0; i<na; i++) {
            int h1,m1,h2,m2,t1,t2;
            scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
            t1=60*h1+m1; t2=60*h2+m2;
            A[0].insert(make_pair(t1,t2));
        }
        for (int i=0; i<nb; i++) {
            int h1,m1,h2,m2,t1,t2;
            scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
            t1=60*h1+m1; t2=60*h2+m2;
            A[1].insert(make_pair(t1,t2));
        }
        int rA=0,rB=0, last=-10000, c=0; bool f;
        if (!A[0].empty() || !A[1].empty()) {
            multiset<pair<int,int> >::iterator it;
            if (A[0].empty() || (!A[1].empty() && A[1].begin()->first<A[0].begin()->first))
                c=1; else c=0;
            while (!A[0].empty() || !A[1].empty()) {
                if (last==-10000) { if (c==0) rA++; else rB++; };
                f=false;
                for (it=A[c].begin(); it!=A[c].end(); it++)
                    if (it->first>=last) {
                        last=it->second+t;
                        A[c].erase(it);
                        c=1-c;
                        f=true;
                        break;
                    }
                if (!f) {
                    last=-10000; 
                    if (A[0].empty() || (!A[1].empty() && A[1].begin()->first<A[0].begin()->first))
                        c=1; else c=0;
                }
            }
        }
        printf("Case #%d: %d %d\n",o,rA,rB);
    }
	return 0;
}