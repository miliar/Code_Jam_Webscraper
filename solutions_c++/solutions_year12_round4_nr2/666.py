#include <cstdio>
#include <memory.h>
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <cctype>
#define pb push_back

using namespace std;
typedef long long ll;
const int N = 1000000;

int i, j, t, n, cnt;
int w, h, x, y, r;
int X[N], Y[N], R[N];

int getRandom(int v){
	return (rand() * 10000 + rand()) % (v + 1);
}

double SQR(int v){
	return 1.0 * v * v;
}

int main(){
	srand(3);
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for (int testcase = 1; testcase <= t; testcase++){
		printf("Case #%d:", testcase);
		scanf("%d %d %d",&n, &w, &h);
		for (i = 0; i < n; i++){
			scanf("%d", &r);
			bool l = false;
			while (!l){
				x = getRandom(w);
				y = getRandom(h);
				l = true;
				for (j = 0; j < i; j++)
					if ( SQR(X[j] - x) + SQR(Y[j] - y) < SQR(r + R[j])){
						l = false;
						break;
					}
				if (!l) continue;
				X[i] = x;
				Y[i] = y;
				R[i] = r;
				break;
			}
		}
		for (i = 0; i < n; i++)
			printf(" %d %d", X[i], Y[i]);
		printf("\n");
	}
	return 0;
}