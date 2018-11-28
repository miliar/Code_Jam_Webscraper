#include <algorithm>
#include <iostream>
#include <map>
#include <cstring>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include <fstream>
using namespace std;

#define rep(i,n) for(int i = 0;i<n;i++)
#define FOR(i,s,e) for (int i = int(s); i != int(e); i++)
#define FORIT(i,c) for (typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define ISEQ(c) (c).begin(), (c).end()

using std::cerr;
using std::cout;
using std::endl;
using std::string;
using std::vector;
char mapping[30];

void domapping(){
	string crypted,ans;
		set<char> cset;

		bool mappedall = true;
		rep(i,30){
			mapping[i] = -1;
		}
		cout << (char)-1;
		while(true){
			mappedall = true;
			cout << "input crypted data" << endl;
			cin >> crypted;
			cout << "input answer data" << endl;
			cin >> ans;
			for(int i = 0;i<crypted.length();i++){
				char c = crypted[i];
				char a = ans[i];
				mapping[c-'a'] = a;
				cset.insert(a);
			}
			cout << "the mapping is" << endl;
			for(int i = 'a';i<='z';i++){
				cout << "[" << (char)i << "]is[" << mapping[i-'a'] << "],";
			}
			cout << endl;
			for(int i = 'a';i<='z';i++){
				if(mapping[i-'a'] == -1){
					mappedall = false;
					cout << "still char " << (char)i << " is not mapped" << endl;
				}
			}
			if(mappedall){
				break;
			}else{
				cout << "unallocated chars are" << endl;
				for(int i = 'a';i<='z';i++){
					if(!cset.count((char)i)){
						cout << "char " << (char)i << " is unallocated" << endl;
					}
				}
			}
		}
		cout << "filled all mappings" << endl;
		for(int i = 'a';i<='z';i++){
			cout << (char)i << "," << mapping[i-'a'] << endl;
		}
}

void inputmappings(){
	cout << "input mapping" << endl;
	for(int i = 'a';i<='z';i++){
		string s;
		cin >> s;//*,* form * -> *
		mapping[s[0] - 'a'] = s[2];
	}
	cout << "end input mapping" << endl;
}

void solve(){
	ofstream fout;
	fout.open("out.txt");
	cout << "started solving" << endl;
	int n;
	cin >> n;
	string s;
	getline(cin,s);
	rep(i,n){
		getline(cin,s);
		rep(j,s.length()){
			s[j] = mapping[s[j] - 'a'];
		}
		cout << "Case #" << i+1 << ": ";
		fout << "Case #" << i+1 << ": ";
		cout << s << endl;
		fout << s << endl;
	}
	fout.close();
}

int main() {
	//domapping();
	inputmappings();
	solve();
    return 0;
}

