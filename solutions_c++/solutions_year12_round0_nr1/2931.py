#include <iostream>
#include <cstdio>
#include <fstream>
using namespace std;

#define FORi(m) for(int i = 0; i < (m); ++i)
#define FOR(i, M) for( int i = 0; i < (M); ++i )

char DIC[27] = "yhesocvxduiglbkrztnwjpfmaq";
#define dic(c) DIC[c-'a']


void train(){
	dic('z') = 'q';
	dic('q') = 'z';
	DIC[26] = '\0';
	
	ifstream ifs("tin.txt");
	ifstream rfs("tout.txt");
	
	char i, o;
	while(ifs >> i){
		rfs >> o;
		dic(i) = o;
	}
	
	ofstream d("dic.txt");
	d << DIC;
}

void solve(){
	int T;
	cin >> T;
	cin.ignore(999,'\n');
	FOR(t, T){
		printf("Case #%d: ", t+1);
		char c;
		while(cin.good()){
			c = cin.get();
			if (c == '\n' || !cin.good()) break;
			if (c == ' ') cout << c;
			else cout << dic(c);
		}
		cout << endl;
	}
}


int main(){
	//train();
	solve();
}
