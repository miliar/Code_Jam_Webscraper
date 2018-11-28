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
    int ans;
    queue<int> rises;
    Case(int caseNo=0) {
        this->caseNo = caseNo;
    }

    void solve() {
        int n;
        scanf("%d", &n);
        VInt numbers(n);
        for(int i = 0; i < n; i++)
            scanf("%d", &numbers[i]);

        VInt counts(10000+10, 0);
        forin(num, numbers)
            counts[*num]++;

        ans = 0;
        for(int i = 1; i < counts.size(); i++) {
            if(counts[i] > counts[i-1]) {
                for(int t=0; t<counts[i] - counts[i-1]; t++)
                    rises.push(i);
            } else if(counts[i] < counts[i-1]) {
                for(int t=0; t<counts[i-1] - counts[i]; t++) {
                    int start = rises.front();
                    rises.pop();
                    int len = i - start;
                    if(ans==0 || len < ans)
                        ans = len;
                }
            }
        }
        printf("Case #%d: %d\n", caseNo, ans);
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
