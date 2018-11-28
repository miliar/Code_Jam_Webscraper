#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>

using namespace std;

const int maxn = 10000 + 10;
int d[maxn], l[maxn];
int r[maxn], h[maxn];
int n, D;
int main() {
	int tc;
	scanf("%d", &tc);
	for(int nCase = 1; nCase <= tc; ++nCase) {
		scanf("%d", &n);
		for(int i = 0; i < n;++i) {
			scanf("%d%d", d + i, l + i);
		}
		scanf("%d", &D);
		bool ok = false;
		int curDist;
		int head, tail;
		int newR, newH;
		head = 0, tail = 1;
		r[0] = d[0] + d[0], h[0] = d[0];
		for(int i = 1; i < n; ++i) {
			curDist = d[i];
			while(tail > head && r[head] < curDist) {
				++head;
			}
			//cout<<"SeeA "<<head<<' '<<tail<<endl;
			if(head >= tail)break;
			newH = curDist;
			newR = curDist + min(d[i] - h[head], l[i]);
			//cout<<"SeeB "<<head<<' '<<tail<<endl;
			r[tail] = newR;
			h[tail] = newH;
			//cout<<"New "<<newR<<' '<<newH<<endl;
			++tail;
			//cout<<"See "<<head<<' '<<tail<<endl;
		}
		while(tail > head && r[head] < D) {
			++head;
		}
		//cout<<"Check "<<head<<' '<<tail<<endl;
		printf("Case #%d: ", nCase);
		puts(tail > head ? "YES":"NO");
	}
	return 0;
}

