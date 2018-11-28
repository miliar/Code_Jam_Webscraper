#include <math.h>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;

#define FOR(i,s,n) for (int i=(s);i<(n);i++)
#define ISS istringstream
#define OSS   ostringstream
typedef vector<int> VI;
typedef pair<int,int> PI;

int dx4[] = {-1, 1, 0 , 0};
int dy4[] = {0, 0, -1 ,1 };

int dx8[] = {-1, -1, -1,  0,  0,  1,  1,  1,};
int dy8[] = {-1,  0,  1, -1,  1, -1,  0,  1 };

template<class X,class Y> ostream &operator<<(ostream &s, pair<X,Y> p){s<<p.first<<'@'<<p.second;return s;}
template<class T> ostream &operator<< (ostream& o, vector<T> v) { o << "("; for (int i=0;i<(int)v.size();i++) o << (i?",":"") << v[i]; o << ")"; return o; }
#define vector_include(Item, Vector) (find(Vector.begin(), Vector.end(),Item ) != Vector.end())

int solve(int p, int k, int l, vector< pair<int,int> > &freq) {
    int res=0;
    sort(freq.begin(), freq.end());
    reverse(freq.begin(), freq.end());
    if(l > p*k) {
        return -1;
    }
    vector<int> keys(k,0);

    int ck=0;
    FOR(i,0,l) {
        keys[ck]++;
        res += keys[ck]*freq[i].first;
        ck=(ck+1)%k;
    }

    return res;
}


int main() {
    int cases;
    cin >> cases;
	FOR(i,0,cases) {
        int p,k,l;
	    cin >> p >> k >> l;
        vector< pair<int,int> > freq;
	    FOR(j,0,l) {
	        int f;
	        cin >> f;
	        freq.push_back(make_pair(f,j));
	    }
		cout << "Case #" << (i+1) << ": ";
        int r = solve(p,k,l,freq);
        if(r < 0) cout << "Impossible";
        else cout << r;
        cout << endl;
	}
	return 0;
}

