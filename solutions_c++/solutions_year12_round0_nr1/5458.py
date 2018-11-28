#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

#define REP(i,n) for(int i=0; i<n; i++)

typedef unsigned long long ull;
typedef long long ll;

int main() {
    #ifdef RISHI
    freopen("in.cpp","r",stdin); freopen("out","w",stdout);
    #endif
    
    string map = "yhesocvxduiglbkrztnwjpfmaq", inp;
    int nt; cin >> nt; REP(ca,nt) {
		scanf("\n"); getline(cin, inp);
		cout << "Case #" << ca+1 << ": "; 
		REP(i,inp.size()) 
			if(inp[i] == ' ') cout << ' ';
			else cout << map[inp[i]-'a'] ; cout << endl;
	}

    return 0;
}
