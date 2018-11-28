#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cassert>
#include <string>
#include <cmath>
#include <iostream>
#include <stack>
#include <queue>
#include <ctime>
#include <utility>
#include <bitset>
#include <memory.h>
#include <list>
#include <deque>

using namespace std;

#define pb push_back
#define mp make_pair
#define rep(i, n) for (int (i) = 0; (i) < (n); (i)++)
#define forn(i, a, b) for (int (i) = a; (i) < (b); (i)++)
#define ford(i,a,b) for (int i(a);i>=(b);--i)
#define sqr(n) (n)*(n)
#define all(v) (v).begin(), (v).end()
#define mem0(a) memset(a,0,sizeof(a))
#define mem1(a) memset(a,-1,sizeof(a))

#define INF 2000000000

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef pair<int, int> pii;

int GCD(int A, int B){
	return B==0?A:GCD(B,A%B);
}

int main()
{
	//freopen("A-small.in","r",stdin);
	//freopen("A-small.out","w",stdout);

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int T;
	scanf("%d",&T);
	for(int z = 0; z < T; z++){
		long long N;
		int Pd,Pg;
		bool flag = true;
		scanf("%lld%d%d",&N,&Pd,&Pg);
		if(Pg==0&&Pd!=0)
			flag = false;
		if(Pg==100&&Pd!=100)
			flag = false;
		int g = GCD(100,Pd);
		int d = 100/g;
		if((long long)d>N)
			flag = false;


			
		printf("Case #%d: ",z+1);


		if(flag)
			printf("Possible");
		else
			printf("Broken");
		printf("\n");
	}

	return 0;
}