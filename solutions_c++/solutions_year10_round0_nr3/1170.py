#include <cstdio>
#include <iostream>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <utility>

using namespace std;
class rec {
public:
    unsigned int r;
    unsigned int v;
    unsigned int R;
};
class find_cycle {
    unsigned int k;
    unsigned int N;
    const unsigned int * g;
    unsigned int p;
    map<unsigned int, rec > s;
public:
    void set(unsigned int ik, unsigned int iN, const unsigned int * ig) {
        k = ik;
        N = iN;
        g = ig;
    };
    void inc() {
        p ++;
        if(p==N)
            p=0;
    };
    unsigned int go(unsigned int maxR) {
        p = 0;        
        unsigned int cap=0, v=0, R=0;
        s.clear();
        s[0].v = 0;
        s[0].R = 0;
        
        unsigned int pre_v, pre_R, cycle_v, cycle_R;
        for( ; ; ) {
            // get as much loaded as can
            unsigned int q = p;
            do {
                if( cap+g[p] <= k ) {
                    cap += g[p];
                    p ++;
                    if(p==N)
                        p=0;
                } else
                    break;
            } while ( p!=q );

            // take a ride!!
            R++;
            v += cap;
//            printf("Ride#%d : %d\t\ttotal income:%d\n", R, cap, v);
            cap = 0;
            if( R==maxR )
                return v;

            // check repeat
            if( s.find(p) == s.end() ) {
                // make a record
                s[p].v = v;
                s[p].R = R;
            } else {
                pre_v = s[p].v;
                pre_R = s[p].R;
                cycle_v = v - pre_v;
                cycle_R = R - pre_R;
                
                // fast predict future
                unsigned int rest_R = maxR - pre_R;
                unsigned int repeat = rest_R / cycle_R;
                // unsigned int remain = rest_R % cycle_R;
                repeat --;
                R += repeat * cycle_R;
                v += repeat * cycle_v;
//                printf("repeat last [%d] rides for [%d] times\n", cycle_R, repeat);
                break;
            }
        }
        if( R == maxR )
            return v;

        for( ; ; ) {
            // get as much loaded as can
            unsigned int q = p;
            do {
                if( cap+g[p] <= k ) {
                    cap += g[p];
                    p ++;
                    if(p==N)
                        p=0;
                } else
                    break;
            } while ( p!=q );

            // take a ride!!
            R++;
            v += cap;
//            printf("Ride#%d : %d\t\ttotal income:%d\n", R, cap, v);
            cap = 0;
            if( R==maxR )
                return v;
        }
        // pre_R : pre_v
        // (rest_R / cycle_R) * cycle_v
        // (rest_R % cycle_R) : ??
        
        //printf("%d\t%d\t%d\t%d\n", pre_v, cycle_v, pre_R, cycle_R);
/*        for( cap=0; ; ) {
            if( cap + g[p] > k ) {
                if( s.find(p) == s.end() ) {
                    R ++;
                    s[p].r = r;
                    s[p].v = v;
                    s[p].R = R;
                    cap = 0;
                    if( R == maxR ) {
                        return v;
                    }
                } else {
                    R++;
                    break;
                }
            } else {
                cap += g[p];
                v += g[p];
                p ++;
                if(p==N) {
                    p=0;
                    r++;
                }
            }
        }
        printf("from round [%d] to round [%d], pos [%d]; pre=[%d], one-round=[%d]; \n", s[p].r, r, p, s[p].v, v-s[p].v);
        printf("pre has [%d] rides, one-round has [%d] rides \n ", s[p].R, R - s[p].R);
        return 0;*/
    };
};

int main()
{
    int T;
    unsigned int g[1024];
    find_cycle f;
    
    cin >> T;

    for(int i=1; i<=T; i++) {
        unsigned int R, k, N;
        cin >> R;
        cin >> k;
        cin >> N;
        for(unsigned int j=0; j<N; j++)
            cin >> g[j];
        
        f.set(k, N, g);
        unsigned int ret = f.go(R);
        cout << "Case #" << i << ": " << ret << endl;
    }
    
    cin >> T;
    return 0;
}
