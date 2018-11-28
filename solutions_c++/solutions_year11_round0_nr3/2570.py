#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <cstdio>
#include <cstdlib>

using namespace std;

#define	MAXDOCES	1010

typedef struct _soma {
	int sPatrick;
	int sSean;
} soma;

int c[MAXDOCES];
int n, somaTotal;
vector <soma> v;

int Resolve() {
	int i, j, max;
	soma a, b;

	v.clear();
	a.sPatrick = 0;
	a.sSean = 0;
	v.push_back(a);
	for(i=0; i < n; i++) {
		for(j=v.size()-1; j>=0; j--) {
			b.sPatrick = v[j].sPatrick ^ c[i];
			b.sSean = v[j].sSean + c[i];
			v.push_back(b);
		}
	}

//	for(i=0; i < v.size(); i++)
//		printf("%d %d\n", v[i].sPatrick, v[i].sSean);

	max = -1;
	for(i=1; i < v.size(); i++) {
		for(j=i+1; j < v.size(); j++)
			if(v[i].sPatrick == v[j].sPatrick && v[i].sSean + v[j].sSean == somaTotal) {
				if(v[i].sSean > max)
					max = v[i].sSean;
				if(v[j].sSean > max)
					max = v[j].sSean;
			}
	}

	return max;
}

int main (void) {
	int i, k, t, res;

	scanf("%d", &t);
	for(k=1; k <= t; k++) {
		scanf("%d", &n);
		somaTotal = 0;
		for(i=0; i < n; i++) { 
			scanf("%d", &c[i]);
			somaTotal += c[i];
		}

		if((res = Resolve()) != -1)
			printf("Case #%d: %d\n", k, res);
		else
			printf("Case #%d: NO\n", k);
	}

	return 0;
}
