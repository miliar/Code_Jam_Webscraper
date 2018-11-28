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

int comb[26][26];
bool opp[26][26];

int main(){
	
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	
	int T;
	int c, d, n;
	string s;
	cin >> T;
	for(int t = 0; t < T; t++){
		memset(comb, -1, sizeof(comb));
		memset(opp, false, sizeof(opp));
		cin >> c;
		for(int i = 0; i < c; i++){
			cin >> s;
			comb[s[0] - 'A'][s[1] - 'A'] = s[2] - 'A';
			comb[s[1] - 'A'][s[0] - 'A'] = s[2] - 'A';
		}
		cin >> d;
		for(int i = 0; i < d; i++){
			cin >> s;
			opp[s[0] - 'A'][s[1] - 'A'] = true;
			opp[s[1] - 'A'][s[0] - 'A'] = true;
		}
		cin >> n;
		cin >> s;
		string res;
		res.push_back(s[0]);
		for(int i = 1; i < n; i++){
			int num1 = s[i] - 'A';
			if(res.empty()) res.push_back(s[i]);
			else{
				int num2 = res[res.size()-1] - 'A';
				if(comb[num1][num2] >= 0){
					res.pop_back();
					res.push_back((char)('A' + comb[num1][num2]));
				
				}else{
					bool del = false;
					for(int j = 0; j < (int)res.size(); j++){
						num2 = res[j] - 'A';
						if(opp[num1][num2]) del = true;
					}
					if(del){
						res.clear();
					}else{
						res.push_back(s[i]);
					}
				}
			}
		}
		
		cout << "Case #" << t + 1 << ": [";
		for(int i = 0; i < (int)res.size() - 1; i++){
			cout << res[i] << ", " ;
		}
		if(!res.empty()) cout << res[res.size() - 1] ;
		cout << "]" << endl;
	}
	
	cin.close();
	cout.close();
	
	return 0;
}