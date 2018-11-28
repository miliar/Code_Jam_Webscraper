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
#include<cstdio>


using namespace std;

#define FOR(i,a,b) for(int i=a; i<b ; i++)

string intToString(int n) {
	strstream ss;
	ss << n;
	string s;
	ss >> s;
	return s;
}
/*
bool noZero(string s) {
	FOR(i,0,s.size())
		if(s[i]=='0')
			return true;
	return false;
}
*/
int main() {
	int N,caseN=0;
	for(cin >> N ; caseN<N; caseN++) {
		string n;
		cin >> n;
		string s=n;
		//string s=intToString(n);
		if(next_permutation(s.begin(),s.end())) {
			cout << "Case #" << caseN+1 <<": " << s << endl;
			
		}
		else {
			
			//inset a zero after sorting
			sort(s.begin(),s.end()) ;
			int ctr=0;
			string ret="";
			FOR(i,0,s.size())  {
				if(s[i]=='0')  {
					ctr++; 
					}
				else 
					ret+=s[i]; 
			}
			cout << "Case #" << caseN+1 <<": " <<ret[0];
			FOR(i,0,ctr+1)
				cout << "0";
			cout << ret.substr(1,ret.size()-1) << endl;
	
		}
		
		
	}

	return 0;
}	