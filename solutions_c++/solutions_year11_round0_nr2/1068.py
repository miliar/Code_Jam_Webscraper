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

bool opp[26][26];
int comb[26][26];
bool exist[26];

void print(vector<int> vec){cout << "Printing the vector" << endl;for(int i = 0 ; i < vec.size() ; i++)cout << (char)('A'+vec[i]) << " " ;cout << endl;}

int main(){

	//freopen("1.in", "rt", stdin);
	//freopen("1.out", "wt", stdout);
	//freopen("B-small-attempt0.in", "rt", stdin);
	//freopen("B-small-attempt0.out", "wt", stdout);
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);

	int tt; cin >> tt;
	for(int t = 0 ; t < tt ; t++){
		cerr << "Solving testcase " << t+1 << endl;

		memset(opp, 0, sizeof opp);
		memset(comb, -1, sizeof comb);
		memset(exist, 0, sizeof exist);

		int C; cin >> C;
		for(int i = 0 ; i < C ; i++){
			string str; cin >> str;
			comb[str[0]-'A'][str[1]-'A'] = str[2]-'A';
			comb[str[1]-'A'][str[0]-'A'] = str[2]-'A';
		}
		int D; cin >> D;
		for(int i = 0 ; i < D ; i++){
			string str; cin >> str;
			opp[str[0]-'A'][str[1]-'A'] = true;
			opp[str[1]-'A'][str[0]-'A'] = true;
		}

		int N; cin >> N;
		string str; cin >> str;
		vector<int> v;
		for(int i = 0 ; i < N ; i++){
			v.push_back(str[i]-'A');
			//print(v);
			bool combined = false;
			while(v.size() >= 2 && comb[v[v.size()-1]][v[v.size()-2]] != -1){
				combined = true;
				int r = comb[v[v.size()-1]][v[v.size()-2]];
				v.pop_back();v.pop_back();
				v.push_back(r);
			}

			if(!combined){
				for(int j = 0 ; j < 26 ; j++)
					if(exist[j] && opp[j][v.back()]){
						v.clear();
						break;
					}
			}

			memset(exist, 0, sizeof exist);
			for(int j = 0 ; j < v.size() ; j++)
				exist[v[j]] = true;
		}

		cout << "Case #" << t+1 << ": [";
		for(int i = 0 ; i < v.size() ; i++){
			if(i)cout << ", ";
			cout << (char)('A'+v[i]);
		}
		cout << "]" << endl;

	}

	return 0;
}
