#include <iostream>
#include <algorithm>
#include <deque>
using namespace std;

struct SCH
{
    int dp;
    int ar;
};

bool operator < (SCH a, SCH b)
{
    return a.dp < b.dp;
}

int main()
{
    int N;
    scanf("%d",&N);
    int c = 0;
    while( c < N ) {
        int T,NA,NB;
        scanf("%d %d %d",&T,&NA,&NB);
        int i;
        deque<SCH> TA;
        deque<SCH> TB;
        for( i = 0; i < NA; i++ ) {
            int a,b,c,d;
            scanf("%d:%d %d:%d",&a,&b,&c,&d);
            SCH tmp;
            tmp.dp = a*100+b;
            tmp.ar = c*100+d;
            TA.push_front(tmp); 
        }
        for( i = 0; i < NB; i++ ) {
            int a,b,c,d;
            scanf("%d:%d %d:%d",&a,&b,&c,&d);
            SCH tmp;
            tmp.dp = a*100+b;
            tmp.ar = c*100+d;
            TB.push_front(tmp); 
        }
        sort(TA.begin(),TA.end());
        sort(TB.begin(),TB.end());
        deque<int> trA,trB;
        int h = 0,m = 0;
        int ra = 0, rb = 0;
        while( h*100+m < 2400 ) {
           int tt = h*100+m;
           while( TA.size() > 0 && tt == TA[0].dp ) {
              if( trA.size() == 0 || trA[0] > tt ) {
                  ra++;
              }
              else {
                  trA.pop_front();
              }
              int tm = TA[0].ar%100;
              int th = TA[0].ar/100;
              tm += T;
              int at = (th+tm/60)*100+tm%60;
              trB.push_back(at);
              TA.pop_front();
           }
           sort(trB.begin(),trB.end());
           while( TB.size() > 0 && tt == TB[0].dp ) {
              if( trB.size() == 0 || trB[0] > tt ) {
                  rb++;
              }
              else {
                  trB.pop_front();
              }
              int tm = TB[0].ar%100;
              int th = TB[0].ar/100;
              tm += T;
              int at = (th+tm/60)*100+tm%60;
              trA.push_back(at);
              TB.pop_front();
           }
           sort(trA.begin(),trA.end());
           m++;
           if( m == 60 ) {
              h++;
              m = 0;
           }
        }
        printf("Case #%d: %d %d\n",c+1,ra,rb);
        c++;
    }
    return 0;
}
