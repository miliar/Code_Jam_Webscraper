#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <fstream>
#include <math.h>
#include <limits>
#include <set>
#include <map>
#include <sstream>
#include <stdio.h>
#include <time.h>
#include <memory.h>
#include <cassert>
using namespace std;

#define ALL(ar)       (ar).begin(),(ar).end()
#define SZ(a)         int((a).size())
#define MP(a,b)       make_pair(a,b)
#define SQR(a)        ((a)*(a))
#define x             first
#define y             second
#define INF           0x7f7f7f7f
#define DEB(k)        cout<<"debug: "#k<<"="<<k<<endl;
typedef long long     LL;
typedef vector<int>   VI;
typedef pair<int,int> II;

int r, k, n;
int g[1000];
int next[1000];
LL add[1000];

void solution(int test) {
   scanf("%d %d %d", &r, &k, &n);
   for (int i = 0; i < n; i++)
      scanf("%d", g+i);
   for (int i = 0; i < n; i++) {
      add[i] = 0;
      int j = 0;
      while (j < n && add[i]+g[j] <= k)
         add[i] += g[j], j++;
      next[i] = (i+j)%n;
      rotate(g, g+1, g+n);
   }
   LL tot = 0;
   int cur = 0;
   for (int i = 0; i < r; i++) {
      tot += add[cur];
      cur = next[cur];
   }
   printf("Case #%d: %lld\n", test, tot);
}

void codejam() {
   int t;
   scanf("%d\n", &t);
   for (int i = 0; i < t; i++)
      solution(i+1);
}

int main()
{
	freopen("C-large.in", "rt", stdin);
   freopen("C-large.out", "wt", stdout);
	codejam();
	return 0;
}