#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;
#define PII pair<int, int>
#define EPS 1e-9
int main(){
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int tc;
	fin >> tc;
	for(int i = 0; i < tc; i++){
		int x, s, r, t, n;
		fin >> x >> s >> r >> t >> n;
		int b[10000], e[10000], sz = n;
		PII w[10000];
		for(int i = 0; i < n; i++){
			fin >> b[i] >> e[i] >> w[i].first;
			w[i].second = i;
		}
		if(b[0] > 0){
			b[sz] = 0;
			e[sz] = b[0];
			w[sz].second = sz;
			w[sz++].first = 0;
		}
		for(int i = 0; i < n - 1; i++){
			if(b[i + 1] - e[i]){
				b[sz] = e[i];
				e[sz] = b[i + 1];
				w[sz].second = sz;
				w[sz++].first = 0;
			}
		}
		if(e[n - 1] < x){
			b[sz] = e[n - 1];
			e[sz] = x;
			w[sz].second = sz;
			w[sz++].first = 0;
		}
		sort(w, w + sz);
		double ans = 0, t1 = 0;
		int id = 0;
		while(id < sz){
			int k = w[id].second;
			double t2 = (double)(e[k] - b[k]) / (double)(r + w[id].first);
			if(t1 + t2 - t > EPS){
				t2 = t - t1;
				double l = e[k] - b[k] - (r + w[id].first) * t2;
				ans += t2;
				t2 = l / (double)(s + w[id].first);
				ans += t2;
				id++;
				break;
			}
			else{
				ans += t2;
				t1 += t2;
				id++;
			}
		}
		while(id < sz){
			int k = w[id].second;
			double t2 = (double)(e[k] - b[k]) / (double)(s + w[id].first);
			ans += t2;
			id++;
		}
		fout.precision(8);
		fout.flags(ios::fixed);
		fout << "Case #" << i + 1 << ": ";
		fout << ans << endl;
	}
	return 0;
}

				