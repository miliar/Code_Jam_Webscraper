//Maked by diver_ru, maked with love^^
#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>

FILE *fi = fopen("input.txt", "r"), *fo = fopen("output.txt", "w");

using namespace std;

typedef int int64;

const int MAXN = 1010;

int64 a, b, p;

int64 root[MAXN];

int answer;

void readData()
{
	//fscanf(fi, "%lld%lld%lld", &a, &b, &p); //!!!
	fscanf(fi, "%d%d%d", &a, &b, &p); //!!!
	for (int i = 0; i < MAXN; ++i)
		root[i] = i;
}

int64 getRoot(int64 v)
{
	if (root[v] != v)
		root[v] = getRoot(root[v]);
	return (root[v]);
}

bool isPrime(int a)
{
	if (a == 2)
		return (true);
	for (int i = 2; i * i <= a; ++i)
		if (a % i == 0)
			return (false);
	return (true);
}

void solve()
{
	answer = b - a + 1;
	for (int64 i = p; i <= b; ++i){
		if (isPrime(i)){
			int64 first = a + (i - a % i) % i;
			for (int64 j = first + i; j <= b; j += i){
				int64 r1 = getRoot(first), r2 = getRoot(j);
				if (r1 != r2){
					root[r1] = r2;
					--answer;
				}
			}
		}
	}	
}

void writeResult()
{
	fprintf(fo, "%d\n", answer);
}

int main()
{
	int T;
	fscanf(fi, "%d", &T);
	for (int i = 0; i < T; ++i){
		readData();
		solve();
		fprintf(fo, "Case #%d: ", i + 1);
		writeResult();
	}
	return 0;
}