#include <algorithm>
#include <string>
#include <list>
#include <numeric>
#include <vector>
#include <math.h>
#include <set>
#include <map>
#include <sstream>
#include <stack>
#include <stdio.h>
#include <iostream>
using namespace std;

int n;
int r[1000];
int wid, len;
int id[1000];
int X[1000];
int Y[1000];
int rgt;
int inf = 2000000000;

bool cmp(int i, int j) {
    return r[i] > r[j];
}

class cl {
public:
    int X0, Y0, X1, Y1;
    cl(int x0, int y0, int x1, int y1) {
        X0 = x0, Y0 = y0, X1 = x1, Y1 = y1;
    }
};

vector<cl> v;

void solve(int tst) {
    printf("Case #%d:", tst+1);
	cin>>n>>wid>>len;

	for (int i = 0; i < n; ++i) {
		cin>>r[i];
        id[i] = i;
    }

    sort(id, id+n, cmp);

    rgt = r[id[0]];
    wid += 2*rgt;
    len += 2*rgt;

    v.clear();
	v.push_back(cl(0, 0, wid, len));

    for (int iter = 0; iter < n; ++iter) {
        int i = id[iter];
        int R = r[i];
        int pos = -1;
        int minSide = inf;
		for (int j = 0; j < v.size(); j++) {
            const cl& elem = v[j];
            int mn = min(elem.X1-elem.X0, elem.Y1-elem.Y0);
            int x = max(rgt, elem.X0+R);
            int y = max(rgt, elem.Y0+R);
            int x2 = min(wid-rgt, elem.X1-R);
            int y2 = min(len-rgt, elem.Y1-R);
            if (!(x <= x2 && y <= y2))
                continue;
            if (pos == -1 || mn < minSide) {
                minSide = mn;
                pos = j;
            }
        }
        cl elem = v[pos];
        v.erase(v.begin()+pos);
        int wid = max(rgt, elem.X0+R);
        int len = max(rgt, elem.Y0+R);
        if (elem.Y1-elem.Y0 <= elem.X1-elem.X0) {
            v.push_back(cl(elem.X0, len+R, wid+R, elem.Y1));
            v.push_back(cl(wid+R, elem.Y0, elem.X1, elem.Y1));
        }
        else {
            v.push_back(cl(elem.X0, len+R, elem.X1, elem.Y1));
            v.push_back(cl(wid+R, elem.Y0, elem.X1, len+R));
        }
        X[i] = wid-rgt;
        Y[i] = len-rgt;
    }
    for (int i = 0; i < n; ++i) {
		cout<<" "<<X[i]<<" "<<Y[i];
	}
    cout<<endl;
}

void solution()
{
    int tst;
	cin>>tst;
    for (int i = 0; i < tst; ++i) {
        solve(i);
	}
}

int main()
{
	freopen("in.in", "rt", stdin);
    freopen("out.out", "wt", stdout);
	solution();
    return 0;
} 