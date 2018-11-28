// Author: Swarnaprakash
// Problem: Bot Trust
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
		int n;
		cin>>n;
		int opos,bpos;
		opos=bpos=1;
		int otime,btime;
		otime=btime=0;
		int prev_time = 0;
		while(n--) {
			string color;
			int button;
			cin>>color>>button;
			if(color == "O") {
				prev_time = max(prev_time + 1, abs(opos - button) + otime + 1);
				opos = button;
				otime = prev_time;
			} else {
				prev_time = max(prev_time + 1, abs(bpos - button) + btime + 1);
				bpos = button;
				btime = prev_time;
			}
		}
		cout<<"Case #"<<t<<": ";
		cout<<prev_time<<endl;
	}
	return 0;
}

