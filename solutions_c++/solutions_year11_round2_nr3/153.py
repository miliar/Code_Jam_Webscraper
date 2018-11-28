#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <complex>
#include <vector>
using namespace std;

const double PI = acos(-1.0);
const double EPS = 1e-7;

#define SIZE(X) ((int)((X).size()))
#define PB push_back

typedef complex<double> Point;
typedef complex<double> Vector;
#define x real()
#define y imag()

typedef vector<Point> Convex;

inline double Cross(const Vector &A, const Vector &B) {
    return A.x * B.y - A.y * B.x;
}
inline double Fabs(const double a) {
    return a >= 0.00 ? a : a * -1.00;
}
inline int Cmp(const double a, const double b) {
    if ( Fabs(a - b) < EPS ) return 0;
    else return a < b ? -1 : 1;
}
bool operator==(const Point &A, const Point &B) {
    return Cmp(A.x, B.x) == 0 && Cmp(A.y, B.y) == 0;
}

const double r = 1000.0;

int N, M, C;
int clr[15];
Point pp[15];
int st[15], ed[15];

vector<Convex> lst;
bool get_ans;

bool check() {
    vector<Convex>::iterator it;
    Convex::iterator itt;
    int i;

    for (it = lst.begin(); it != lst.end(); ++it) {
        vector<bool> app(C, false);
        for (itt = it->begin(); itt != it->end(); ++itt) {
            for (i = 0; i < N; i++) {
                if (*itt == pp[i]) break;
            }
            //cerr << i << " ";
            app[clr[i]] = true;
        }
        //cerr << "|" << endl;
        for (i = 0; i < C; i++) {
            if (!app[i]) return false;
        }
    }
    return true;
}

void go(int dep, int prev) {
    if (dep == N) {
        for (int i = dep; i < N; i++) {
            clr[i] = C - 1;
        }
        int c[15];
        for (int i = 0; i < N; i++) {
            c[i] = clr[i];
        }
        /*
        for (int i = 0; i < N; i++) {
            cerr << clr[i] << " ";
        }
        cerr << endl;
        */
        do {
            if (check()) { get_ans = true; break; }
        } while (next_permutation(clr, clr + N));
        if (get_ans) return;
        for (int i = 0; i < N; i++) {
            clr[i] = c[i];
        }
        return;
    }
    for (int i = prev; i < C; i++) {
        clr[dep] = i;
        go(dep + 1, i);
        if (get_ans) return;
    }
}

int main() {
    int t, casN;
    int i, j;

    scanf("%d", &t);
    for (casN = 1; casN <= t; casN++) {
        scanf("%d%d", &N, &M);
        Convex ini = Convex();
        lst = vector<Convex>();
        for (i = 0; i < N; i++) {
            pp[i] = Point(r * cos((2.0*PI*i) / N), r * sin((2.0*PI*i) / N));
            ini.PB(pp[i]);
        }
        lst.PB(ini);
        for (i = 0; i < M; i++) {
            scanf("%d", &st[i]);
            st[i]--;
        }
        for (i = 0; i < M; i++) {
            scanf("%d", &ed[i]);
            ed[i]--;
            vector<Convex> new_lst = vector<Convex>();
            for (vector<Convex>::iterator it = lst.begin(); it != lst.end(); ++it) {
                Convex a = Convex(), b = Convex();
                for (Convex::iterator itt = it->begin(); itt != it->end(); ++itt) {
                    if (Cmp(Cross(pp[st[i]] - *itt, pp[ed[i]] - *itt), 0.0) < 0) a.PB(*itt);
                    else if (Cmp(Cross(pp[st[i]] - *itt, pp[ed[i]] - *itt), 0.0) > 0) b.PB(*itt);
                }
                if (SIZE(a) == 0 || SIZE(b) == 0) new_lst.PB(*it);
                else {
                    if (SIZE(a) > 0) {
                        a.PB(pp[st[i]]);
                        a.PB(pp[ed[i]]);
                        new_lst.PB(a);
                    }
                    if (SIZE(b) > 0) {
                        b.PB(pp[st[i]]);
                        b.PB(pp[ed[i]]);
                        new_lst.PB(b);
                    }
                }
            }
            lst = new_lst;
            //cerr << "XD" << SIZE(lst) << endl;
        }
        /*
        for (vector<Convex>::iterator it = lst.begin(); it != lst.end(); ++it) {
            for (Convex::iterator itt = it->begin(); itt != it->end(); ++itt) {
                cerr << *itt << " ";
            }
            cerr << endl;
        }
        */
        int sml = N;
        for (vector<Convex>::iterator it = lst.begin(); it != lst.end(); ++it) {
            sml = min(sml, SIZE(*it));
        }
        for (i = sml; i >= 2; i--) {
            C = i;
            get_ans = false;
            go(0, 0);
            if (get_ans) break;
        }
        printf("Case #%d: %d\n", casN, i);
        for (i = 0; i < N; i++) {
            printf("%d%c", clr[i] + 1, i == N-1 ? '\n' : ' ');
        }
    }

    return 0;
}

