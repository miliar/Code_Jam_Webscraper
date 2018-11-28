#include<algorithm>
#include<vector>
#include<list>
#include<deque>
#include<queue>
#include<iostream>
#include<cctype>
#include<cmath>
#include<iterator>
#include<cstdlib>
#include<sstream>
#include<cstdio>
#include<cassert>
#include<climits>
#include<string>
#include<map>
#include<set>
#include<stack>
#include<numeric>
#include<complex>
#include<valarray>

#define FOR(i,a,b) for(int i=a; i<b; i++)
#define F(i,n) for(int i=0; i<n; i++)
#define VI vector<int>
#define pb(a) push_back(a)
#define pf(a) push_front(a)
#define LL long long


using namespace std;

int main() {
	int N; cin>>N;
	int caseN=0;
	while(N--) {
		caseN++;
		int C,D;
		map<string,char> combine;
		set<string> combineSet;
		set<string> oppose;
		string temp = "";
		char ch1,ch2,ch3;
		cin >> C;
		F(i,C) {	
			cin >> ch1 >> ch2 >> ch3;
			temp += ch1;
			temp += ch2;
			sort(temp.begin(),temp.end());
			combine[temp] = ch3;
			combineSet.insert(temp);
			temp="";
		}
		cin >> D;
		F(i,D) {
			cin >> ch1 >> ch2;
			temp += ch1;
			temp += ch2;
			sort(temp.begin(),temp.end());
			oppose.insert(temp);
			temp="";
		}
		
		int sz;
		string s;
		cin >> sz >> s;
		string ret="";
		F(i,sz) {
			bool operationPerformed = false;
			if(ret.size()>0) {
				string tmp = "";
				tmp += s[i];
				tmp += ret[ret.size()-1];
				sort(tmp.begin(),tmp.end());
				if(combineSet.find(tmp) != combineSet.end()) {
					char ch = combine[tmp];
					ret = ret.substr(0,ret.size()-1);
					ret += ch;
					/*cout << " About to perform combine on ret =  " << ret << endl; 
					cout << " Performed combine for " << tmp << endl;
					cout << " New ret = " << ret << endl;*/
					operationPerformed = true;
				}
				else {
					F(j,ret.size()) {
						string tmp="";
						tmp += ret[j];
						tmp += s[i];
						sort(tmp.begin(),tmp.end());
						if(oppose.find(tmp) != oppose.end()) {
							ret="";
							operationPerformed = true;
//							cout << "destroyed ret " << endl;
						}
					}
				}
				if(!operationPerformed) {
					ret += s[i];
	//				cout << "Appended to ret from inside " << s[i] << endl;
	//				cout << " ret = " << ret << endl;
				}
			}
			else {
				ret += s[i];
		//		cout << "Appended to ret from outside " << s[i] << endl;
		//		cout << " ret = " << ret << endl;
			}
		}
		string finalRet = "[";
		FOR(i,0,ret.size()) {
			finalRet += ret[i] ;
			finalRet += ", ";
		}
		finalRet = finalRet.substr(0,finalRet.size()-2);
		finalRet += ']';
		cout << "Case #" << caseN << ": " <<  finalRet << endl ;
	}	
	return 0;
}
