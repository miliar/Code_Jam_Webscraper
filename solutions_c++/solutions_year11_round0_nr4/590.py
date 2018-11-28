#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <cmath>
using namespace std;
int main() {
	int T;
	scanf("%d",&T);
	for(int cn=1;cn<=T;++cn) {
		int N, s = 0;
		scanf("%d",&N);
		for(int i=1;i<=N;++i) {
			int a;
			scanf("%d",&a);
			if(a != i) ++s;
		}
		printf("Case #%d: %d\n",cn,s);
	}
}
