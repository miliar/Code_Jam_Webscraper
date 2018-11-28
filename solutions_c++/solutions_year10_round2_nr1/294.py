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

int main(){

	//freopen("1.in", "rt", stdin);
	//freopen("1.out", "wt", stdout);
//	freopen("A-small-attempt0.in", "rt", stdin);
//	freopen("A-small-attempt0.out", "wt", stdout);
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);

	int tt; cin >> tt;
	for(int t = 0 ; t < tt ; t++){

		int N, M;
		cin >> N >> M;
		set<string> s;
		for(int i = 0 ; i < N ; i++){
			string str; cin >> str;
			s.insert(str);
		}
		int res = 0;
		set<string> created;
		for(int i = 0 ; i < M ; i++){
			string str; cin >> str;
			if(str[str.size()-1] != '/')str += "/";
			string x = "/";
			for(int j = 1 ; j < str.size() ; j++){
				if(str[j] == '/'){
					if(created.find(x) == created.end()){
						created.insert(x);
						res += (s.find(x) == s.end());
					}
				}
				x += str[j];
			}
		}

		cout << "Case #" << t+1 << ": " << res << endl;
	}

	return 0;
}
