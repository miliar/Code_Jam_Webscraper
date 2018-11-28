#include <iostream>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>

using namespace std;

#define FOR(i,a,b)  for(int i=(a);i<(b);++i)
#define F(i,a)      FOR(i,0,a)
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define S           size()

int unViaje(queue<int>&q, int k){
	queue<int> aux;
	int sum = 0;
	while(!q.empty()){
		if(sum + q.front() > k)
			break;
		sum += q.front();
		aux.push(q.front());
		q.pop();
	}
	while(!aux.empty()){
		q.push(aux.front());
		aux.pop();
	}
	return sum;
}

int solve(queue<int> q, int r, int k){
	int sum = 0;
	F(i, r){
		sum += unViaje(q, k);
	}
	return sum;
}

int main() {
//	freopen("c.in", "r", stdin);
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	int ca, r, k ,n, aux;
	scanf("%d", &ca);
	F(caso, ca){
		printf("Case #%d: ", caso+1);
		scanf("%d %d %d", &r, &k, &n);
		queue<int> q;
		F(i, n){
			scanf("%d", &aux);
			q.push(aux);
		}
		cout<<solve(q, r, k)<<endl;
	}
}
