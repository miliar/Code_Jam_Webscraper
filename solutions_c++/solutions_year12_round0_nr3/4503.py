#include <iostream>
#include <cstdio>
#include <cstring>
#include <sstream>
#include <algorithm>

using namespace std;

#define REP(i,n) for(int i=0; i<n; i++)

typedef unsigned long long ull;
typedef long long ll;

bool pre[2500][2500];

void rotate(string &s) {
	char f = s[0];
	s = s.substr(1,s.size()-1) + f;
}

int main() {
    #ifdef RISHI
    freopen("in.cpp","r",stdin); freopen("out","w",stdout);
    #endif
    
    for(int i=10; i<=2500; i++) {
		stringstream ss; ss << i;
		string num; ss >> num;
		for(int j=0; j<(num.size()-1); j++) {
			rotate(num);
			if(num[0] != '0')	{ //cout << i << " " << num << endl;
				pre[i][atoi(num.c_str())] = 1;
			}
		}
	}
   
    int nt; cin >> nt; REP(ca,nt) {
		int cnt=0,x,y; cin >> x >> y;
		for(int i=x; i<=y; i++) for(int j=i+1; j<=y; j++) if(i!=j) cnt += pre[i][j];
		cout << "Case #" << ca+1 << ": " << cnt << endl;
	}

    return 0;
}
