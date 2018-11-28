// Author: Swarnaprakash
// Problem: Magicka
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cassert>

using namespace std;

const int M = 105;
const int INF = 0x3f3f3f3f;
const bool debug=true;

#define SET(x,v)	memset(x,v,sizeof(x))
#define ALL(x) 		(x).begin() , (x).end()
#define SZ(x)		((int)((x).size()))
#define DB(x) 		if(debug) cout << #x << " : " << x <<endl;

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef pair<int,PII> PIII;

int main() {
	int tc;
	cin>>tc;
	for(int t=1;t<=tc;++t) {
		char combine[200][200];
		char opposite[200];
		SET(combine,'0');
		SET(opposite,'0');
		int c;
		cin>>c;
		while(c--) {
			string comb;
			cin>>comb;
			combine[comb[0]][comb[1]]=comb[2];
			combine[comb[1]][comb[0]]=comb[2];
		}
		int d;
		cin>>d;
		while(d--) {
			string opp;
			cin>>opp;
			opposite[opp[0]]=opp[1];
			opposite[opp[1]]=opp[0];
		}
		int n;
		string base;
		cin>>n>>base;
		string result;
		for(int i=0;i<SZ(base);++i) {
			if(SZ(result) == 0) {
				result.push_back(base[i]);
			} else if(combine[result[SZ(result) - 1]][base[i]] != '0') {
				result[SZ(result) - 1] = combine[result[SZ(result) - 1]][base[i]]; 
			} else if(opposite[base[i]] != '0' && result.find(opposite[base[i]]) != -1) {
				result = "";
			} else {
				result.push_back(base[i]);
			}
			
		}
		cout<<"Case #"<<t<<": ";
		cout<<"[";
		for(int i=0;i<SZ(result);++i) {
			if(i) cout<<", ";
			cout<<result[i];
		}
		cout<<"]"<<endl;
	}
	return 0;
}

