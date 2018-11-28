#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define gcj_print(ans) {cout << "Case #" << ((test)+1) << ": " << (ans) << endl;}

string words[5010];
bool can[20][30];

int main(void){
	int i,j,x,L,D,N,test;
	
	cin >> L >> D >> N;
	REP(i,D) cin >> words[i];
	
	REP(test,N){
		REP(i,L) REP(j,26) can[i][j] = false;
		
		string s;
		cin >> s;
		i = 0; x = 0;
		while(1){
			if(i == s.length()) break;
			if(s[i] == '('){
				for(j=i+1;s[j]!=')';j++) can[x][s[j]-'a'] = true;
				i = j + 1;
			} else {
				can[x][s[i]-'a'] = true;
				i++;
			}
			x++;
		}
		
		int ans = 0;
		REP(i,D){
			bool match = true;
			REP(j,L) if(!can[j][words[i][j]-'a']) match = false;
			if(match) ans++;
		}
		
		gcj_print(ans);
	}
	
	return 0;
}
