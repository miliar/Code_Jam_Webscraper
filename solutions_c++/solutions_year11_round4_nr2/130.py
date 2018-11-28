#include <iostream>
#include <algorithm>
#include <numeric>
#include <limits>
#include <vector>
#include <set>
#include <map>
#include <string>
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
typedef vector<VPInt> VVPInt;
typedef set<int> SInt;
typedef map<int, int> MIntInt;
typedef vector<double> VDouble;
typedef vector<VDouble> VVDouble;

PInt sum(PInt a, PInt b) {
    return PInt(a.first+b.first, a.second+b.second);
}

PInt diff(PInt a, PInt b) {
    return PInt(a.first-b.first, a.second-b.second);
}

PInt mult(PInt a, int num) {
    return PInt(num*a.first, num *a.second);
}

struct Case {
	int caseNo;
	Case(int caseNo=0) {
		this->caseNo = caseNo;
	}

	void solve() {
        int height, width, d;
        scanf("%d%d%d", &height, &width, &d);
        VVInt w(height, VInt(width, 0));
        for(int i = 0; i<height; i++) {
            char s[1000];
            scanf("%s", s);
            for(int j = 0; j < width; j++)
                w[i][j] = s[j] - '0';
        }

        // Precalc
        VVPInt data(height+1, VPInt(width+1, PInt(0, 0)));
        VVInt wData(height+1, VInt(width+1, 0));
        for(int i = 1; i <= height; i++)
            for(int j = 1; j <= width; j++) {
                data[i][j] = sum(mult(PInt(i-1, j-1), w[i-1][j-1]), diff(sum(data[i-1][j], data[i][j-1]), data[i-1][j-1]));
                wData[i][j] = w[i-1][j-1] + wData[i-1][j] + wData[i][j-1] - wData[i-1][j-1];
            }

        // DEBUG
        /*
        for(int i = 0; i <= height; i++) {
            for(int j = 0; j <= width; j++)
                printf("%d ", wData[i][j]);
            printf("\n");
        }

        for(int i = 0; i <= height; i++) {
            for(int j = 0; j <= width; j++)
                printf("(%d,%d) ", data[i][j].first, data[i][j].second);
            printf("\n");
        }*/

        // Find the answer
        int ans = 0;
        int minD=3;
        for(int i = 0; i <= height-minD; i++)
            for(int j = 0; j <= width-minD; j++)
                for(int d = minD;  i + d <= height && j + d <= width; d++) {
                    if(d<=ans) continue;
                    PInt s = diff(sum(data[i+d][j+d], data[i][j]), sum(data[i][j+d], data[i+d][j]));
                    int sw = wData[i+d][j+d] + wData[i][j] - wData[i][j+d] - wData[i+d][j];
                    for(int tI=0; tI<2; tI++)
                        for(int tJ=0; tJ<2; tJ++) {
                            int curI = i+tI*(d-1);
                            int curJ = j+tJ*(d-1);
                            s = diff(s, mult(PInt(curI, curJ), w[curI][curJ]));
                            sw -= w[curI][curJ];
                        }
                    if(mult(s, 2) == mult(PInt(2*i+d-1, 2*j+d-1), sw))
                        ans = d;
                }

        if(ans==0)
            printf("Case #%d: IMPOSSIBLE\n", caseNo);
        else
            printf("Case #%d: %d\n", caseNo, ans);
	}
};

int main()
{
	try {
		int testCount;
		cin >> testCount;
		for(int i = 1; i <= testCount; i++) {
			Case c(i);
			 cerr << "solving " << i << endl;
			c.solve();
		}
	} catch(const char *msg) {
		cerr << "EXCEPTION: " << msg << endl;
		return 1;
	}
	return 0;
}
