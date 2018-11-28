#include <cstdio>
#include <set>
#define h 1111

using namespace std;

class tree {
public:
	int value;
	int a,b;
	bool have;
};

inline int left(int i) { return i * 2 + 1; }
inline int right(int i) { return i * 2 + 2; }

int c,t,n,p,i,j,k,m[h],x[13];
tree T[h*h];

void init(int ind, int a, int b) {
	T[ind].a = a;
	T[ind].b = b;
	T[ind].have = false;
	if(a < b) {
		init(left(ind), a, (a + b) / 2);
		init(right(ind), (a + b) / 2 + 1, b);
	}
	scanf("%d", &T[ind].value);
}

void buy(int ind, int team) {
	if(!T[ind].have) {
		T[ind].have = true;
		k += T[ind].value;
		for(int i=2*T[ind].a;i<=2*T[ind].b+1;i++)
			m[i] ++;
	}
	if(m[team] < p) {
		if(team > T[ind].a + T[ind].b)
			buy(right(ind), team);
		else
			buy(left(ind), team);
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	x[0] = 1;
	for(i=1;i<11;i++)
		x[i] = x[i-1] * 2;

	scanf("%d", &t);
	for(c=1;c<=t;c++) {
		scanf("%d", &p);
		n = x[p];
		for(i=0;i<n;i++)
			scanf("%d", &m[i]);
		init(0, 0, n / 2 - 1);
		k = 0;
		for(i=0;i<n;i++)
			if(m[i] < p)
				buy(0, i);
		printf("Case #%d: %d\n", c, k);
	}
	return 0;
}