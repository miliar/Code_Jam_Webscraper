#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

vector<int> prime;

FILE *f;
FILE *fin;

int a, b, p;

bool root[1001];
int prev[1001];

void init(){
	for (int i = 0; i <= 1000; i++){
		root[i] = true;
		prev[i] = 1;
	}
}

int group(int x){
	while (!root[x]) x = prev[x];
	return x;
}

void merge(int _x, int _y){
	int x = group(_x), y = group(_y);
	if (prev[x] > prev[y]){
		prev[x] += prev[y];
		prev[y] = x;
		root[y] = false;
	}
	else{
		prev[y] += prev[x];
		prev[x] = y;
		root[x] = false;
	}
}

//////

void detPrimes(){
	prime.push_back(2);
	for (int i = 3; i <= 1000; i+=2){
		bool p = true;
		for (int j = 2; j * j <= i; j++){
			if (i % j == 0){
				p = false;
				break;
			}
		}
		if (p) prime.push_back(i);
	}
}


bool conn(int a, int b){
	for (int i = 0; i < prime.size(); i++){
		if (prime[i] < p) continue;
		if (a % prime[i] == 0 && b % prime[i] == 0) return true;
	}
	return false;
}

void solve(int test){
	init();
	int res = b - a + 1;
	for (int i = a; i <= b; i++) for (int j = i + 1; j <= b; j++){
		if (conn(i, j)){
			int x = group(i), y = group(j);
			if (x != y){
				res--;
				merge(x, y);
			}
		}
	}
	
	fprintf(f, "Case #%d: %d\n", test, res);
}

int main(){
	detPrimes();
	
	f = fopen("B_small.out", "w");
	fin = fopen("B_small.in", "r");
	
	int C;
	fscanf(fin, "%d", &C);
	for (int test = 1; test <= C; test++){
		fscanf(fin, "%d %d %d", &a, &b, &p);
		solve(test);
	}
	
	fclose(f);
	fclose(fin);
	
	return 0;
}
