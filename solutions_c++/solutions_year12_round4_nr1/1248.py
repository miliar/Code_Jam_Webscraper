#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cstring>

#include <algorithm>
#include <vector>
#include <string>
#include <bitset>
#include <queue>

using namespace std;

typedef long long int64;//NOTES:int64
typedef unsigned long long uint64;//NOTES:uint64
const double pi=acos(-1.0);//NOTES:pi
const double eps=1e-11;//NOTES:eps

// min max
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}//NOTES:checkmin(
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}//NOTES:checkmax(
template<class T> inline T square(T x){return x*x;}//NOTES:sqr

// bit manipulation
template<class T> inline T lowbit(T n){return (n^(n-1))&n;}//NOTES:lowbit(
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}//NOTES:countbit(

// math
template<class T> inline T gcd(T a,T b)//NOTES:gcd(
  {if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b)//NOTES:lcm(
  {if(a<0)return lcm(-a,b);if(b<0)return lcm(a,-b);return a*(b/gcd(a,b));}

// jihe
struct Point
    { int x,y; };
struct Rect
    { Point l,r; };
template <class T>
inline bool rect_intersect(T x1, T y1, T x2, T y2, T x3, T y3, T x4, T y4)
    { if (x2 >= x3 && y2 >= y3 && x4 >= x1 && y4 >= y1) return 1; return 0;}
inline bool rect_intersect(const Point &p1, const Point &p2, const Point &p3, const Point &p4)
    { return rect_intersect(p1.x, p1.y, p2.x, p2.y, p3.x, p3.y, p4.x, p4.y);}
inline bool rect_intersect(const Rect &rect1, const Rect &rect2)
    { return rect_intersect(rect1.l, rect1.r, rect2.l, rect2.r);}

#define ZERO(x) memset((x), 0, sizeof(x));

struct Line
{
    int d,l,cur;
    void set(int _d, int _l) {d=_d;l=_l;}
    void read()
    {
        scanf("%d %d", &d, &l);
        cur = -1;
    }
};
bool comp(const Line &lhs, const Line &rhs)
{
    return lhs.d < rhs.d;
}
const int max_line = 10000;
Line line[max_line+100];
int n_line;

int D;

void input()
{
    scanf("%d", &n_line);
    for (int i = 1; i <= n_line; i++)
        line[i].read();
    scanf("%d", &D);
}

int found;
int visited[max_line+100];
void DFS(int step, int pos, int len)
{
    ;
}

void solve()
{
    found = 0;
    line[1].cur = line[1].d;
    for (int i = 1; i <= n_line && ! found; i++)
    {
        if (line[i].cur + line[i].d >= D)
        {
            found = 1;
            break;
        }
        else if (line[i].cur == -1)
            break;

        for (int j = i+1; j <= n_line && ! found;j++)
        {
            if (line[i].cur + line[i].d >= line[j].d)
                checkmax(line[j].cur, min(line[j].d-line[i].d, line[j].l));
            else
                break;
        }
    }


    if(found)
        printf("YES\n");
    else
        printf("NO\n");
}


int main()
{
//	freopen("A.in", "r", stdin);

//	freopen("A-small-attempt0.in", "r", stdin);freopen("A-small-attempt0.out", "w", stdout);
//	freopen("A-small-attempt1.in", "r", stdin);freopen("A-small-attempt1.out", "w", stdout);
//	freopen("A-small-attempt2.in", "r", stdin);freopen("A-small-attempt2.out", "w", stdout);
//	freopen("A-small-attempt3.in", "r", stdin);freopen("A-small-attempt3.out", "w", stdout);
	freopen("A-large.in", "r", stdin);freopen("A-large.out", "w", stdout);


    int case_total;
    scanf("%d", &case_total);
    for (int case_i = 1; case_i <= case_total; case_i++)
    {
        printf("Case #%d: ", case_i);

        input();
        solve();
    }

    return 0;
}
