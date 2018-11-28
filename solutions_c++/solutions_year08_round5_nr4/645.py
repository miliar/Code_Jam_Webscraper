#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <deque>
#include <set>
#include <list>

#include <algorithm>
#include <iterator>
#include <numeric>
#include <utility>	// make_pair(a,b)
#include <limits>

#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>


using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef vector<string> vs;
typedef complex<double> point;
typedef pair<int,int> pii;

#define foreach(i,c)  for( typeof((c).begin()) i = (c).begin(); i!=(c).end(); i++)
#define all(c) (c).begin(), (c).end()
#define sz(c) ((int)(c).size())
#define pb push_back
#define contains(c,x) ((c).find(x) != (c).end()) 

template<class T> void getvec(vector<T> &v) {
    v.clear();
    string s;
    getline(cin,s);
    istringstream ss(s);
    copy(istream_iterator<T>(ss), istream_iterator<T>(), back_inserter(v));
}


const int BIGINT = numeric_limits<int>::max();
const int MOD = 10007;

class A {
public:
    vector<pii> bad;
    pii coord(int r, int c) {
	int n = (r+c)/3;
	int d = (c-r+n)/2;
	return make_pair(n,d);
    }
    void add_rocks(int r, int w) {
	if ((r+w)%3==0) {
	    pii co = coord(r,w);
	    bad.push_back(co);	    
// 	    cout<<"+ "<<co.first<<' '<<co.second<<endl;
	}
    }
    int H,W;
    int solve() {
	int R,r,w;

	cin>>H>>W>>R;
	H--; W--;
	for (int i=0; i<R; i++) {
	    cin>>r>>w;
	    r--; w--;
	    add_rocks(r,w);
	}

	if ((H+W)%3!=0)  return 0;
	pii co = coord(H,W);
// 	cout<<": "<<co.first<<' '<<co.second<<endl;
	if (co.second <0  or co.second>co.first)  return 0;
	vi v(co.first+1);
	    
	v[0] = 1;
// 	int min = 0;
// 	int max = 0;
	for (int i=0; i<co.first; i++) {
	    for (int j=0; j<bad.size(); j++) {
		if (bad[j].first == i)
		    if (0<=bad[j].second && bad[j].second<=i)
			v[bad[j].second] = 0;
	    }

	    vi vold(co.first+1);
	    swap(v,vold);
	    for (int j=0; j<=i; j++) {
		v[j] += vold[j];
		v[j+1] += vold[j];
	    }
	    for (int j=0; j<=i+1; j++) {
		v[j] = v[j]%MOD;
	    }
// 	    cout<<endl<<"# ";
// 	    copy(all(v),ostream_iterator<int>(cout," "));
	}
	return v[co.second];
    }
    
};



int main() {
    int NN;
    cin>>NN;  cin.ignore(99, '\n');
    for (int nn=1; nn<=NN; nn++) {
	A a;
	cout<<"Case #"<<nn<<": "<<a.solve()<<endl;
    }
    return 0;
}
