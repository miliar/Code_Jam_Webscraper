

#include "template.h"
#include <cstdio>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <utility>
#include <vector>
#include <sstream>
#include <map>
#include <set>

using namespace std;

#define FOR(i,a,b) for(int i = a; i <b ; i++)
#define FRR(i,a,b) for(int i = b - 1; i >=a ; i--)
#define sz size()
#define pb push_back
#define VI vector<int>
#define VVI vector<VI>
#define eps 1e-9


int main(){
	int cases;
	cin >> cases;
	FOR(caseNum, 0, cases){
		string s;
		cin >> s;
		if(s.sz == 1){
			s = s + "0";
		}
		else {
			bool flag = next_permutation(s.begin(), s.end());
			if(!flag){
				int nz = 0;
				if(s[nz] == '0'){
					while(s[nz] == '0' && nz < s.sz)nz++;
					s[0] = s[nz];
					s[nz] = '0';
				}
				s = s.substr(0,1) + "0" + s.substr(1);
			}
		}
		cout << "Case #" <<  caseNum + 1 << ": " << s << endl;
	}
}