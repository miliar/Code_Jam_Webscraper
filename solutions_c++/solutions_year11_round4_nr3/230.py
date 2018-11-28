#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <string>
#include <queue>
#include <cmath>
#include <numeric>
#include <list>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <climits>
#include <set>
#include <memory.h>
#include <memory>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>
#include <map>
#include <cassert>
#include <time.h>
#define _USE_MATH_DEFINES
using namespace std;

typedef long long ll;
typedef pair<int, int> P;
typedef pair<int, P> PP;
typedef pair<string, int > Ps;
typedef vector<int> vec;
typedef vector<vec> mat;
const int INF = 1 << 30;
const double EPS = 1e-9;

bool prime[1000010];

int main(){
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	memset(prime, true, sizeof(prime));
	prime[0] = prime[1] = false;
	for(int i = 2; i * i <= 1000000; i++){
		if(prime[i]){
			for(int j = 2; j * i <= 1000000; j++){
				prime[i*j] = false;
			}
		}
	}

	int T;
	cin >> T;
	for(int t = 0; t < T; t++){
		ll n;
		cin >> n;
		int res = 0;
		if(n != 1){
			res++;
			for(ll i = 2; i * i <= n; i++){
				if(!prime[i]) continue;
				int c = 0;
				ll num = i;
				while(num * i <= n){
					c++;
					num *= i;
				}
				res += c;
			}
		}
		cout << "Case #"  << t + 1 << ": " << res << endl;
	}
	
	cin.close();
	cout.close();
	return 0;
}

/*// A
vector<PP> walk;

int main(){
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	

	int T;
	cin >> T;
	for(int t = 0; t < T; t++){
		walk.clear();
		int s, r, x, n;
		double tim;
		cin >> x >> s >> r >> tim;
		cin >> n;
		for(int i = 0; i < n; i++){
			int b, e, w;
			cin >> b >> e >> w;
			walk.push_back(PP(b, P(e, w)));
		}

		sort(walk.begin(), walk.end());
		priority_queue<P, vector<P>, greater<P> > que;
		int pos = 0;
		for(int i = 0; i < (int)walk.size(); i++){
			if(walk[i].first > pos) {
				que.push(P(s, walk[i].first - pos));
			}
			que.push(P(s + walk[i].second.second, walk[i].second.first - walk[i].first));
			pos = walk[i].second.first;
		}
		if(pos < x) que.push(P(s, x - pos));

		double res = 0.0;
		while(!que.empty()){
			P p = que.top();
			que.pop();
			double l = p.second;
			int sp = p.first;
			
			double need = l / (sp - s + r);
			if(need < tim + EPS){
				tim -= need;
				res += need;
			}else{
				res += tim + (l - (double)tim * (sp - s + r)) / sp;
				tim = 0;
			}
		}

		cout << "Case #" << fixed << setprecision(9) << t + 1 << ": " << res << endl;
	}
		
	
	cin.close();
	cout.close();
	
	return 0;
}



*/









// A
/*
char table[200][200];

P wp[200];

double owp[200];

double oowp[200];

int main(){
	
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	
	int n, T;
	cin >> T;
	for(int t = 0; t < T; t++){
		cin >> n;

		for(int i = 0; i < n; i++){
			int w = 0;
			int l = 0;
			for(int j = 0; j < n; j++){
				cin >> table[i][j];
				if(table[i][j] == '1'){
					w++;
				}else if(table[i][j] == '0')
					l++;
			}
			wp[i] = P(w, w + l);
		}
		for(int i = 0; i < n; i++){
			double sum = 0;
			int c = 0;
			for(int j = 0; j < n; j++){
				if(table[i][j] == '1' || table[i][j] == '0'){
					c++;
					if(table[i][j] == '1'){
						sum += (double)(wp[j].first) / (wp[j].second - 1);
					}else{
						sum += (double)(wp[j].first - 1) / (wp[j].second - 1);
					}
				}
			}
			owp[i] = sum / c;
		}
		for(int i = 0; i < n; i++){
			double sum = 0;
			int c = 0;
			for(int j = 0; j < n; j++){
				if(table[i][j] == '1' || table[i][j] == '0'){
					sum += owp[j];
					c++;
				}
			}
			oowp[i] = sum / c;
		}
		cout << "Case #" << t + 1 << ":" << endl;
		for(int i = 0; i < n; i++){

			cout << fixed << setprecision(9) <<  0.25 * (double)wp[i].first / wp[i].second + 0.50 * owp[i] + 0.25 * oowp[i] << endl;
		}
	}

	
	cin.close();
	cout.close();
	
	return 0;
}

*/