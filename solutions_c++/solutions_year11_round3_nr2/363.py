#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>

#define MP make_pair
#define ST first
#define ND second
#define PII pair<int,int>
#define PB push_back
#define VII vector<int>
#define VIT vector<int>::iterator
#define LL long long

using namespace std;

int testc;
int L, n, c;
LL T;

int dist[1000005];
/*
#define INF 1000000000

int solve1(int x){
    int sum = 0;
    for(int i = 0; i < n; i++){
	if(i == x){
	    if(sum >= T){
		if(dist[i] % 2 == 1)  return INF;
		else sum += (dist[i] / 2);
	    }
	    else if(sum + dist[i] > T){
		if((dist[i] - (T-sum)) % 2 == 1) return INF;
		else sum += (dist[i] - (T-sum)) / 2 + T - sum;
	    }
	    else{
		sum += dist[i];
	    }
	}
	else{
	    sum += dist[i];
	}
    }
    return sum;
}

int solve2(int x1, int x2){
    int sum = 0;
    int reszta = 0;
    for(int i = 0; i < n; i++){
	if(i == x1){
	    if(sum >= T){
		reszta = dist[i] % 2;
		sum += (dist[i] / 2);
	    }
	    else if(sum + dist[i] > T){
		reszta = (dist[i] - (T-sum)) % 2;
		sum += (dist[i] - (T-sum)) / 2 + T - sum;
	    }
	    else{
		sum += dist[i];
	    }
	}
	else if(i == x2){
	    if(sum >= T){
		if(dist[i] % 2 != reszta) return INF;
		else sum += (dist[i] / 2) + reszta;
	    }
	    else if(sum + dist[i] > T){
		if((dist[i] - (T-sum)) % 2 != reszta) return INF;
		else sum += (dist[i] - (T-sum)) / 2 + T - sum + reszta;
	    }
	    else{
		sum += dist[i];
	    }
	}
	else{
	    sum += dist[i];
	}
    }
    return sum;
}*/

int main(){
    scanf("%d", &testc);
  
    for(int tc = 1; tc <= testc; tc++){
	scanf("%d %lld %d %d", &L, &T, &n, &c);
	
	for(int i = 0; i < c; i++) scanf("%d", &dist[i]);
	for(int i = 0; i < c; i++) dist[i] *= 2;
	for(int i = c; i < n; i++) dist[i] = dist[i-c];

	LL res = 0LL;
	int start = 0;
	while(res < T && start < n){
	    res += dist[start];
	    start++;
	}
	
	if(start == n && res < T){
	    printf("Case #%d: %lld\n", tc, res);
	    continue;
	}
	
	if(res > T){
	    start--;
	    res -= dist[start];
	    LL temp = T - res;
	    res += temp;
	    dist[start] -= temp;
	}
	
	sort(dist+start, dist+n);
	
	LL plus = 0LL;
	for(int i = n-1; i >= start; i--){
	    if(L > 0){
		res += (dist[i] / 2);
		plus += dist[i] % 2;
		L--;
	    }
	    else{
		res += dist[i];
	    }
	}
	res += plus/2;

	printf("Case #%d: %lld\n", tc, res);
    }
    return 0;
}