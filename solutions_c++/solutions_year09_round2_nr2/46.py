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
template <class T> inline string itos(T n) {return (n)<0?"-"+itos(-(n)):(n)<10?(string)("")+(char)('0'+(n)):itos((n)/10)+itos((n)%10);}
#define gcj_print(ans) {cout << "Case #" << ((test)+1) << ": " << (ans) << endl;}

string func(string s){
	int n=s.length(),i;
	vector <char> v1,v2;
	
	REP(i,n) v1.push_back(s[i]);
	v2 = v1;
	sort(v2.begin(),v2.end());
	reverse(v2.begin(),v2.end());
	if(v1 != v2){
		next_permutation(v1.begin(),v1.end());
		string ans;
		REP(i,n) ans += v1[i];
		return ans;
	} else {
		int zero = 0;
		REP(i,n) if(v1[i] == '0') zero++;
		v2.clear();
		REP(i,n) if(v1[i] != '0') v2.push_back(v1[i]);
		sort(v2.begin(),v2.end());
		string ans;
		ans += v2[0];
		REP(i,zero+1) ans += '0';
		for(i=1;i<v2.size();i++) ans += v2[i];
		return ans;
	}
}

int main(void){
	int T,test;
	string s;
	
	cin >> T;
	REP(test,T){
		cin >> s;
		string ans = func(s);
		gcj_print(ans);
	}
	
	return 0;
}
