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

char B[52][52], C[52][52];
bool checkWin(char who, int n, int k) {
    fi(y,n) {
        fi(x, n) {
            bool win=true;
            fi(i, k) {
                if(y + i >= n || C[y+i][x] != who) {
                    win = false;
                    break;
                }
            }
            if(win) return true;

            win=true;
            fi(i, k) {
                if(x + i >= n || C[y][x+i] != who) {
                    win = false;
                    break;
                }
            }
            if(win) return true;

            win=true;
            fi(i, k) {
                if(x + i >= n || y + i >= n || C[y+i][x+i] != who) {
                    win = false;
                    break;
                }
            }
            if(win) return true;

            win=true;
            fi(i, k) {
                if(x - i >= n || y + i >= n || C[y+i][x-i] != who) {
                    win = false;
                    break;
                }
            }
            if(win) return true;
        }
    }
    return false;
}

void solve(int t) {
    int n = ri(), k=ri();
    SET(B, '.');
    SET(C, '.');
    fi(i, n)
        scanf(" %s ", B[i]);

    fi(y, n) {
        int ci = n-1;
        fd(x, n-1, 0)
            if(B[y][x] != '.') {
                C[y][ci] = B[y][x];
                ci--;
            }
    }
    printf("Case #%d: ", t);
    bool BWin = checkWin('B', n, k),
         RWin = checkWin('R', n, k);
    if(BWin && RWin)
        printf("Both\n");
    else if(BWin)
        printf("Blue\n");
    else if(RWin)
        printf("Red\n");
    else
        printf("Neither\n");
}

int main(){
    fi(t,ri()) solve(t+1);
    return 0;
}

