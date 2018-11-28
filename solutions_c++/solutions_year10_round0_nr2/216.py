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

int d[1000];

int gcd(int a, int b) {
   return b ? gcd(b, a%b) : a;
}

void solution(int test) {
   int n;
   scanf("%d", &n);
   for (int i = 0; i < n; i++)
      scanf("%d", d+i);
   sort(d, d+n, greater<int>());
   int g = d[0]-d[1];
   for (int i = 1; i < n-1; i++)
      g = gcd(g, d[i]-d[i+1]);
   int ret = (g-d[0]%g)%g;
   printf("Case #%d: %d\n", test, ret);
}

void codejam() {
   int t;
   scanf("%d\n", &t);
   for (int i = 0; i < t; i++)
      solution(i+1);
}

int main()
{
	freopen("B-small-attempt0.in", "rt", stdin);
   freopen("B-small-attempt0.out", "wt", stdout);
	codejam();
	return 0;
}