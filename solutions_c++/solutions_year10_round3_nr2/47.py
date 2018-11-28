#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <list>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <valarray>
#include <ctime>
#include <set>
#include <sstream>

using namespace std;

typedef pair<int, int> PII;
typedef unsigned long long ULL;


void solution(int tstNum){
	ULL l, p, c;
	scanf("%llu%llu%llu", &l, &p, &c);
	int dif = 0;
	ULL t = l;

	while (t * c < p){
		t *= c;
		++dif;
	}
	//fprintf(stderr, "%d\n", tstNum);
	
	int res = ceil(log(dif + 1.0) / log(2.0));
	printf("Case #%d: %d\n", tstNum + 1, res);
}

int main(){

	//freopen("A-small.in", "rt", stdin);
	//freopen("A-small.out", "wt", stdout);

	//freopen("A-large.in", "rt", stdin);
	//freopen("A-large.out", "wt", stdout);

	//freopen("B-small.in", "rt", stdin);
	//freopen("B-small.out", "wt", stdout);

	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);


	//freopen("C-small.in", "rt", stdin);
	//freopen("C-small.out", "wt", stdout);

	//freopen("C-large.in", "rt", stdin);
	//freopen("C-large.out", "wt", stdout);

	int t = 0;
	scanf("%d", &t);
	for (int tt = 0; tt < t; tt++){
		solution(tt);
	}

	return 0;
}