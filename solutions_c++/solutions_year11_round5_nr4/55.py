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

    VChar pattern;
    VVInt values;
    VInt ans;
    VInt one;
    VInt base;

    bool match(int digit, char pattern) {
        return pattern=='?' || pattern == '0' + digit;
    }

    void addshift(VInt &res, int shift, VInt &source, int srcLim = -1) {
        int carry = 0;
        if(srcLim==-1)srcLim = source.size();
        for(int i = 0; i + shift < res.size(); i++) {
            int curD = carry + res[i+shift];
            if(i < srcLim) curD += source[i];
            res[i+shift] = curD % 2;
            carry = curD / 2;
            if(carry==0 && i>=srcLim) break;
        }
    }

    bool run(int d) {
        VInt &prev = values[d];
        VInt &cur = values[d+1];
        // DEBUG
        /*
        fprintf(stderr, "trying ");
        forin(dig, base)fprintf(stderr, "%1d", *dig);
        fprintf(stderr, "\n");
        forin(dig, cur)fprintf(stderr, "%1d", *dig);
        fprintf(stderr, "\n");
        */

        if(d >= pattern.size()) {
            ans = prev;
            return true;
        }

        cur = prev;
        if(match(cur[d], pattern[d]) && run(d+1)) return true;
        if(2*d >= pattern.size()) return false;
        addshift(cur, d+1, base, d);
        addshift(cur, 2*d, one);
        if(cur[pattern.size()] || cur[pattern.size()+1]) return false;
        base[d] = 1;
        if(match(cur[d], pattern[d]) && run(d+1)) return true;
        base[d] = 0;

        return false;
    }

    void solve() {
        // init
        one.assign(1, 1);
        base.assign(150, 0);

        // read the input
        char line[1000];
        scanf("%s", line);
        for(int i = 0; line[i]; i++)
            pattern.push_back(line[i]);
        reverse(range(pattern));

        // Do the brainching
        values.assign(150, VInt(300, 0));
        if(!run(0))
            throw "no answer!";

        // Format the answer
        ans.resize(pattern.size());
        reverse(range(ans));

        printf("Case #%d: ", caseNo);
        forin(digit, ans) {
            printf("%1d", *digit);
        }
        printf("\n");
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
