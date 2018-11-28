#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cstring>
using namespace std;

#define hh first
#define mm second
struct TRAIN {
        bool f;
        pair<int, int> departure, arrive;
};

class COMP {
        public:
                bool operator() (const TRAIN& r1, const TRAIN& r2) const {
                        if(r1.departure.hh==r2.departure.hh)
                                return r1.departure.mm < r2.departure.mm;

                        return r1.departure.hh < r2.departure.hh;
                }
};

bool comp(TRAIN r1, TRAIN r2) {
        if(r1.departure.hh==r2.departure.hh)
                return r1.departure.mm < r2.departure.mm;
        return r1.departure.hh < r2.departure.hh;
}

#define ATOI(x) atoi(x.c_str());

int main() {
        int CASE,tt,i;
        int T,A,B,a,b;
        TRAIN train;
        string s1,s2;

        cin >> CASE;
//      CASE=1;
        for(tt=1;CASE--;tt++) {
                multiset<TRAIN,COMP> ss,aa,bb;

                cin >> T;
                cin >> A >> B;
                for(i=0;i<A+B;i++) {
                        cin >> s1 >> s2;
                        if(i<A) train.f=true; else train.f=false;
                        train.departure.hh = ATOI(s1.substr(0,2));
                        train.departure.mm = ATOI(s1.substr(3));
                        train.arrive.hh = ATOI(s2.substr(0,2));
                        train.arrive.mm = ATOI(s2.substr(3));
                        ss.insert(train);
                }

                set<TRAIN,COMP>::iterator it,pos;
                TRAIN tmp;
                int sa=0, sb=0;
                for(it=ss.begin();it!=ss.end();++it) {
                        tmp = *it;
                        tmp.departure = tmp.arrive;
/*
printf("[GET] %c %d:%d %d:%d\n", it->f ? 'A' :'B',
        it->departure.hh, it->departure.mm,
        it->arrive.hh, it->arrive.mm);
printf("[AA] ");
for(set<TRAIN,COMP>::iterator aaa=aa.begin();aaa!=aa.end();++aaa) {
        printf("%d:%d ", aaa->departure.hh, aaa->departure.mm);
}
printf("\n[BB] ");
for(set<TRAIN,COMP>::iterator aaa=bb.begin();aaa!=bb.end();++aaa) {
        printf("%d:%d ", aaa->departure.hh, aaa->departure.mm);
}
puts("");
*/
                        if(it->f) { // begin A
                                pos = aa.begin();
                                if(pos==aa.end() || comp(*it, *pos)) {
//                                      puts("A++");
                                        sa++;
                                } else aa.erase(pos);

                                tmp.departure.mm+=T;
                                if(tmp.departure.mm>=60) {
                                        tmp.departure.hh++;
                                        tmp.departure.mm-=60;
                                }
                                if(tmp.departure.hh<24) bb.insert(tmp);
                        } else {        // begin B
                                pos = bb.begin();
                                if(pos==bb.end() || comp(*it, *pos)) {
//                                      puts("B++");
                                        sb++;
                                } else bb.erase(pos);

                                tmp.departure.mm+=T;
                                if(tmp.departure.mm>=60) {
                                        tmp.departure.hh++;
                                        tmp.departure.mm-=60;
                                }
                                if(tmp.departure.hh<24) aa.insert(tmp);

                        }
                }

                printf("Case #%d: %d %d\n", tt,sa,sb);
        }

        return 0;
}