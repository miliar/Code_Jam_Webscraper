#include <iostream>
#include <cstdio>
#include <string>
#include <set>
using namespace std;

#define FOR(i, M) for( int i = 0; i < (M); ++i )
#define FOR_(i, m, c, M) for( int i = (m); i c (M); ++i )

int main(){
	int T, M, N;
	cin >> T;
	string s;
	FOR_(Ti, 1, <=, T){
		set<string> dir;
		cin >> N >> M; cin.get();
		FOR(i, N){
			cin.get();
			getline(cin, s);
			int x = 0;
			
			while((x = s.find_first_of ( '/', x)) != string::npos){
				dir.insert(s.substr(0, x++));
			}
			
			dir.insert(s);
			
		}
		int mk = 0;
		FOR(i, M){
			cin.get();
			getline(cin, s);
			if (dir.find(s) == dir.end()){
				int x = 0;
				string sa;
				while((x = s.find_first_of ( '/', x)) != string::npos){
					sa = s.substr(0, x++);
					if (dir.find(sa) == dir.end()){
						dir.insert(sa);
						++mk;
					}
				}
				dir.insert(s);
				++mk;
			}
		}
		/*
		for( set<string>::iterator ii = dir.begin(); ii != dir.end(); ++ii ){
			cout << *ii << endl;
		}*/
		printf("Case #%d: %d\n", Ti, mk);
	}
}
