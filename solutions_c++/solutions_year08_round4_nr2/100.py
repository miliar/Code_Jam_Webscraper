#include <cstdio>
#include <cstring>
#include <cassert>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>

#define Eo(x) { std::cerr << #x << " = " << x << std::endl; }
#define inf 0x3f3f3f3f

#define maxn 11000

using namespace std;

typedef long long int64;

typedef double real;

int n, m, a;
int x1, y1, x2, y2, x3, y3;


int calc(){
 	return abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1));
}

void Out(){
 	printf("%d %d %d %d %d %d\n", x1, y1, x2, y2, x3, y3);
}

bool get(int x, int y){
	x1 = x;
	y1 = y;
	for (x2 = 0; x2 <= n; x2++)
		for (y2 = 0; y2 <= m; y2++)
			for (x3 = 0; x3 <= n; x3++)
				for (y3 = 0; y3 <= m; y3++){
					if (calc() == a) return 1;
				}
	return 0;
}

int main() {
	int ferlon;
	scanf("%d", &ferlon);
	int _;
	for (_ = 0; _ < ferlon; ++_){
		scanf("%d%d%d", &n, &m, &a);
		printf("Case #%d: ", _ + 1);
		if (get(0, 0)) Out();
		else if (get(0, m)) Out();
		else if (get(n, 0)) Out();
		else if (get(n, m)) Out();
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
