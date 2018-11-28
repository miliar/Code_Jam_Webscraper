#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <cassert>
#include <math.h>
using namespace std;
#define ALL(x) x.begin(),x.end()
#define MP make_pair
#define SZ size()
#define REP(i,n) for( int i=0;i<int(n);++i)
#define PII pair<int,int>
#define VPII vector<PII>
namespace my_namespace {
    template <class X >static vector < X > &operator+=(vector < X > &vec,
     const X & el) {
        vec.push_back(el);
        return vec;
}};
#define VI vector<int>
#define VVI vector<VI>
VI mk3(int a, int b, int c)
{
    VI vi(3);
    vi[0] = a;
    vi[1] = b;
    vi[2] = c;
    return vi;
}
using namespace my_namespace;
VVI a;
int Answer;
void subprocess(int cnt, int left)
{
    VPII vec;
    REP(i, cnt)
     vec += MP(a[i][1], a[i][2]);
    sort(ALL(vec));
    priority_queue < int >pq;
    REP(i, cnt) {
        int v = vec[i].first;
        int l2 = left - v;
        if (l2 < 0)
            break;
        pq.push(vec[i].second);
        while (!pq.empty() && pq.top() > l2)
            pq.pop();
        Answer = max(Answer, (int) pq.SZ);
    }
}
void generate()
{
    int n = 5000;
    printf("%d\n", 1);
    printf("%d\n", n);
    REP(i, n)
     printf("%d %d %d\n", rand() % 10001, rand() % 10001, rand() % 10001);
}
void problem()
{
    a.clear();
    Answer = 0;
    int n;
    scanf("%d", &n);
    REP(i, n) {
        int x, y, z;
        scanf("%d%d%d", &x, &y, &z);
        a += (mk3(x, y, z));
    }
    sort(ALL(a));
    REP(i, n) {
        int left = 10000 - a[i][0];
        subprocess(i + 1, left);
    }
    printf("%d\n", Answer);
}
int main(int argc, char **argv)
{
    if (1 < argc)
        return generate(), 0;
    int n;
    scanf("%d", &n);
    REP(i, n) {
        printf("Case #%d: ", i + 1);
        problem();
    }
    return 0;
}
