#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
using namespace std;

struct node {
    int location; string robot;
};

int T, N;

inline int abs(int x) { return x < 0 ? -x : x; }

int main() {
    freopen("A-large.in","r",stdin);
    freopen("botout.txt","w",stdout);
    scanf("%d",&T);
    for (int t = 1; t <= T; t++) {
        scanf("%d",&N);
        vector<node> Total;
        for (int n = 0; n < N; n++) {
            node n;
            cin >> n.robot >> n.location;
	    Total.push_back(n);
        }

        int lastb = 0, lasto = 0, bspot = 1, ospot = 1, time = 0;
        for (int n = 0; n < N; n++) {
            if (Total[n].robot == "B") {
                time += 1 + max(0, abs(Total[n].location - bspot) - (time - lastb));
		lastb = time; bspot = Total[n].location;
            }
	    else {
		time += 1 + max(0, abs(Total[n].location - ospot) - (time - lasto));
		lasto = time; ospot = Total[n].location;
	    }
        }
	printf("Case #%d: %d\n",t ,time);
    }
}
