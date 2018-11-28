#include <cstdio>
#include <algorithm>
#include <map>
#include <string>
#include <vector>

#define FOR(i,a,b) for (int i=(a);i<(b);++i)
#define FORQ(i,a,b) for (int i=(a);i<=(b);++i)
#define FORE(i,x) for (__typeof__((x).begin()) i=(x).begin();i!=(x).end();++i)

#define MP make_pair
#define F first
#define S second
#define PB push_back

using namespace std;

int main() {
    int t;
    scanf("%d",&t);
    FORQ(l,1,t) {
        map<pair<char,char>, char> C;
        map<pair<char,char>, bool> P;
        FORQ(a,'A','Z')
            FORQ(b,'A','Z') {
                C[MP(a,b)] = 0;
                P[MP(a,b)] = false;
            }
        
        int c;
        scanf("%d",&c);
        FOR(i,0,c) {
            char Buf[10];
            scanf("%s",Buf);
            C[MP(Buf[0], Buf[1])] = Buf[2];
            C[MP(Buf[1], Buf[0])] = Buf[2];
        }

        int d;
        scanf("%d",&d);
        FOR(i,0,d) {
            char Buf[10];
            scanf("%s",Buf);
            P[MP(Buf[0], Buf[1])] = true;
            P[MP(Buf[1], Buf[0])] = true;
        }

        vector<char> T;
        
        int n;
        scanf("%d%*c",&n);
        FOR(i,0,n) {
            char z;
            scanf("%c",&z);

            T.PB(z);
            
            while (true) {
                if (T.size() <= 1) break;
                if (C[MP(T[T.size()-2], T[T.size()-1])] != 0) {
                    char t = C[MP(T[T.size()-2], T[T.size()-1])];
                    T.pop_back();
                    T.pop_back();
                    T.PB(t);
                    continue;
                }
                FORE(a, T)
                    FORE(b, T)
                        if (P[MP(*a, *b)]) {
                            T.clear();
                            goto Break;
                        }
Break:
                break;
            }
        }
        printf("Case #%d: [", l);
        FOR(i,0,T.size()) {
            printf(i==T.size()-1 ? "%c" : "%c, ", T[i]);
        }
        printf("]\n");
    }
    return 0;
}
