#include <cstdio>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <utility>
#include <algorithm>
#include <list>
#include <cstring>
#include <map>

#define FOREACH(a,c) for(__typeof((c).begin()) a = (c).begin(); a != (c).end(); a++)
#define MP(i,j) make_pair(i,j)

using namespace std;

typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VII;

VII vine;
set<PII> S;

bool DFS(int v, int l, int D){
//    printf ("%d %d : %d\n", vine[v].first, l, D);
    if (l <= 0) return false;
//    printf ("1\n");
    if (D == vine[v].first + l) return true;
//    printf ("2\n");
    if (S.find(MP(v,l)) != S.end()) return false;
//    printf ("3\n");
    S.insert(MP(v,l));
    for (int i = v+1; i < vine.size(); i++){
//        printf ("%d : %d %d %d\n", i, vine[v].first, l, vine[i].first);
        if (vine[v].first + l >= vine[i].first)
            if (DFS(i, min(vine[i].first - vine[v].first, vine[i].second), D)) return true;
    }
    return false;
}

int main(){
    int z; scanf ("%d", &z);
    for (int ww = 1; ww <= z; ww++){
        vine.clear(); S.clear();
        int n; scanf ("%d", &n);
        for (int i = 0; i < n; i++){
            int d, l; scanf ("%d %d", &d, &l);
            vine.push_back(MP(d,l));
        }
        int D; scanf ("%d", &D);
        bool answer;
        if (vine[0].first > vine[0].second) { answer = false; }
        else {answer = DFS(0, vine[0].first, D); }
        printf ("Case #%d: %s\n", ww, answer ? "YES" : "NO");
    }
    return 0;
}
