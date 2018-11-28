#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <queue>
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

int X,S,R,T,N;
int spaces[102];

double process() {
	scanf("%d%d%d%d%d", &X, &S, &R, &T, &N);
	memset(spaces, 0, sizeof(spaces));
	
	int b,e,w;
	for (int i = 0; i < N; i++) {
		scanf("%d%d%d", &b, &e, &w);
		spaces[w] += e-b;
		X -= e-b;
	}
	spaces[0] = X;
	double runningtime = T;
	double answer = 0;
	double maxspace;
	double temptime;
	for (int i = 0; i <= 100; i++) {
		if (spaces[i]) {
			if (runningtime > 0) {
				maxspace = (i+R)*runningtime;
				if (maxspace > spaces[i]) {
					// run all
					temptime = ((double)spaces[i])/(i+R);
					runningtime -= temptime;
					answer += temptime;
				} else {
					// run all time
					answer += runningtime;
					runningtime = 0;
					answer += (spaces[i]-maxspace)/(S+i);
				}
			} else {
				answer += ((double)spaces[i])/(S+i);
			}
		}
	}
	return answer;
}

int main() {
	
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int T;
	scanf("%d", &T);
	for (int i = 0 ; i < T ; i++) {
		printf("Case #%d: %.10lf\n", i+1, process());
	}
	
	return 0;
}
