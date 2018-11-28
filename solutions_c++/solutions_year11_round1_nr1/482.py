#include <cstdio>
#include <iostream>

using namespace std;

const int MAXN = 105;

int i, j, k, T, Pd, Pg;
int pt[MAXN], pc[MAXN], p1[MAXN], c1[MAXN];
long long N;

void init()
 {
 	cin >> N >> Pd >> Pg;
 	memset(pt, 0, sizeof(pt));
 	memset(pc, 0, sizeof(pc));
 }
 
void work()
 {
 	if (((Pd < 100) && (Pg == 100)) || ((Pd > 0) && (Pg == 0)))
 	 {
 	 	puts("Broken");
 	 	return;
 	 }
 	if (Pd == 0)
 	 {
 	 	puts("Possible");
 	 	return;
 	 }
 	for (i = Pd, j = 2; j <= 100; j ++)
 		if (i % j == 0)
 		 {
 		 	for (; i % j == 0; ++ pc[j], i /= j);
 		 }
 	for (i = 2, k = 1; i <= 100; i ++)
 		if (c1[i] > pc[i])
 		 {
 		 	for (; c1[i] > pc[i]; ++ pc[i], k *= i);
 		 }
 	if (k <= N) puts("Possible");
 	else puts("Broken");
 }
 
int main()
 {
 	freopen("A.in", "r", stdin);
 	freopen("A.out", "w", stdout);
 	for (i = 100, j = 2; j <= 100; j ++)
 		if (i % j == 0)
 		 {
 		 	for (; i % j == 0; ++ c1[j], i /= j);
 		 }
 	scanf("%d", &T);
 	for (int Case = 1; Case <= T; Case ++)
 	 {
 	 	printf("Case #%d: ", Case);
 	 	init();
 	 	work();
 	 }
 	return 0;
 }
