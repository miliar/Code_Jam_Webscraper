#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <iostream>

using namespace std;

struct ride {
	int s, f;
	bool a;
};

bool operator <(ride a, ride b) {
	return a.s < b.s;
}

int main() {
	FILE *fin = fopen("B-large.in", "r");
	int n;
	fscanf(fin, "%d", &n);
	FILE *fout = fopen("B-large.out", "w");
	for(int i = 0; i < n; i++) {
		int t;
		fscanf(fin, "%d", &t);
		int na, nb;
		fscanf(fin, "%d %d", &na, &nb);
		ride r[210];
		for(int j = 0; j < na; j++) {
			int hs, ms, hf, mf;
			fscanf(fin, "%d:%d %d:%d", &hs, &ms, &hf, &mf);
			r[j].s = 60 * hs + ms;
			r[j].f = 60 * hf + mf;
			r[j].a = true;
			//if(i < 5) cout << r[j].s << " " << r[j].f << endl;
		}
		for(int j = na; j < na + nb; j++) {
			int hs, ms, hf, mf;
			fscanf(fin, "%d:%d %d:%d", &hs, &ms, &hf, &mf);
			r[j].s = 60 * hs + ms;
			r[j].f = 60 * hf + mf;
			r[j].a = false;
			//if (i < 5) cout << r[j].s << " " << r[j].f << endl;
		}
		sort(r, r + na + nb);
		int a = 0, b = 0;
		priority_queue<int, vector<int>, greater<int> > pa, pb;
		for(int j = 0; j < na + nb; j++)
			if(r[j].a) {
				if(pa.empty() || pa.top() > r[j].s) {
					a++;
					pb.push(r[j].f + t);
				}
				else {
					pa.pop();
					pb.push(r[j].f + t);
				}
			}
			else {
			if(pb.empty() || pb.top() > r[j].s) {
					b++;
					pa.push(r[j].f + t);
				}
				else {
					pb.pop();
					pa.push(r[j].f + t);
				}
			}
		fprintf(fout, "Case #%d: %d %d\n", i + 1, a, b);
	}
	fclose(fin);
	fclose(fout);
	//system("pause");
	return 0;	
}
