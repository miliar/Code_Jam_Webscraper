#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>


using namespace std;

#define INF 999999
#define pb push_back
#define sz(x) ((int)((x).size()))
#define all(x) (x).begin(),(x).end()
#define db double
#define ll long long
#define rep(i,n) for (int (i)=0; (i)<(n); ++(i))
#define forn(i,a,n) for (int (i)=(a); (i)<(n); ++(i))
#define VI vector<int>
#define VB vector<bool>
#define MAXN 1024
#define MAXNN (2*N-1)
int N,NN;

int mas[2047];
#define EPS 10E-5
int P;
int main(){
	freopen("input.txt","rt",stdin); freopen("output.txt","wt",stdout);
	int C;
	scanf("%d",&C);
	int tmp;
	rep(qwer,C){
		scanf("%d",&P);
		N = 1 << P;
		NN = 2*N - 1;
		for (int i = N - 1; i < NN; ++ i)
			scanf("%d",&mas[i]);
		rep(i,N-1)
			scanf("%d",&tmp);
		
		rep(i,N-1)
			mas[i] = 0;
		int ans = 0;
		for (int i = N-1; i < NN; ++ i){
			int cnt = mas[i];
			if (cnt == P)
				continue;
			
			int p = (i-1) >> 1;
			rep(j,cnt)
				p = (p-1) >> 1;
			while (p > 0){
				if (!mas[p])
					++ans;
				mas[p] = 1;
				p = (p-1) >> 1;
			}
			if (!mas[0])
				++ans;
			mas[0] = 1;
		}
		printf("Case #%d: %d\n",qwer+1,ans);
	}
	return 0;
}