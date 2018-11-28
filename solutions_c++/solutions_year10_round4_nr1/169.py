/* All includes and defines required by the templates
 * Just add it at the beginning and all will work OOB */
#include<iostream>
#include<set>
#include<iomanip>
#include<sstream>
#include<fstream>
#include<stack>
#include<cstdio>
#include<cmath>
#include<cassert>
#include<queue>
#include<vector>
#include<list>
#include<algorithm>
#include<map>
#include<cstring>
#include<cctype>


using namespace std;
#define fe(e,C) for(__typeof((C).begin()) e = (C).begin(); e != (C).end(); e++)
#define fi(i,n) for(int i = 0, i##end = (n); i < i##end; i++)
#define ft(i,a,b) for(int i = (a), i##end = (b); i <= i##end; i++)
#define fd(i,a,b) for(int i = (a), i##end = (b); i >= i##end; i--)
#define fs(i,C) fi(i,SZ(C))
#define ALL(V) (V).begin(), (V).end()
#define SET(T, c) memset(T, c, sizeof(T))
#define VI vector<int>
#define PB push_back
#define PII pair<int, int>
#define SEC second
#define FST first
#define MP make_pair
#define SZ(C) ((int)(C).size())
#define SQR(a) ((a)*(a))
#define VII vector<PII>

typedef unsigned long long ULL;
typedef long long LL;

int ri() { int n; scanf(" %d", &n); return n; }
void pi(int n) { printf("%d\n", n); }
string rs() { char buf[10000]; buf[9999]=-1; scanf(" %s ", buf); assert(buf[9999]==-1); return buf; }
void ps(const string &s) { printf("%s\n", s.c_str()); }
template<class R, class T>
R conv(const T &t) { stringstream ss; ss << t; R r; ss >> r; return r; }
LL gcd(LL a, LL b) { if(b == 0) return a; else return gcd(b, a % b); }
struct pt { int x, y; pt(int x, int y):x(x), y(y) {} };

int M[110][110];

void symTr(int &x, int &y, int ) {
    swap(x, y);
}

void asymTr(int &x, int &y, int bs) {
    swap(x, y);
    x = bs - 1 - x;
    y = bs - 1 - y;
}

void solve(int t) {
    SET(M, '.');

    int k = ri();
    ft(sum, 0, 2*k+1) {
        ft(y, 0, sum) {
            int x = sum - y;
            if(x < k && y < k)
                M[y][x] = ri();
        }
    }

    ft(bs, k, 10000) {
        fi(oy, bs - k + 1)
            fi(ox, bs - k + 1) {
                bool found = true;
                fi(y, k)
                    fi(x, k) {
                        int nx = ox + x,
                            ny = oy + y;

                        int sx, sy;
                        int rx, ry;

                        sx = nx;
                        sy = ny;
                        symTr(sx, sy, bs);

                        rx = sx - ox;
                        ry = sy - oy;
                        if(rx >= 0 && rx < k && ry >= 0 && ry < k) {
                            if(M[y][x] != M[ry][rx]) {
                                //cout<<"war:"<<(M[y][x] != M[ry][rx])<<endl;
                                found = false;
                                goto out;
                            }
                        }

                        sx = nx;
                        sy = ny;
                        asymTr(sx, sy, bs);

                        rx = sx - ox;
                        ry = sy - oy;
                        if(rx >= 0 && rx < k && ry >= 0 && ry < k) {
                            if(M[y][x] != M[ry][rx]) {
                                //cout<<"war:"<<(M[y][x] != M[ry][rx])<<endl;
                                found = false;
                                goto out;
                            }
                        }

                        sx = nx;
                        sy = ny;
                        symTr(sx, sy, bs);
                        asymTr(sx, sy, bs);

                        rx = sx - ox;
                        ry = sy - oy;
                        if(rx >= 0 && rx < k && ry >= 0 && ry < k) {
                            if(M[y][x] != M[ry][rx]) {
                                //cout<<"war:"<<(M[y][x] != M[ry][rx])<<endl;
                                found = false;
                                goto out;
                            }
                        }
                    }
out:;
                if(found) {
                    printf("Case #%d: %d\n", t, bs*bs-k*k);
                    return;
                }
            }
    }
    assert(false);
}

int main(){
    fi(t,ri()) solve(t+1);
    return 0;
}

