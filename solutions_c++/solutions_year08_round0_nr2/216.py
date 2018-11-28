#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <utility>
#include <queue>

using namespace std;

#define maxn 2000


int x[maxn], da[maxn], db[maxn], ind[maxn];

bool cmp(int a, int b){
	if (x[a] != x[b]) return x[a] < x[b];
	if (da[a] != da[b]) return da[a] > da[b];
	if (db[a] != db[b]) return db[a] > db[b];
	return a < b;
}


int main(){
	int ferlon;
	scanf("%d", &ferlon);
	for (int _ = 0; _ < ferlon; ++_){
		int t;
		scanf("%d", &t);
		int na, nb;
		scanf("%d%d", &na, &nb);
		int i;
		int cnt = 0;
		for (i = 0; i < na + nb; i++){
			int h1, m1, h2, m2;
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);		
//			cerr << h1 << ' ' << m1 << ' ' << h2 << ' ' << m2 << endl;
			if (i < na){
				x[cnt] = h1 * 60 + m1;
				da[cnt] = -1;
				db[cnt] = 0;
				ind[cnt] = cnt;
				++cnt;
				
				x[cnt] = h2 * 60 + m2 + t;
				da[cnt] = 0;
				db[cnt] = 1;
				ind[cnt] = cnt;
				++cnt;
			}else{
				x[cnt] = h1 * 60 + m1;
				da[cnt] = 0;
				db[cnt] = -1;
				ind[cnt] = cnt;
				++cnt;
				
				x[cnt] = h2 * 60 + m2 + t;
				da[cnt] = 1;
				db[cnt] = 0;
				ind[cnt] = cnt;
				++cnt;
			}
		}
		sort(ind, ind + cnt, cmp);		
		int ansa = 0, ansb = 0;
		int cnta = 0, cntb = 0;
		for (i = 0; i < cnt; i++){
			cnta += da[ind[i]];
			cntb += db[ind[i]];
			if (cnta < 0){
				cnta++;
				ansa++;
			}
			if (cntb < 0){
				cntb++;
				ansb++;
			}
		}	
		printf("Case #%d: %d %d\n", _ + 1, ansa, ansb);
	}
	return 0;
}	
