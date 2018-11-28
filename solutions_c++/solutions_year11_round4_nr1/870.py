#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<deque>
#include<string>
#include<cctype>
#include<cmath>
#include<sstream>
#include<numeric>
#include<complex>
#include<queue>
using namespace std;

int X, S, R, TT, N;
map<int, int> table;
bool used[2000000];

int main(){

	//freopen("1.in", "rt", stdin);
	//freopen("1.out", "wt", stdout);
	//freopen("A-small-attempt0.in", "rt", stdin);
	//freopen("A-small-attempt0.out", "wt", stdout);
	//freopen("A-small-attempt1.in", "rt", stdin);
	//freopen("A-small-attempt1.out", "wt", stdout);
	//freopen("A-small-attempt2.in", "rt", stdin);
	//freopen("A-small-attempt2.out", "wt", stdout);
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);

	int tt; cin >> tt;
	for(int t = 0 ; t < tt ; t++){
		//cerr << "Solving testcase " << t+1 << endl;

		memset(used, 0, sizeof used);
		table.clear();
		cin >> X >> S >> R >> TT >> N;
		double T = TT;
		for(int i = 0 ; i < N ;i++){
			int a, b, c;
			cin >> a>> b >> c;
			table[c] += b-a;
			for(int j = a ; j < b ; j++)
				used[j] = true;
		}

		for(int i = 0 ; i < X ; i++){
			if(used[i])continue;
			table[0]++;
		}

		double res = 0;
		for(map<int, int>::iterator itr = table.begin() ; itr != table.end() ; itr++){
			double mt = (*itr).second*1./((*itr).first+R);
			double okT = min(mt, T);
			res += okT;
			T -= okT;
			double okD = okT*((*itr).first+R);

			double remD = (*itr).second-okD;
			double remT = remD/((*itr).first+S);
			res += remT;
		}

		printf("Case #%d: %.9lf\n", t+1, res);
	}

	return 0;
}
