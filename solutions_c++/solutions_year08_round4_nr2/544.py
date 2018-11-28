#include<cstdio>
#include<cstring>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include <list>
#include<queue>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
	int C,M,N,A;
	scanf("%d\n",&C);
	for(int ii=1;ii<=C;++ii) {
		scanf("%d %d %d\n",&N,&M,&A);
		bool found = false;
		printf("Case #%d: ",ii);
		for(int x1 = 0;x1 <=N;++x1) for(int x2 = 0;x2 <= N;++x2)
		for(int y1 = 0;y1 <=M;++y1) for(int y2 = 0;y2 <= M;++y2)
			if(x1*y2 - x2*y1 == A || x1*y2 - x2*y1 == -A) {
				found = true;printf("0 0 %d %d %d %d\n",x1,y1,x2,y2);goto L;
		}
L:
		if(!found) printf("IMPOSSIBLE\n");
	}
	return 0;
}
