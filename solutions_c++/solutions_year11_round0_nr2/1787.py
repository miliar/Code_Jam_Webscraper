#include <iostream>
#include <istream>
#include <string>
using namespace std;

const int MAX_C = 37;
const int MAX_O = 29;

int caseno;
int caseNum, combineNum, opposeNum, invokeNum;
string combine[MAX_C], oppose[MAX_O], invoke;

bool check(string s1, string s2){
	if(s1==s2) return true;

	string ss;
	ss += s2[1];
	ss += s2[0];

	if(s1==ss) return true;
	return false;
}


void solve(){
	/*
	cout << "case" << caseno << endl;
	
	for(int i=0 ; i<combineNum ; i++){
		cout << combine[i] << endl;
	}
	cout << endl;

	for(int i=0 ; i<opposeNum ; i++){
		cout << oppose[i] << endl;
	}
	cout << endl;

	cout << invoke << endl;
	*/

	string s;
	int p=0;

	for(int p=0 ; p<invokeNum ; p++){
		s += invoke[p];

		if(s.size()==1) continue;

		// combine
		string cs = s.substr(s.size()-2, 2);

		for(int i=0 ; i<combineNum ; i++){
			if( check( cs, combine[i].substr(0,2) ) ){
				s.pop_back();
				s.pop_back();
				s += combine[i][2];
				break;
			}
		}

		// oppose
		string os;
		os += s.back();
		bool opposed = false;
		for(int i=0 ; i<s.size()-1 ; i++){
			os += s[i];


			for(int j=0 ; j<opposeNum ; j++){
				if( check( os, oppose[j] ) ){
					//s.erase(i);
					s.clear();
					opposed = true;
					break;
				}
			}
			if(opposed) break;
			
			os.pop_back();
		}

	}
	
	cout << "Case #" << caseno << ": ["; 

	if(s.empty()){
		cout << "]" << endl;
		return;
	}

	for(int i=0 ; i<s.size()-1 ; i++){
		cout << s[i] << ", ";
	}

	cout << s.back() << "]" << endl;

}



int main(){

	cin >> caseNum;

	for(caseno=1 ; caseno<=caseNum ; caseno++){

		cin >> combineNum;

		for(int i=0 ; i<combineNum ; i++){
			cin >> combine[i];
		}

		cin >> opposeNum;

		for(int i=0 ; i<opposeNum ; i++){
			cin >> oppose[i];
		}

		cin >> invokeNum;

		cin >> invoke;

		solve();

	}

}