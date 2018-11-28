#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cfloat>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

//#define NDEBUG

#if defined(NDEBUG)
#define DBG_CODE(cb...)
#else
#define DBG_CODE(cb...) cb
#endif

#define WRITE(x) DBG_CODE(cout << x << endl)
#define WATCH(x) DBG_CODE(cout << #x << "=" << x << endl)

//[a, b) incrementando
#define FORN(i, a, b) for(typeof(b) i = (a); i < (b); i++)
//(a, b] decrementando
#define FORR(i, a, b) for(typeof(a) i = (a) - 1; i >= (b) && i < (a) ; i--)

#define ALL(x) x.begin(), x.end()
#define FOREACH(i, c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define FOREACHR(i, c) for(typeof((c).rbegin()) i = (c).rbegin(); i != (c).rend(); i++)

const int MAX_N = 2000;

void inc(vector< int > &color, int k)
{
    FOREACH(i, color){
        *i += 1;
        if(*i < k) break;
        *i = 0;
    }
}

bool ok(vector< int > &color, vector< set < int > > &sala, int k)
{
    FOREACH(s, sala){
        set< int > sc;
        FOREACH(i, *s){
            sc.insert(color[*i]);
        }

        if(sc.size() < k) return false;
    }

    return true;
}


bool solve_k(int n, int k, vector< set< int > > &sala, vector< int > &resp)
{
    vector< int > color(n + 1, 0);
    while(color[n] == 0){
       if(ok(color, sala, k)){
           resp = color;
           return true;
       }
       inc(color, k);
    }

    return false;
}

int solve(vector< set< int > > &sala, int n, int min_k, vector< int > &resp)
{
    for(int k = min_k; k > 1; k--){
        if(solve_k(n, k, sala, resp)) return k;
    }

    return 1;
}

int main()
{
    int NTC;
    scanf("%d", &NTC);

    FORN(TC, 0, NTC){
        int n;
        int m;
        scanf("%d %d", &n, &m);
        vector< set< int > > sala;

        set< int > tudo;
        FORN(i, 0, n){
            tudo.insert(i);
        }
        sala.push_back(tudo);

        vector< int > U(m);
        vector< int > V(m);

        FORN(i, 0, m){
            scanf("%d", &(U[i]));
            U[i]--;
        }

        FORN(i, 0, m){
            scanf("%d", &(V[i]));
            V[i]--;
        }


        FORN(i, 0, m){
            FOREACH(it, sala){
                if((it->find(U[i]) != it->end()) and (it->find(V[i]) != it->end())){
                    /*FORN(r, min(U[i], V[i]) + 1, (int)max(U[i], V[i])){
                        it->erase(r);
                        WATCH(r);
                    }

                    set< int > nova;
                    FORN(x, min(U[i], V[i]), max(U[i], V[i]) + 1){
                        nova.insert(x);
                        WATCH(x);
                    }*/

                    set< int > a;
                    set< int > b;

                    FOREACH(x, *it){
                        if(*x < max(U[i], V[i]) and *x > min(U[i], V[i])){
                            a.insert(*x);
                        }else{
                            b.insert(*x);
                        }

                        a.insert(U[i]);
                        a.insert(V[i]);
                    }

                    *it = a;

                    sala.push_back(b);
                    break;
                }
            }

            vector< int > color(n);
        }

        int min_c = INT_MAX;
        FOREACH(i, sala){
            if(i->size() < min_c) min_c = i->size();
        }

        vector< int > resp(n);
        printf("Case #%d: %d\n", TC + 1, solve(sala, n, min_c, resp));
        printf("%d", resp[0] + 1);
        FORN(i, 1, resp.size() - 1){
            printf(" %d", resp[i] + 1);
        }
        printf("\n");
    }
}
