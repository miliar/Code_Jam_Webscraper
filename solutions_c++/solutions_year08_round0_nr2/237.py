#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;

#define FOREACH(it,x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)
#define ALL(x) (x).begin(), (x).end()
template<class T> void DUMP(const T& v) { FOREACH(it,v) cout<<*it<<' '; cout<<endl; }

enum { goalA, goalB, startA, startB };
typedef pair<int, int> Train;
#define time first
#define type second

int main() {
	int N; cin>>N;
	for (int testcase = 1; testcase <= N; testcase++) {
		int turnaround; cin>>turnaround;
		int na, nb; cin>>na>>nb; 
		vector<Train> t((na+nb)*2);
		for (int i = 0; i < t.size(); i++) {
			int h,m;
			scanf("%d:%d", &h, &m);
			t[i].time = h*60+m;
			int v = 0;
			if (i%2 == 0) v+=2;
			else t[i].time += turnaround;
			if (i >= na*2) v++;
			t[i].type = v;
		}
		sort(ALL(t));
		int a = 0, b = 0;
		int nowa = 0, nowb = 0;
		for (int i = 0; i < t.size(); i++) {
			if (t[i].type < 2) {
				if (t[i].type == 0) nowb++;
				else nowa++;
			} else {
				if (t[i].type == 2) {
					if (nowa == 0) a++;
					else nowa--;
				} else {
					if (nowb == 0) b++;
					else nowb--;
				}
			}
		}
		cout<<"Case #"<<testcase<<": "<<a<<" "<<b<<endl;
	}
	return 0;
}
