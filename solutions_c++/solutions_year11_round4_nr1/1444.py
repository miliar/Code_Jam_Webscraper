#include <cmath>
#include <ctime>
#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <cctype>
#include <stack>
using namespace std;

typedef long long int int64;

#define EPS 10e-8

int x, s, r, n;

typedef struct Walk {
	int b, e, v;	
}Walk;

Walk walk[1500];

typedef struct Corredor {
	int ds, v;
}Corredor;

bool comp(Walk a, Walk b) {
	return a.b < b.b;	
}

bool comp2(Corredor a, Corredor b) {
	return a.v < b.v;
}

vector<Corredor> solucao;

int main()
{	
	int t;
	scanf("%d", &t);
	for (int k = 0; k < t; k++) {
		double tempo;
		scanf("%d %d %d %lf %d", &x, &s, &r, &tempo, &n);
		for (int i = 0; i < n; i++) {
			scanf("%d %d %d", &(walk[i].b), &(walk[i].e), &(walk[i].v));
		}
		sort(walk, walk + n, comp);	
		int i = 0;
		solucao.clear();
		int j = 0;
		Corredor cor;
		while (1) {
			if (i == x) break;
			if (j == n) {
				cor.ds = x - i;
				cor.v = s;
				//printf("%d %d\n", cor.ds, i);
				solucao.push_back(cor);
				break;
			}
			//printf("%d %d %d\n", j, walk[j].b, i);
			if (walk[j].b == i) {
				cor.ds = walk[j].e - walk[j].b;
				cor.v = walk[j].v + s;
				solucao.push_back(cor);
				i = walk[j].e;
				j++;
				//printf("%d %d %d\n", i, j, cor.ds);
			}
			else {
				cor.ds = walk[j].b - i;
				cor.v = s;
				
				solucao.push_back(cor);
				i = walk[j].b;
			}	
		}
		sort(solucao.begin(), solucao.end(), comp2);
		double res = 0;
		double total;
		double des;
		for (int i = 0; i < solucao.size(); i++) {
			//printf("%d %d\n", solucao[i].ds, solucao[i].v);
			if (!(fabs(tempo) <= EPS)) {
				total = (double) solucao[i].ds / (double) (solucao[i].v + r - s);
				if (!(tempo + EPS < total)) {
					res = res + total;
					tempo = tempo - total;
				}
				else {
					res = res + tempo;
					des = (solucao[i].v + r - s) * tempo;
					res = res + (double) (solucao[i].ds - des) / (double) solucao[i].v;
					tempo = 0;	
				}
			}
			else {
				total = (double) solucao[i].ds / (double) (solucao[i].v);
				res = res + total;		
			}
		}
		printf("Case #%d: %.10lf\n", k+1, res);
	}
	return 0;
}