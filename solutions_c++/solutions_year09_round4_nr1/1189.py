#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
typedef long long int lint;
typedef pair<int,int> par;
 
#define sz size
#define pb push_back
#define all(x) (x).begin() , (x).end()
#define sqr(x) (x)*(x)
#define x first
#define y second
#define rep(i,n)  for (int (i)=0;(i)<(int)(n);(i)++)
#define Rep(i,a,n) for (int (i)=(int)(a);(i)<(int)(n);(i)++)

int n;
int vec[50];
vector<int> one;

int bfs() {
	map<vector<int> , int> mapa;
	queue< pair< vector<int>, int> > q;
	q.push(make_pair(one,0));
	
	while (!q.empty()) {
		vector<int> v = q.front().x;
		int p = q.front().y;
		q.pop();
		
		if (mapa.find(v) != mapa.end())
			continue;
		mapa[v] = 1;
		
		int mau = 0;
		for (int k=0;k<n;k++)
			if (v[k] > k)
				mau = 1;
		if (!mau)
			return p;
		//cout << p << endl;
			
			
		for (int k=0;k<n-1;k++) {
			swap(v[k],v[k+1]);
			q.push(make_pair(v,p+1));
			swap(v[k],v[k+1]);
		}
	}
	return 0;
}

int main() {
	int t;
	cin >> t;
	Rep(i,1,t+1) {
		one.clear();
		cin >> n;
		rep(j,n) {
			string r;
			cin >> r;
			int z= (int)r.sz() - 1;
			while ( z >= 0) {
				if (r[z] == '1')
					break;
				z--;
			}
			one.pb(max(z,0));
			vec[j] = max(z,0);
		}
		
		sort(vec, vec + n);
		reverse(vec, vec + n);
		
		/*
		int sum=0;
		
		rep(pos,n) {
			int sai = 0;
			rep(j,n) {
				if (one[j] == vec[pos] && one[j] > j) {
					sai = 1;
					for (int l=j+1;l<n;l++) {
						sum++;
						swap(one[l-1],one[l]);
						if (one[l] < l)
							break;
					}
				}
				if (sai)
					break;
			}
		}
		*/
		
	
		cout << "Case #" << i << ": " << bfs() << endl;
	}
	return 0;
}

