#include <math.h>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
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

string solve(vector< pair<int,int> > sch) {
    sort(sch.begin(), sch.end());
    vector<int> x(4,0);
    FOR(i,0,sch.size()) {
        int a = sch[i].second;
        switch(a) {
            case 4:
                if(x[0]) x[0]--;
                else x[2]++;
                break;
            case 1:
                x[1]++;
                break;
            case 8:
                if(x[1]) x[1]--;
                else x[3]++;
                break;
            case 2:
                x[0]++;
                break;


        }
    }

    OSS oss;
    oss << x[2] << " " << x[3];
	return oss.str();
}

int main() {
    int cases;
    cin >> cases;
	FOR(i,0,cases) {
	    int t;
	    string s;
	    vector< pair<int,int> > sch;
	    vector<int> tr(2,0);
	    cin >> t >> tr[0] >> tr[1];
        FOR(k,0,2)
            FOR(j,0,tr[k]) {
                int h,m;
                int t1,t2;

                cin >> s;
                sscanf(s.c_str(), "%d:%d", &h, &m);
                t1 = h*60+m;
                sch.push_back(make_pair(t1, 4<<k));

                cin >> s;
                sscanf(s.c_str(), "%d:%d",&h,&m);
                t2 = h*60+m+t;
                sch.push_back(make_pair(t2, 1<<k));
            }


		cout << "Case #" << (i+1) << ": " <<  solve(sch) << endl;
	}
}
