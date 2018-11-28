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

ll mass[510][510];
ll sumx[510][510];
ll sumy[510][510];
ll sumw[510][510];

bool ok(int i, int j, int k){
	double py = i + (double)k / 2;
	double px = j + (double)k / 2;
	ll m = sumw[i+k][j+k] - sumw[i+k][j-1] - sumw[i-1][j+k] + sumw[i-1][j-1];
	m -= (mass[i+k][j+k] + mass[i][j] + mass[i][j+k] + mass[i+k][j]);
	ll sy = sumy[i+k][j+k] - sumy[i+k][j-1] - sumy[i-1][j+k] + sumy[i-1][j-1];
	sy -= (mass[i+k][j+k] * (i+k) + mass[i][j+k] * i + mass[i+k][j] * (i+k) + mass[i][j] * i);
	ll sx = sumx[i+k][j+k] - sumx[i+k][j-1] - sumx[i-1][j+k] + sumx[i-1][j-1];
	sx -= (mass[i+k][j+k] * (j+k) + mass[i][j+k] * (j+k) + mass[i+k][j] * j + mass[i][j] * j);
	double x = (double)sx / m;
	double y = (double)sy / m;
	
	if(x < px + EPS && x > px - EPS && y < py + EPS && y > py - EPS){
		return true;
	}
	else return false;
}

int main(){
	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int T;
	cin >> T;
	for(int t = 0; t < T; t++){
		int R, C, D;
		cin >> R >> C >> D;
		for(int i = 1; i <= R; i++){
			for(int j = 1; j <= C; j++){
				char ch;
				cin >> ch;
				mass[i][j] = D + ch - '0';
			}
		}
		memset(sumx, 0, sizeof(sumx));
		memset(sumy, 0, sizeof(sumy));

		for(int i = 1; i <= R; i++){
			for(int j = 1; j <= C; j++){
				sumw[i][j] = sumw[i-1][j] + sumw[i][j-1] - sumw[i-1][j-1] + mass[i][j];
				sumx[i][j] = sumx[i-1][j] + sumx[i][j-1] - sumx[i-1][j-1] + mass[i][j] * (ll)j;
				sumy[i][j] = sumy[i-1][j] + sumy[i][j-1] - sumy[i-1][j-1] + mass[i][j] * (ll)i;
				
			}
		
		}
		int res = 0;
		for(int i = 1; i <= R - 2; i++){
			for(int j = 1; j <= C - 2; j++){
				int d = min(R - i, C - j); 
				for(int k = 2; k <= d; k++){
					if(ok(i, j, k)) res = max(res, k + 1);
				}
			}
		}
		cout << "Case #" << t + 1 << ": ";
		if(res >= 3) cout << res << endl;
		else cout << "IMPOSSIBLE" << endl;
	}
	
	cin.close();
	cout.close();
	return 0;
}

/* B
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

/* A
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