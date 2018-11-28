#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>
#define MAXC 100
#define MAXD 100
#define MAXN 1000
#define FOR(A,B) for(A = 0; A < B; A++)
using namespace std;

typedef struct {
	char a,b;
	char res;
} combin;

typedef struct {
	char a, b;
} oppo;

int main()
{
	int T;
	scanf("%d", &T);
	int t = 0;
	FOR(t, T) {
		int C, D, N,i,j,k,l;
		combin combs[MAXC];
		oppo opps[MAXD];
		scanf("%d", &C);
		FOR(i, C) {
			char in[3];
			scanf("%s", in);
			combs[i].a = in[0];
			combs[i].b = in[1];
			combs[i].res = in[2];
		}
		scanf("%d", &D);
		FOR(i, D) {
			char in[3];
			scanf("%s", in);
			opps[i].a = in[0];
			opps[i].b = in[1];
		}
		scanf("%d", &N);
		char str[1001];
		scanf("%s", str);
		vector<char> elements;
		FOR(i, N) {
			bool ok = false;	
			FOR(j, C) if(elements.size() > 0 && ((elements[elements.size()-1] == combs[j].a && str[i] == combs[j].b) || (elements[elements.size()-1] == combs[j].b && str[i] == combs[j].a))) { elements.pop_back(); elements.push_back(combs[j].res); ok = true; break;}
			if(ok) continue;
			FOR(j, D) if((opps[j].a == str[i] && find(elements.begin(), elements.end(), opps[j].b) != elements.end()) || (opps[j].b == str[i] && find(elements.begin(), elements.end(), opps[j].a) != elements.end())) { elements.clear(); ok = true; break; }
			if(ok) continue;

			elements.push_back(str[i]);
		}
		printf("Case #%d: [", t+1);
		FOR(i, elements.size()) {
			printf("%c", elements[i]);
			if(i != elements.size()-1)
				printf(", ");
		}
		printf("]\n");
	}
	return 0;
}
