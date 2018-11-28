#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <map>
#include <queue>
#include <vector>
#include <string>
using namespace std;
#define		MAX(a,b)	((a)>(b)?(a):(b))
#define		MIN(a,b)	((a)<(b)?(a):(b))

int main() {
	int T;
	int i, j, k;
	scanf("%d\n", &T);
	for (i = 0; i < T; i ++) {
		int TIME, NA, NB;
		vector <int> tbl;
		vector <pair < pair<int ,int>, pair<int, int> > > db;
		scanf("%d\n", &TIME);
		scanf("%d %d\n", &NA, &NB);
		int a, b, c,d;
		for (j = 0; j < NA; j ++) {
			scanf("%d:%d %d:%d\n", &a, &b ,&c, &d);
			db.push_back(make_pair(make_pair(a*60+b, c*60+d + TIME), make_pair(1, 0)));
			tbl.push_back(c*60+d + TIME);
		}
		for (j = 0; j < NB; j ++) {
			scanf("%d:%d %d:%d\n", &a, &b ,&c, &d);
			db.push_back(make_pair(make_pair(a*60+b, c*60+d + TIME), make_pair(0, 1)));
			tbl.push_back(c*60+d + TIME);
		}
		sort(db.begin(), db.end());
		/*
		for (j = 0; j < db.size(); j ++) {
			printf("[%d] %d %d \n", db[j].second.first, db[j].first.first, db[j].first.second);
		}
		puts("");*/
		sort(tbl.begin(), tbl.end());

		for (int time = 0; time < tbl.size(); time ++) {
			for (j = 0; j < db.size(); j ++) {
				if (tbl[time] == db[j].first.second) {

					int tmp = 999999;
					vector <pair < pair<int ,int>, pair<int, int> > >::iterator ite, bk = NULL;
					for (ite = db.begin(); ite != db.end(); ite ++) {
						if (db[j] == *ite) continue;

						if ((*ite).second.first == db[j].second.second) {
							if ((*ite).first.first >= db[j].first.second) {
								if (tmp > (*ite).first.first - db[j].first.second) {
									tmp = (*ite).first.first - db[j].first.second;
									bk = ite;
								}
							}
						}
					}
					if (bk != NULL) {
						if (db[j].second.second == 0) db[j].second.second = 1;
						else db[j].second.second = 0;

						db[j].first.second = (*bk).first.second;
						db.erase(bk);
						j = -1;
					}
				}
			}
		}

		
		a = b = 0;
		for (j = 0; j < db.size(); j ++) {
			if (db[j].second.first == 1) a++;
			else b ++;
		//	printf("[%d] %d %d \n", db[j].second.first, db[j].first.first, db[j].first.second);
		}
		printf("Case #%d: %d %d", i+1, a, b);
		puts("");
	}

	return 0;
}