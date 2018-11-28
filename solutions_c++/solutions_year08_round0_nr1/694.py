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
ostream &operator<< (ostream& o, set<string> s) {
    o << "<";
    for (set<string>::iterator i = s.begin(); i != s.end(); i++) {
        o << (*i);
    }
    o << ">";
    return o;
}
#define vector_include(Item, Vector) (find(Vector.begin(), Vector.end(),Item ) != Vector.end())


int solve(vector<string> &e,vector<string> &q) {
    set<string> s;
    int res=0;
    FOR(i,0,q.size()) {
        s.insert(q[i]);
        if(s.size() == e.size()) {
            res++;
            s.clear();
            s.insert(q[i]);
        }
    }
	return res;
}

int main() {
    vector<string> e, q;
    int cases;
    string scases;
    std::getline(cin,scases);
    cases = atoi(scases.c_str());
	FOR(i,0,cases) {
	    int ne,nq;
	    string s;
	    e.clear();
	    q.clear();
        std::getline(cin,s);
        ne = atoi(s.c_str());
	    FOR(j,0,ne) {
	        std::getline(cin,s);
	        e.push_back(s);
        }

        std::getline(cin,s);
        nq = atoi(s.c_str());
	    FOR(j,0,nq) {
            std::getline(cin,s);
	        q.push_back(s);
        }
		cout << "Case #" << (i+1) << ": " <<  solve(e,q) << endl;
	}
}

