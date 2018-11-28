#include <iostream>
#include <algorithm>
#include <numeric>
#include <limits>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <queue>
using namespace std;
#include <stdio.h>

#define forin(it, col) for(typeof (col).begin() it = (col).begin(); it != (col).end(); it++)
#define range(col) (col).begin(), (col).end()
#define substr(s, from, to) (s).substr((from), (to)-(from))

typedef long long ll;
typedef vector<int> VInt;
typedef vector<VInt> VVInt;
typedef vector<bool> VBool;
typedef vector<VBool> VVBool;
typedef vector<char> VChar;
typedef vector<VChar> VVChar;
typedef pair<int, int> PInt;
typedef vector<PInt> VPInt;
typedef set<int> SInt;
typedef map<int, int> MIntInt;
typedef vector<double> VDouble;
typedef vector<VDouble> VVDouble;

struct Case {
    int caseNo;
    Case(int caseNo=0) {
        this->caseNo = caseNo;
    }

    int height, width, n;
    queue<int> q;
    VVInt left, right;
    VInt degLeft, degRight;
    VBool deadLeft, deadRight;

    void removeEdge(int from, int to) {
        left[from].erase(remove(range(left[from]), to), left[from].end());
        right[to].erase(remove(range(right[to]), from), right[to].end());
        degLeft[from]--;
        degRight[to]--;
    }

    int getAns() {
        // Read the input, build the graph
        scanf("%d%d", &height, &width);
        n = height * width;
        left = VVInt(n, VInt());
        right = VVInt(n, VInt());
        degLeft.assign(n, 0);
        degRight.assign(n, 0);
        deadLeft.assign(n, false);
        deadRight.assign(n, false);
        for(int i = 0; i < height; i++) {
            char line[1000];
            scanf("%s", line);
            for(int j = 0; j < width; j++) {
                char ch = line[j];
                int di, dj;
                switch(ch) {
                case '|': di = 1; dj = 0; break;
                case '-': di = 0; dj = 1; break;
                case '/': di = 1; dj = -1; break;
                case '\\': di = 1; dj = 1; break;
                default: throw "Unknown character";
                }
                for(int t = -1; t <= 1; t+=2) {
                    int newI = ((i + di*t)+height)%height;
                    int newJ = ((j + dj*t)+width)%width;
                    int from = i*width + j;
                    int to = newI*width + newJ;
                    left[from].push_back(to);
                    right[to].push_back(from);
                    degLeft[from]++;
                    degRight[to]++;
                }
            }
        }

        // Check for orphaned vertices, build the queue
        for(int v = 0; v < n; v++) {
            if(degRight[v] == 0) return 0;
            if(degRight[v] == 1) q.push(v);
        }

        // Deal with the leaves
        while(!q.empty()) {
            int v = q.front();
            q.pop();
            if(degRight[v] != 1) continue;
            int u = right[v][0];
            int newV = left[u][0] + left[u][1] - v;
            removeEdge(u, newV);
            if(degRight[newV]==0) return 0;
            if(degRight[newV]==1) q.push(newV);
            //fprintf(stderr, "removed 1 leaf\n");
        }

        // DEBUG
        /*
        for(int v = 0; v < n; v++)
            fprintf(stderr, "%d ", degRight[v]);
        fprintf(stderr, "\n");*/

        // Deal with the loops
        int ans = 1;
        for(int v = 0; v < n; v++) {
            if(degRight[v] != 2 || deadRight[v]) continue;
            int u = right[v][0];
            while(!deadRight[v]) {
                deadRight[v] = true;
                int newU = right[v][0] + right[v][1] - u;
                int newV = left[newU][0] + left[newU][1] - v;
                u = newU;
                v = newV;
            }
            ans = (ans*2) % 1000003;
        }
        return ans;
    }

    void solve() {

        printf("Case #%d: %d\n", caseNo, getAns());
    }
};

int main()
{
    try {
        int testCount;
        scanf("%d", &testCount);
        for(int i = 1; i <= testCount; i++) {
            fprintf(stderr, "Solving %d\n", i);
            Case c(i);
            c.solve();
        }
    } catch(const char *msg) {
        fprintf(stderr, "EXCEPTION: %s\n", msg);
        return 1;
    }
    return 0;
}
