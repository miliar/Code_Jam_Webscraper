#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

#define pii pair<int,int>

int t;
int na, nb;
vector< pii > a, b;

bool comp(pii p, pii q) { return p.first < q.first || (p.first == q.first && p.second < q.second); }

void fun(int turn, int hora) {
	if(turn == 0 && a.size() == 0) return;
	if(turn == 1 && b.size() == 0) return;
	if(turn == 0) {
		for(int i=0; i<a.size(); i++) {
			if(a[i].first >= hora+t) {
// 				printf("a:%d ", i);
				fun(1, a[i].second);
				a.erase(a.begin()+i);
				return;
			}
		}
	} else {
		for(int i=0; i<b.size(); i++) {
			if(b[i].first >= hora+t) {
// 				printf("b:%d ", i);
				fun(0, b[i].second);
				b.erase(b.begin()+i);
				return;
			}
		}
	}
// 	printf("\n");
	return;
}

int main(void)
{
	int casos, i, j, k;
	int h1, h2, m1, m2;
	scanf("%d", &casos);
	for(int caso = 1; caso <= casos; caso++) {
		scanf("%d", &t);
		scanf("%d %d", &na, &nb);
		a.clear(); b.clear();
		
		for(i=0; i<na; i++) {
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
			a.push_back(make_pair(h1*60+m1, h2*60+m2));
		}
		for(i=0; i<nb; i++) {
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
			b.push_back(make_pair(h1*60+m1, h2*60+m2));
		}
		
		sort(a.begin(), a.end(), comp);
		sort(b.begin(), b.end(), comp);
		
		int ra = 0, rb = 0;
		while(a.size() > 0 || b.size() > 0) {
			if(a.size() == 0) { rb += b.size(); /*printf("rest-b: %d\n", a.size()); */break; }
			if(b.size() == 0) { ra += a.size(); /*printf("rest-a: %d\n", b.size()); */break; }
			if(comp(a[0], b[0])) fun(0, -100), ra++;
			else fun(1, -100), rb++;
		}
		
		printf("Case #%d: %d %d\n", caso, ra, rb);
	}
	
	return 0;
}
