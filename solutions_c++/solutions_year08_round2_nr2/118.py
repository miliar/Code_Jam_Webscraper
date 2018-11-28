#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

#define sqr(a) ((a)*(a))
#define ab(a) (((a)>0)?(a):(-(a)))
#define dist2(x1, y1, x2, y2) (sqr((x1)-(x2)) + sqr((y1)-(y2)))
#define PB push_back
#define SZ size()
#define ALL(a) (a).begin(),(a).end()
#define mset(a, val) memset(a, val, sizeof(a))

#define pii pair < int, int >
#define MP make_pair
#define X first
#define Y second 

#define TYPE long long

TYPE A, B, P;

#define N 1000111

int rank[N], parent[N], n;
bool used[N];

void init() {
	for (int i = 0; i < n; i++) rank[i] = 0, parent[i] = i;
}

inline int mfind(int x) {
	if (x != parent[x]) parent[x] = mfind(parent[x]);
	return parent[x];
}

inline void munion(int A, int B) {
	A = mfind(A), B = mfind(B);
	if (A == B) return;
	if (rank[A] > rank[B]) {
		parent[B] = A;
	}
	else {
		parent[A] = B;
		if (rank[A] == rank[B]) rank[B]++;
	}
}

int prime[] = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997};

int main () {
	int i, j, T;

	scanf("%d", &T);
	TYPE x, y;
	
	for (int cas = 1; cas <= T; cas++) {
		scanf("%lld%lld%lld", &A, &B, &P);

		n = B-A+1;

		init();

		for (x = A; x <= B; x++) for (y = x+1; y <= B; y++) {
			for (i = 0; prime[i] <= x; i++) if (prime[i] >= P) {
				if ( x % prime[i] == 0 && y % prime[i] == 0 ) {
					munion( x-A, y-A );
				}
			}
		}

		mset(used, 0);
		int res = 0;

		for (i = 0; i < n; i++) used[ mfind(i) ] = true;
		for (i = 0; i < n; i++) if (used[i]) res++;

		printf("Case #%d: %d\n", cas, res);
	}

	return 0;
}
