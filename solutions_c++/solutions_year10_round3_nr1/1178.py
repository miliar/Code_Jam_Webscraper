#include <algorithm>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <list>
#include <numeric>
#include <map>
#include <queue>
#include <string>
#include <sstream>
#include <set>
#include <vector>
#include <stdio.h>
#include <string.h>


using namespace std;


int wires[10001];
int N;

int check_wire(int p1, int p2) {
	int res=0;
	for (int i=1;i<=10000;i++) {
		
		if (i!=p1&&wires[i]) {
			if (p1<i&&p2>wires[i]) res++;
			if (p1>i&&p2<wires[i]) res++;
		}
	}
	return res;
}



int main() {
	int t, n, cas=0;
	cin >> t;
	int p1, p2;
	int score=0;
	while (cas++<t) {
		cin >> N;
		
		memset(wires, 0, sizeof(wires));
		
		score=0;
		n=0;
		while (n++<N) {
			cin >> p1;
			cin >> p2;
			score+=check_wire(p1,p2);
			wires[p1]=p2;
		}
		printf("Case #%d: %d\n", cas, score);
	}
	return 0;
}

