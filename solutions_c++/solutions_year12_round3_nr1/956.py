#include<iostream>
#include<vector>
#include<map>
#include<sstream>
#include<math.h>
#include<set>
#include<fstream>
#include<algorithm>
#include<cstring>
#include<cassert> 
#include <list>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;


#define debug(x) cout << #x << " = " << x << "\n";
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define sz size()
#define pb push_back
#define mp make_pair
#define fr(i, n) for(i=0;i<n;i++)
#define fr2(i, a, n) for(i=a;i<n;i++)
#define mem(a, n) memset(a, n, sizeof(a))
typedef vector<int> VI;
int n;
const int mx = 1001;
vector<int> v[mx];
#include<queue>
bool solve(int id) {
	queue<int> q;
	q.push(id);
	bool vis[1001] = {0};
	vis[id] = 1;
	while(! q.empty()) {
		int cur = q.front();
		q.pop();
		for(int i=0;i<v[cur].size();i++) {
			if(vis[v[cur][i]])
				return 1;
			q.push(v[cur][i]);
			vis[v[cur][i]] = 1;
		}
	}
	return 0;
}
void print() {
	int i, j;
	cout << endl;
	fr(i, n) {
		cout << i << " -> ";
		fr(j, v[i].sz) {
			cout << v[i][j] << " ";
		}
		cout << endl;
	}
}

int main() {
	int t;
	scanf("%d", &t);
	for(int k=1;k<=t;k++) {
		scanf("%d", &n);
		int i;
		for(int i=0;i<mx;i++)
			v[i].clear();
		int l;
		fr(i, n) {
			scanf("%d", &l);
			int j;
			fr(j, l) {
				int x;
				scanf("%d", &x);
				v[x-1].pb(i);
			}
		}	
//		print();
		bool b = 0;
		for(int i=0;i<n;i++) {	
			b = solve(i);
			if(b)
				break;
		}
			
		printf("Case #%d: ", k);
		if(b) {
			printf("Yes\n");
		}
		else {
			printf("No\n");
		}
	}
}
