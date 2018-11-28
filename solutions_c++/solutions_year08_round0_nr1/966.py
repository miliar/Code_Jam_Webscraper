#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <map>
#include <queue>
#include <vector>
#include <string>
#include <conio.h>
using namespace std;
#define		MAX(a,b)	((a)>(b)?(a):(b))
#define		MIN(a,b)	((a)<(b)?(a):(b))

int wara[102];

int size;
int dbsize;
int ga;
vector <int> gq;

int ahya;

void saiki(int n, int step) {
	if (ahya == 1)
		return;
	if (step == 0) {
			char flag[102];
		if (ga != 0) {
			int a, b;
			a = 0; b = wara[ga-1];
			int k;
			int cnt = 0;

			int pt = 0;
			int v = ga-1;

			memset(flag, 0, dbsize);
	/*		for (k = ga-1; k >= 0; k --) {
				printf("%d", wara[k]);
			}*/
		//	printf("*");
			for (;pt < size; pt ++) {
				flag[gq[pt]] = 1;
	//			printf("%d ", gq[pt]);

				if (wara[v]-1 == pt && v >= 0) {
					v --;
	//				printf(" -- ");
					for (int j = 0; j < dbsize; j ++) {
						if (flag[j] == 0) break;
					}
					if (j != dbsize) {
						cnt ++;
					}
					memset(flag, 0, dbsize);
				}
			}
	
			for (int j = 0; j < dbsize; j ++) {
				if (flag[j] == 0) break;
			}
			if (j != dbsize) {
				cnt ++;
			}
			/*
			for (k = ga-1;k > 0; k --) {
//				printf("[[%d %d]]", a, b);
				memset(flag, 0, dbsize);
	
				for (a;a <= b; a++) {
					flag[gq[a]] = 1;
					printf("(%d)", gq[a]);
				}
				printf(" ");
				int f = 0;
				for (int j = 0; j < dbsize; j ++) {
					if (flag[j] == 0) break;
				}
				if (j != dbsize) {
					cnt ++;
				}
				a = wara[k], b = wara[k-1];
			}*/
	//		printf("[%d %d]", cnt, ga);
	//		puts("");
			if (cnt == ga+1) {
				ahya = 1;
	//			printf("!!");
				return;
			}
		} else if (ga == 0) {
	//		printf("*");
			memset(flag, 0, dbsize);
			for (int a = 0;a < size; a++) {
				flag[gq[a]] = 1;
		//	printf("(%d)", gq[a]);
			}
			int cnt = 0;
			for (int j = 0; j < dbsize; j ++) {
				if (flag[j] == 0) break;
			}
			if (j != dbsize) {
				ahya = 1;	
				return;
			}
		}
		/*
		for (int j = 0; j < ga; j ++) {
			printf("%d ", wara[j]-1);
		}
		if (ga == 0)
			printf("no");
		puts("");
		*/
		//
	} else if (step > 0) {
		for (int j = n+1; j < size; j ++) {
			wara[step-1] = j;
			saiki(j, step-1);
			if (ahya == 1) return;
		}
	}
}

int main() {
	int T, N;
	int i, j, k;

	/*
	size = 9;
	ga = 3;
	saiki(0, 3);
	return 0;*/

	scanf("%d\n", &T);
	for (i = 0; i < T; i ++) {
		vector <string> db;
		vector <int> q;
		scanf("%d\n", &N);
		for (j = 0; j < N; j ++) {
			char buf[1024];
//			scanf("%s", buf);
			gets(buf);
			db.push_back(buf);
		}
		scanf("%d\n", &N);
		for (j = 0; j < N; j ++) {
			char buf[1024];
			string str;
			gets(buf);
			str = buf;
			for (k = 0; k < db.size(); k ++) {
				if (str == db[k]) break;
			}
			q.push_back(k);
		}



		int a;
		int now = 0, cnt = -1;

		int target, tmp;
		for (;now < q.size();) {
			tmp = -1;
			for (a = 0; a < db.size(); a ++) {
				int d;
				if (q[now] == a) continue;
				for (d = now; d < q.size(); d ++) {
					if (q[d] == a) break;
				}
				if (tmp < d - now) {
					tmp = d - now;
					target = a;
				}
			}
			now += tmp;
			cnt ++;
		}
		if (cnt == -1) cnt = 0;
		printf("Case #%d: %d\n",i+1, cnt);
		/*
		dbsize = db.size();
		size = q.size();
		gq = q;
		ahya = 0;
		for (int ans = 0; ans < q.size(); ans ++) {
			ga = ans;
			saiki(0,ans);
			if (ahya == 1) {
				printf("Case #%d: %d\n",i+1, ga);
				break;
			}
		}*/
	}
	return 0;
}