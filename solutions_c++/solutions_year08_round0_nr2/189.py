#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

FILE *fp_r, *fp_w;
int t, d, n, m;
int i, j, k;
int hour, minute;

struct sche {
	int s, e;

	bool operator < (const sche &r) const {
		return (s != r.s ? s < r.s : e < r.e);
	}
	bool operator == (const sche &r) const {
		return s == r.s && e == r.e;
	}
};

sche s;
vector<sche> v1, v2;
int x, y;
int chk1[100], chk2[100];
int c1, c2;
int now, ret;

int trainAB(int tm, int idx) {
	int p;

	for(p = idx; p < v1.size(); p++) {
		if (chk1[p] != 0) continue;
		if (v1[p].s >= tm) {
			chk1[p] = 1;
			return v1[p].e;
		}
	}
	return -1;
}

int trainBA(int tm, int idx) {
	int p;

	for(p = idx; p < v2.size(); p++) {
		if (chk2[p] != 0) continue;
		if (v2[p].s >= tm) {
			chk2[p] = 1;
			return v2[p].e;
		}
	}
	return -1;
}

int main() {
	//fp_r = fopen("B-small.txt", "r");
	fp_r = fopen("B-large.in", "r");
	fp_w = fopen("b.out", "w");

	fscanf(fp_r, "%d", &t);
	for(i = 0; i < t; i++) {
		fscanf(fp_r, "%d", &d);		
		fscanf(fp_r, "%d %d", &n, &m);

		v1.clear();
		v2.clear();
		for(j = 0; j < n; j++) {
			fscanf(fp_r, "%d:%d", &hour, &minute);
			s.s = hour * 60 + minute;
			fscanf(fp_r, "%d:%d", &hour, &minute);
			s.e = hour * 60 + minute;
			v1.push_back(s);
			chk1[j] = 0;
		}
		for(j = 0; j < m; j++) {
			fscanf(fp_r, "%d:%d", &hour, &minute);
			s.s = hour * 60 + minute;
			fscanf(fp_r, "%d:%d", &hour, &minute);
			s.e = hour * 60 + minute;
			v2.push_back(s);
			chk2[j] = 0;
		}

		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end());

		x = 0;	y = 0;	c1 = 0;	c2 = 0;
		while(1) {
			while(x < v1.size()) {
				if (chk1[x] == 0) break;
				x++;
			}
			while(y < v2.size()) {
				if (chk2[y] == 0) break;
				y++;
			}

			if (x == v1.size()) {
				for(j = y; j < v2.size(); j++) {
					if (chk2[j] == 0)
						c2++;
				}
				break;
			}

			if (y == v2.size()) {
				for(j = x; j < v1.size(); j++) {
					if (chk1[j] == 0)
						c1++;
				}
				break;
			}

			if (v1[x].s <= v2[y].s) {
				c1++;
				chk1[x] = 1;
				now = v1[x].e + d;
				while(1) {
					ret = trainBA(now, y);
					if (ret == -1) break;
					now = ret + d;
					ret = trainAB(now, x);
					if (ret == -1) break;
					now = ret + d;
				}
			}
			else {
				c2++;
				chk2[y] = 1;
				now = v2[y].e + d;
				while(1) {					
					ret = trainAB(now, x);
					if (ret == -1) break;
					now = ret + d;
					ret = trainBA(now, y);
					if (ret == -1) break;
					now = ret + d;
				}
			}
		}

		fprintf(fp_w, "Case #%d: %d %d\n", i+1, c1, c2);
	}

	fclose(fp_w);
	fclose(fp_r);

	return 0;
}