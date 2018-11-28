#include<iostream>
#include<string>
#include<vector>
#include<queue>
#include<list>
#include<iterator>
#include<map>
#include<algorithm>
#include<cctype>
#include<cmath>
#include<numeric>
#include<strstream>


using namespace std;

#define FOR(i,a,b) for(long int i=a; i<b ; i++)
#define pb(a) push_back(a)
#define pf(a) push_front(a)
#define VI vector<int>

int stringToInt(string s) {
	strstream ss;
	ss << s;
	long long int n;
	ss >> n;
	return n;
}

int totDiff(string s) {
	map<char,int> m;
	int ret=0;
	FOR(i,0,s.size()) {
		if(!m[s[i]]) {
			ret++;
			m[s[i]]++;
		}
	}
	return ret;
}
long long int toBase(string s,int base) {
	long long int ret=0;
	reverse(s.begin(),s.end());
	int ctr=0;
	FOR(i,0,s.size()) {
		ret += pow(base,ctr)*(int)(s[i]-'0');
		ctr++;
	}
	return ret;

}
int main() {
	int N,caseN=0;
	for(cin >> N ; caseN<N; caseN++) {
		string s;
		cin >> s;
		map<char,int> m;
		string ret="";
		int ctr=0;
		int base = totDiff(s);
		m[s[0]]=1;
		ret += "1";
		char chZero='*';
		FOR(i,1,s.size()) {
			if(m[s[i]] != 0) {
				ret+= (char)(m[s[i]]+'0');
			}
			else if(chZero == s[i]) {
				ret+= "0";
			}
			else {
				if(ctr==1) ctr++;
				if(ctr==0) chZero=s[i];
				ret+=(char)((ctr++)+'0');
				m[s[i]] = ctr-1;
			}
		}
		//convert to base base
		
		if(base==1) base++;
		
		cout << "Case #" << caseN+1 << ": " << toBase(ret,base) << endl;
	}

	return 0;
}	