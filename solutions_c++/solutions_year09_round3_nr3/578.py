#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <cmath>
#include <memory.h>

using namespace std;

#define ffcOR(i,a,b) for(int i=a; i<b; ++i)

#define FILL(a, val) memset(a, val, sizeof(a))

#define pb push_back
#define sz(c) (int)c.size()
#define all(c) c.begin(),c.end()

#define mp make_pair
#define X first
#define Y second

typedef long int Int;
typedef vector<int> VI;
typedef pair<int, int> PII;

const int INF = 1000000000;
const double PI = acos(-1.0);

int a[100000];
bool b[100000];
int n, m;

int calc_res(){
	int res = 0;
	FILL(b, 1);
	ffcOR(i, 0, m){
		int j = a[i];
		while (j>=0 && b[j]==true){
			--j;
			++res;
		}
		j = a[i];
		while (j<n && b[j]==true){
			++j;
			++res;
		}
		res -=2;
		b[a[i]] = false;
	}
		
	return res;
}

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	ffcOR(t, 0, T){
		
		scanf("%d%d", &n, &m);
		ffcOR(i, 0, m){
			scanf("%d", &a[i]);
			--a[i];
		}
		sort(a, a+m);
		int res=INF;
		res = min(calc_res(), res);
		while (next_permutation(a, a+m)){
			res = min(calc_res(), res);
		}
		printf("Case #%d: %d\n", t+1, res);
	}
	return 0;
}