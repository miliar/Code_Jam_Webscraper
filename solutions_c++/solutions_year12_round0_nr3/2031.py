/*
permutations - which permutations
assume:
restrict to 4 digits
10 P 4
10^4 combinations - those with leading 0 i.e. 1 * 3^10

asking for: pairs
A and B have the same no of digits
O(n) required
(log10(N)) ! ways to permutate i.e. 7! = 5040 ways
7! * N
only consider numbers in lexicographical order of digits

for i = A to B
	chop up digits
	check lexicographical order
	

recursion
is recursion (DFS) faster or to looping through the nos and checking?


*/
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <set>
using namespace std;

int A,B, digits, ans, fz;
int cA[10], cB[10];
int no[10], tmp, ttl;
//bool chk[2000100];
set<int> chk;
void dfs(int depth) {
	int i, tt, cnt, qq;
	if(depth == digits) {
		tmp = ttl;
//		fprintf(stderr, "%d\n", ttl);
//		memset(chk, 0, sizeof(chk));
		chk.clear();
		for(i=0;i<digits-1;i++) {
			tmp += fz * (tmp % 10);
			tmp /= 10;
			if( A <= tmp && tmp <= B && tmp > ttl && !chk.count(tmp)) {
//				fprintf(stderr, "%d\t%d\n", ttl, tmp);
				ans++;
				chk.insert(tmp);
			}
		}
	} else {
		for(i=0;i<10;i++) {
			no[depth] = i;
			ttl = ttl * 10 + i;
			if(cA[depth] <= ttl && ttl <= cB[depth]) dfs(depth+1);
			ttl /= 10;
		}
	}
}

int main() {
	int t,tc,i, ta, tb;
	scanf("%d",&tc);
	for(t=0;t<tc;t++) {
		ans = 0;
		scanf("%d %d", &A, &B);
		digits = log10(A)+1;
		for(i=0,fz=1;i<digits;i++) fz *= 10;
		ta = A; tb = B;
		for(i=digits-1;i>=0;i--) {
			cA[i] = ta;
			cB[i] = tb;
			ta /= 10;
			tb /= 10;
		}
		dfs(0);
		printf("Case #%d: %d\n", t+1, ans);
	}
	return 0;
}
