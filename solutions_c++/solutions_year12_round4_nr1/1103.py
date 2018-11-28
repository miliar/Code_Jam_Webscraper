#include<iostream>
#include<fstream>
#include<sstream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<cstring>
using namespace std;

#define FOR(I,A,B) for (int I=int(A);I<int(B);++I)
#define MEM(A,B) memset(A,B,sizeof(A));
#define CPY(A,B) memcpy(A,B,sizeof(B));
typedef long long LL;
const int N(10010);
bool bo[N];
int n, ca;
int D[N], I[N], q[N], d[N];
int nxt(int x) {return (x + 1) % N;}
bool check()
{
	 int t = 0;
	 MEM(d, 0);
	 MEM(bo, 0);
	 q[t++] = 0; bo[0] = true;  d[0] = D[0];
	 for (int h = 0; h != t; h = nxt(h)) {
	 	 if (d[q[h]] + D[q[h]] >= D[n - 1]) return true;
	 	 FOR(i, 0, n) {
	 	 	if (i == q[h]) continue;
	 	    int sw = abs(D[q[h]] - D[i]);
	 	    if (sw <= d[q[h]] && I[q[h]] + I[i] >= sw && d[i] < min(I[i], sw)) {
	 	       d[i] = min(I[i], sw);
	 	   	   if (!bo[i]) {
	 	   	      bo[i] = true;
	 	   	      q[t] = i;
	 	   	      t = nxt(t);
	 	   	   } 
	 	   	}
	 	 }
	     bo[q[h]] = 0;
	 }
	 return false;
}
int main()
{
	int c = 0;
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	for (scanf("%d", &ca); ca; --ca) {
	    scanf("%d", &n);
	    FOR(i, 0, n) 
	       scanf("%d%d", &D[i], &I[i]);
	    scanf("%d", &D[n]);
	    I[n] = 0;
	    n++;
	    printf("Case #%d: ", ++c);
	    if (check()) printf("YES\n");
	    else printf("NO\n");
	}
	return 0;
}
