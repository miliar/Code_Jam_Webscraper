#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;
typedef pair<int,int> PI;
#define REP(i,n)	for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,s,k)	for(int i=(s),_k=(k);i<=_k;++i)
#define FORD(i,s,k)	for(int i=(s),_k=(k);i>=_k;--i)
#define FORE(it,q)	for(__typeof((q).begin())it=(q).begin();it!=(q).end();++it)


int main()
{
	int TT;
	int N, NA, NB,T;
	int h1,m1,h2,m2;
	vector<PI> A[2];
	scanf("%d",&TT);
	FOR(cs,1,TT) {
        A[0].clear();
        A[1].clear();
        scanf("%d%d%d\n",&T,&NA,&NB);
        REP(i,NA) {
            scanf("%d:%d %d:%d\n", &h1, &m1, &h2, &m2);
            m1 += 60*h1;
            m2 += 60*h2;
            A[0].push_back(PI(m1,m2));
        }
        REP(i,NB) {
            scanf("%d:%d %d:%d\n", &h1, &m1, &h2, &m2);
            m1 += 60*h1;
            m2 += 60*h2;
            A[1].push_back(PI(m1,m2));
        }
        REP(i,2) sort(A[i].begin(),A[i].end());
        int resA = 0, resB = 0;
        while(!A[0].empty() || !A[1].empty()) {
            int cur = 0;
            if(!A[0].empty() && !A[1].empty()) {
                if(A[0][0].first <= A[1][0].first)
                    cur = 0;
                else 
                    cur = 1;
            } else if(!A[0].empty()) cur = 0;
            else cur = 1;
            if(!cur) ++resA; else ++resB;
            int ct = -T;
            vector<PI>::iterator itor;
            do {
                itor = A[cur].end();
                FORE(it,A[cur])
                    if(it->first >= ct+T) {
                        itor = it;         
                        break;
                    }               
                if(itor != A[cur].end()) {
                    ct = itor->second;
                    A[cur].erase(itor);
                    cur = !cur;
                } else 
                    break;
            } while(1);
        }
        printf("Case #%d: %d %d\n", cs, resA, resB);
    }
}
