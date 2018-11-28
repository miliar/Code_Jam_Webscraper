
#include <iostream>
#include <set>
#include <cstring>

using namespace std;

int main(){
	
	int L, D, N;

	cin >> L >> D >> N;

	string *x = new string[D];

	for(int i=0; i<D; ++i){
		cin >> x[i];
	}

	set<char> m[16];

	for(int ncase=1; ncase <= N; ++ncase){
		
		string t;
		
		cin >> t;

		int len = strlen(t.c_str());

		int ptr = 0;

		for(int i=0; i<len && ptr<16; ++i){
			if(t[i] == '('){
				for(++i ; i<len; ++i){
					if(t[i] != ')'){
						m[ptr].insert(t[i]);
					}else{
						break;
					}
				}
			}else{
				m[ptr].insert(t[i]);
			}
			++ptr;
		}
		/*	
		for(int i=0; i<ptr; ++i){
			for(set<char>::iterator ite = m[i].begin(); ite != m[i].end(); ++ite){
				cout << *ite;
			}
			cout << endl;
		}
		*/
		int rtn = 0;
		
		if(ptr <= 15){

			for(int i=0; i<D; ++i){
				int len = strlen(x[i].c_str());
				bool found = true;
				for(int j=0; j<len; ++j){
					if(m[j].find(x[i][j]) == m[j].end()){
						found = false;
						break;
					}
				}

				if(found){
					++rtn;
				}
			}
		}

		cout << "Case #" << ncase << ": " << rtn << endl;
		
		for(int i=0; i<16; ++i){
			m[i].clear();
		}
	}
	return 0;
}
