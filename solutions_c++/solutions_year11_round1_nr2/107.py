#include <stdio.h>
#include <vector>
#include <string.h>
#include <algorithm>

#define INF 999999

using namespace std;


char words[10010][100];

char aCompareKey;
class A {
	public:
		int no;
		A(int _no = 0) : no(_no) {
		}
		bool operator < (const A &rhs) const {
			char wa[100], wb[100];
			make(wa, no);
			make(wb, rhs.no);
			return strcmp(wa, wb) < 0;
		}
		bool operator != (const A &rhs) const {
			return *this < rhs || rhs < *this;
		}
		bool operator == (const A &rhs) const {
			return !(*this != rhs);
		}

		void make(char reWord[], int gno) const {
			char *iword = words[gno];
			int i;
			for (i = 0; iword[i]; i++)
				reWord[i] = (iword[i] == aCompareKey) ? '1' : '0';
			reWord[i] = '\0';
		}
};

int notContain(char word[], char l) {
	for (int i = 0; word[i]; i++)
		if (word[i] == l)
			return 0;
	return 1;
}

void f(int level, int gtime, const vector<A> &set, char guessList[], int &reNo, int &reDeep) {
	if (set.size() == 0) {
		reDeep = 0;
	}
	else if (set.size() == 1) {
		reNo = set[0].no;
		reDeep = gtime;
		//printf("size one: level=%d, gtime=%d, has only %s\n", level, gtime, words[set[0].no]);
	}
	else {
		vector<A> cset = set;
		aCompareKey = guessList[level];
		sort(cset.begin(), cset.end());
		

		bool shouldSkip = true;
		for (int i = 0; i < cset.size(); i++)
			if (notContain(words[cset[i].no], guessList[level]) == 0)
				shouldSkip = false;
		
		//printf("level=%d, gtime=%d  (%c)[skip=%d]\n", level, gtime, guessList[level], shouldSkip);
		//for (int i = 0; i < cset.size(); i++)
		//	printf("  %s\n", words[ cset[i].no ], cset[i].no);

		if (shouldSkip)
			f(level+1, gtime, set, guessList, reNo, reDeep);
		else {
			int gadd;
			vector<A> tmpSet;
			tmpSet.push_back(cset[0]);
			gadd = notContain(words[cset[0].no], guessList[level]);

			for (int i = 1; i <= cset.size(); i++) {
				aCompareKey = guessList[level];
				if (i == cset.size() || cset[i] != cset[i-1]) {
					int tNo = INF, tDeep = 0;
					f(level+1, gtime+gadd, tmpSet, guessList, tNo, tDeep);
					//printf("level=%d update: %d %d (i=%d)\n", level, tDeep, tNo, i);
					if (tDeep > reDeep || (tDeep == reDeep && tNo < reNo)) {
						reDeep = tDeep;
						reNo = tNo;
						//printf("level=%d update: %d %d (i=%d)\n", level, tDeep, tNo, i);
					}
					tmpSet.clear();
				}	
				if (i < cset.size()) {
					tmpSet.push_back(cset[i]);
					gadd = notContain(words[cset[i].no], guessList[level]);
				}
			}
		}
	}

}

int main() {
	int ecase, ecount;

	scanf("%d", &ecase);
	for (ecount = 1; ecount <= ecase; ecount++) {
		int ed, el;
		scanf("%d%d", &ed, &el);
		for (int i = 0; i < ed; i++)
			scanf("%s", words[i]);
		fprintf(stderr, "case=%d, ed=%d, el=%d\n", ecount, ed, el);

		vector<A> lno[100];
		for (int j = 0; j < ed; j++) {
			int len = strlen(words[j]);
			lno[len].push_back(A(j));
		}
		
		printf("Case #%d:", ecount);
		for (int i = 0; i < el; i++) {
			char eguess[100];
			scanf("%s", eguess);
			int nno = INF, ndeep = 0;

			for (int j = 0; j < 100; j++) {
				int tno, tdeep;
				f(0, 1, lno[j], eguess, tno, tdeep);
				if (tdeep > ndeep || (tdeep == ndeep && tno < nno)) {
					ndeep = tdeep;
					nno = tno;
					//printf("-->%d -- %d %d\n", j, ndeep, nno);
				}
			}
			printf(" %s", words[nno]);
		}
		printf("\n");
	}

	return 0;
}
