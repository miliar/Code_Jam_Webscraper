//Catch me if you can!
#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<deque>
#include<string>
#include<cctype>
#include<cmath>
#include<string>
#include<sstream>
#include<numeric>
#include<complex>
#include<cassert>
#include<queue>
using namespace std;

#define big long long
#define EPS 1e-9
#define s(x) ((int)(x).size())
#define all(x) (x).begin(), (x).end()

const int SIZE = 10005;
int D[SIZE], L[SIZE], N, G;
bool vis[SIZE];

int main(){

	//freopen("1.in", "rt", stdin);
	//freopen("1.out", "wt", stdout);
	//freopen("A-small-attempt1.in", "rt", stdin);
	//freopen("A-small-attempt1.out", "wt", stdout);
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);

	int tt; scanf("%d ", &tt);
	for(int t = 0 ; t < tt ; t++){
		cerr << "Solving testcase " << t+1 << endl;
		cin >> N;
		for(int i = 0 ; i < N ; i++)
			cin >> D[i] >> L[i];
		cin >> G;

		memset(vis, 0, sizeof vis);
		queue<pair<int, int> > q;

		q.push(make_pair(0, D[0]));
		vis[0] = true;
		bool ok = false;
		while(!q.empty()){
			pair<int, int> p = q.front(); q.pop();
			int i = p.first, w = p.second;
			if(D[i]+w >= G){
				ok = true;
				break;
			}
			for(int j = i+1 ; j < N ; j++){
				if(D[i]+w < D[j])break;
				int d = D[j]-D[i];
				d = min(d, L[j]);
				if(!vis[j]){
					pair<int, int> pp = make_pair(j, d);
					q.push(pp);
					vis[j] = true;
				}
			}
		}

		if(ok)
			printf("Case #%d: YES\n", t+1);
		else
			printf("Case #%d: NO\n", t+1);
	}

	return 0;
}
