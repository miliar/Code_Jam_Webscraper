#include <algorithm>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
using namespace std;

typedef long long ll;

typedef vector<int> vi;
typedef vector<string> vs;

#define f(i,a,b) for(int i=(a);i<(b);++i)
#define fd(i,a,b) for(int i=(a);i>=(b);--i)
#define pb(_v,_a) (_v).push_back(_a)
#define sz size()
#define range(_a) (_a).begin(),(_a).end()
#define foreach(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define init(m,v) memset((m), (v), sizeof((m)))
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 

int h, w;
int heights[100][100];
int sink[100][100];
char sinkCharAssignments[26];
int sinks;
int findSink(int r, int c) {
    int &retval = sink[r][c];
    if (retval) return retval;
    int nextR = r, nextC = c;
    if (r > 0) { // North
        if (heights[r-1][c] < heights[r][c]) {
            nextR = r-1;
        }
    }
    if (c > 0) { // West
        if (heights[r][c-1] < heights[nextR][nextC]) {
            nextR = r;
            nextC = c-1;
        }
    }
    if (c < w-1) { // east
        if (heights[r][c+1] < heights[nextR][nextC]) {
            nextR = r;
            nextC = c + 1;
        }
    }
    if (r < h -1) { // south
        if (heights[r+1][c] < heights[nextR][nextC]) {
            nextR = r+1;
            nextC = c;
        }
    }
    if (nextR == r && nextC == c) {
        retval = sinks;
        sinks++;
        return retval;
    }
    return retval = findSink(nextR, nextC);
}
int main() {
    int n;
    cin>>n;
    f(test,1,n+1) {
        ll ans = 0;
        cin>>h>>w;
        sinks = 1;
        init(sink, 0);
        init(sinkCharAssignments, 0);
        f(i,0,h) f(j,0,w) cin>>heights[i][j];
        f(i,0,h) f(j,0,w) if (!sink[i][j]) sink[i][j] = findSink(i,j);
        int currentSinkChar = 0;
        cout<<"Case #"<<test<<":"<<endl;
        f(i,0,h) {
            f(j,0,w) {
                if (!sinkCharAssignments[sink[i][j]-1]) {
                    sinkCharAssignments[sink[i][j]-1] = currentSinkChar + 'a';
                    currentSinkChar++;
                }
                cout<<sinkCharAssignments[sink[i][j]-1];
                if (j == w-1) cout<<endl;
                else cout<<" ";
            }
        }
    }
    return 0;
}
