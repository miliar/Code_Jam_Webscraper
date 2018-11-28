#include <algorithm>
#include <string>
#include <cstring>
#include <cstdio>
#include <map>
#include <vector>
#define X first
#define Y second
#define PII pair<int, int>
#define PB push_back
#define FOREACH(c, it) for(typeof(c.begin()) it = c.begin(); it != c.end(); ++it)
#define ll long long

using namespace std;

int nodes[10000];
int gates[10000];
int change[10000];
int m;

void calc(int i) {
  if (nodes[2*(i+1)-1] == -1)
    calc(2*(i+1)-1);
  if (nodes[2*(i+1)] == -1)
    calc(2*(i+1));
  if (gates[i] == 1)
    nodes[i] = nodes[2*(i+1)-1] * nodes[2*(i+1)];
  else
    nodes[i] = nodes[2*(i+1)-1] + nodes[2*(i+1)] - nodes[2*(i+1)-1] * nodes[2*(i+1)];
}

int solve(int i, int val) {
  if (val == nodes[i])
    return 0;
  if (i >= (m-1)/2)
    return -1;
    
  int s1 = solve(2*(i+1)-1, 0);
  int s2 = solve(2*(i+1), 0);
  int s3 = solve(2*(i+1)-1, 1);
  int s4 = solve(2*(i+1), 1);
  
  int andcost, orcost;
  
        if (val == 1) {
            if (s3 == -1 || s4 == -1)
                andcost = -1;
            else
                andcost = s3 + s4;
        } else {
            if (s1 == -1 && s2 == -1)
                andcost = -1;
            else
                andcost = s1 == -1 ? s2 : s2 == -1 ? s1 : s1 < s2 ? s1 : s2;
        }

        if (val == 0) {
            if (s1 == -1 || s2 == -1)
                orcost = -1;
            else
                orcost = s1 + s2;
        } else {
            if (s3 == -1 && s4 == -1)
                orcost = -1;
            else
                orcost = s3 == -1 ? s4 : s4 == -1 ? s3 : s3 < s4 ? s3 : s4;
        }

  if (change[i] == 1) {
    if (orcost != -1 && gates[i] == 1)
        ++orcost;
    if (andcost != -1 && gates[i] == 0)
        ++andcost;
    if (andcost == -1)
        return orcost;
    if (orcost == -1)
        return andcost;
    return orcost < andcost ? orcost : andcost;
    
  } else {  
    if (gates[i] == 1)
        return andcost;
    else
        return orcost;  
  }
  
}

int main() {
    int ncase;
    scanf("%d", &ncase);
    for (int icase = 0; icase < ncase; ++icase) {
        int v;
        scanf("%d %d", &m, &v);
        
        for (int i = 0; i < (m-1)/2; ++i) {
            scanf("%d %d", &gates[i], &change[i]);
        }
        memset(nodes, 0xff, sizeof(nodes));
        for (int i = 0; i < (m+1)/2; ++i) {
            scanf("%d", &nodes[(m-1)/2+i]);
        }
        calc(0);
        int sol = solve(0, v);
        
        if (sol == -1)
            printf("Case #%d: IMPOSSIBLE\n", icase+1);
        else
            printf("Case #%d: %d\n", icase+1, sol);
    }
    return 0;
}
