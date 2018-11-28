//#include <iostream>
#include <fstream>
#include <sstream>
#include <set>
#include <list>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;

ifstream cin("B-large.in",ios::in);
ofstream cout("B-large.out",ios::out);

void go() {
	long long N, K, B, T;
	cin >> N >> K >> B >> T;
	long long * X = new long long [N];
	long long * V = new long long [N];
	for (int i=0; i<N; i++)
		cin >> X[i];
	for (int i=0; i<N; i++)
		cin >> V[i];
	vector <pair <long long, bool> > G;
	for (int i=0; i<N; i++) {
		if ((B-X[i]) <= T*V[i])
			G.push_back (make_pair(X[i], 1));
		else
			G.push_back (make_pair(X[i], 0));
	}
	sort(G.begin(), G.end());
	reverse(G.begin(), G.end());
	int ans = 0;
	int sw = 0;
	for (int i=0; i<N && K>0; i++) {
		if (G[i].second) {
			K--;
			ans+=sw;
		}
		else
			sw++;
	}
	if (K>0) {
		cout << "IMPOSSIBLE";
		return;
	}
	cout << ans;
}

int main() {
	int T;
	cin>>T;
	for (int i=1; i<=T; i++) {
		cout<<"Case #"<<i<<": ";
		go();
		cout<<endl;
	}
	return 0;
}