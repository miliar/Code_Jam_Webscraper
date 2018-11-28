#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <cstring>
/*#include <hash_map>
using namespace __gnu_cxx;*/
typedef long long ll;
using namespace std;

#define pb push_back
#define mp make_pair
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vector<pii> > adjL;
int oo = (int) 1e9;

vector<string >vs;
int di[]={1, 0, 1, 1};
int dj[]={0, 1, 1,-1};
bool sameC(int i, int j, int d, char c) {
	for (int k = 0; k < 4; ++k) {
		if(vs[i][j] != c && vs[i][j] != 'T')
			return false;
		i+=di[d];
		j+=dj[d];
	}
	return true;
}
bool isWon(char c) {
	for (int i = 0; i < 4; ++i) {
//		for (int d = 0; d < 2; ++d) {
			if(sameC(0, i, 0, c) ||sameC(i, 0, 1, c))
				return true;
//		}
	}
	if(sameC(0, 0, 2, c) || sameC(0, 3, 3, c))
		return true;
	return false;
}
bool isDone() {
	for (int i = 0; i < 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			if(vs[i][j] == '.')
				return false;
		}
	}
	return true;
}
int main() {
	//	std::ios_base::sync_with_stdio(false);
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.txt", "wt", stdout);

	int t;
	cin>>t;
	for (int ii = 0; ii < t; ++ii) {
		cout<<"Case #"<<ii+1<<": ";
		vs.clear();
		string str;
		for (int i = 0; i < 4; ++i) {
			cin>>str;
			vs.pb(str);
		}
		if(isWon('X'))
			cout<<"X won";
		else if(isWon('O'))
			cout<<"O won";
		else if(isDone())
			cout<<"Draw";
		else cout<<"Game has not completed";
		cout<<endl;
	}
	return 0;
}
