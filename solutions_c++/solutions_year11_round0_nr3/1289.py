#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>

using namespace std;


int main(){
    int T;
    cin >> T;
    for(int TT=1;TT<=T;++TT){
    
	int sz;
	cin >> sz;
	int x=0;
	int m=10000000;
	int s=0;
	for(int i=0;i<sz;++i){
	    int t;
	    cin >> t;
	    x ^= t;
	    s += t;
	    m = min(m,t);
	}

	cout << "Case #" << TT << ": " ;
	if(x == 0) cout << s - m << endl;
	else cout << "NO" << endl;
    }
}
