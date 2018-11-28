#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <functional>

#define all(v) (v).begin(), (v).end()

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;


int gcd (int a, int b) {
    while (b > 0) {
        int m = a % b;
        a = b; b = m;
    }
    return a;
}

int main (void) {
    int T = 0;
    cin >> T;

    for (int c = 1; c<=T; ++c) {
	ll N;
	int Pd, Pg;
	cin >> N >> Pd >> Pg;
	printf("Case #%d: ",c);

//	cout<<"N="<<N<<", Pd="<<Pd<<", Pg="<<Pg<<endl;

	int x = gcd(Pd,100);
	int D = 100/x, Wd = Pd/x;
//	cout<<x<<", D="<<D<<", Wd="<<Wd<<endl;
	
	if (Pg == 0 and Pd > 0) {
	    cout<<"Broken"<<endl;
	    continue;
	}
	if (Wd == 0 and Pg < 100) {
	    cout<<"Possible"<<endl;
	    continue;
	}

	if (D > N) {
	    cout<<"Broken"<<endl;
	    continue;
	}
	//Now exists a,b s.t. a<=b and 
	int g = gcd(Pg,100);
	int G = 100/g, Wg = Pg/g;
//	cout<<g<<", G="<<G<<", Wg="<<Wg<<endl;
	
	if (G == Wg and D != Wd) {
	    cout<<"Broken"<<endl;
	    continue;
	}
/*	
	double c = ceil((double)(D-Wd) / (G-Wg)) + 1;
	G *= c; Wg *= c;
	cout<<c<<", G="<<G<<", Wg="<<Wg<<endl;
*/
	cout<<"Possible"<<endl;
    }

    return 0;
}
