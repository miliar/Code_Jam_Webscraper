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
	vector<int> v;
	cin >> sz;
	int n=0;
	for(int i=0;i<sz;++i){
	    int t;
	    cin >> t;
	    if(t != i+1) ++n;
	}

	cout << "Case #" << TT << ": " << ((n<2)?0:n) << endl;
    }
}
