#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

#define fs first
#define sc second
#define mp make_pair
#define pb push_back

typedef unsigned long long ULL;
typedef long long LL;
typedef vector < int > VI;

int abs(int v){return v > 0 ? v : -v;}

int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int num = 0, n, s, p, t, kol;
	cin >> num;
	for(int i = 0; i < num; ++i){
		cin >> n >> s >> p;
		kol = 0;
		for(int j = 0; j < n; ++j){
			cin >> t;
			int mx = t % 3 ? t / 3 + 1 : t / 3;
			if(mx >= p){
				++kol;
				continue;
			}
			t -= p;
			if(s && abs(t / 2 - p) == 2){
				--s;
				++kol;
				continue;
			}
		}
		cout << "Case #"  << i+1 << ": " << kol << endl;;
	}
	return 0;
}
