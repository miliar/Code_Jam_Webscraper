#include <iostream> 
#include <vector> 
#include <cstdio> 
#include <cstring> 
#include <algorithm> 
#include <set> 
#include <map> 
#include <queue> 
#include <stack> 
#include <string> 
#include <sstream> 
#include <ctime> 
#include <cmath> 

using namespace std; 

struct edge {
	int length;	int speed;
	edge(int a, int b) {
		length = a; speed = b;
	}
};

bool operator < (edge e1, edge e2) {
	return e1.speed < e2.speed;
}

int T, X, S, R, N, B[1005], E[1005], w[1005];
int te;
vector<edge> edges;

int main() { 
	FILE *fin = fopen("test.txt", "r");  
	FILE *fout = fopen("testans.txt", "w");
	
	fscanf(fin, "%d", &T);
	
	for (int z = 1; z <= T; z++) {
		edges.clear();
		fscanf(fin, "%d %d %d %d %d", &X, &S, &R, &te, &N);
		double t = (double)te;
		int totlen = 0;
		for (int i = 1; i <= N; i++) {
			fscanf(fin, "%d %d %d", &B[i], &E[i], &w[i]);
			edges.push_back(edge(E[i]-B[i], w[i]));
			totlen += (E[i]-B[i]);
		}
		int remlen = X - totlen;
		edges.push_back(edge(remlen, 0));
		sort(edges.begin(), edges.end());
		double ans = 0.0;
		for (vector<edge>::iterator it = edges.begin(); it != edges.end(); it++) {
			edge e = *it;
			double a = (double)e.length / (R+e.speed);
			//printf("%d %d\n", e.length, e.speed);
			//printf("%.2f\n", t);
			if (a <= t) {
				ans += a;
				t -= a;
			} else {
				ans += t;
				
				double remdist = e.length - (double)(R+e.speed)*t;
				t = 0;
				ans += remdist/(S+e.speed);
			}
			//printf("%f\n", ans);
		}
		//printf("Case #%d: %.7f\n", z, ans);
		fprintf(fout, "Case #%d: %.7f\n", z, ans);
	}
	
	
	
	
	//cin.get();
	
    return 0;
}

