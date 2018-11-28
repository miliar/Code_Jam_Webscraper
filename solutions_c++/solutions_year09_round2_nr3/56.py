/* small-C.cc
 */
#include <iostream>
#include <string>
#include <cstring>
#include <map>
using namespace std;
int T, W, Q, q;
string S[10];
typedef map<int,string> map_t;
map_t all[100];

void add(int sum, const string& path, int i, int j, int di, int dj,
	 int di2, int dj2, bool& added) 
{
    if (i+di+di2 < 0 || i+di+di2 >= W || j+dj+dj2 < 0 || j+dj+dj2 >= W)
	return;

    string new_path = path + S[i+di][j+dj];
    i += di+di2, j += dj+dj2;
    if (*new_path.rbegin() == '+')
	sum += S[i][j]-'0';
    else
	sum -= S[i][j]-'0';
    new_path += S[i][j];
    map_t::iterator p = all[i*10+j].find(sum);
    if (p == all[i*10+j].end()) {
	// cerr << sum << ' ' << new_path << endl;
	all[i*10+j][sum] = new_path, added = true;
	return;
    }
    if (p->second.size() == new_path.size()
	&& p->second != new_path
	&& lexicographical_compare(new_path.begin(), new_path.end(),
				   p->second.begin(), p->second.end()))
    {
	// cerr << sum << ' ' << new_path << endl;
	p->second = new_path, added = true;
    }
}

void add(int sum, const string& path, int i, int j, int di, int dj,
    bool& added) 
{
    if (i+di < 0 || i+di >= W || j+dj < 0 || j+dj >= W)
	return;
    add(sum, path, i, j, di, dj,  1, 0, added);
    add(sum, path, i, j, di, dj, -1, 0, added);
    add(sum, path, i, j, di, dj,  0, 1, added);
    add(sum, path, i, j, di, dj,  0,-1, added);

}
void run()
{
    for (int i=0; i<100; ++i) all[i].clear();
	for (int i=0; i<W; ++i) 
	    for (int j=0; j<W; ++j)
		if (isdigit(S[i][j])) {
		    all[i*10+j][S[i][j]-'0'] = S[i][j];
		    if (S[i][j]-'0' == q) {
			cout << q << endl;
			return;
		    }
		}
    bool added = true;
    for (int d=1; added; ++d) {
	// cerr << "depth " << d << ' ' << q << endl;
	for (int i=0; i<W; ++i) {
	    for (int j=0; j<W; ++j) {
		if (! isdigit(S[i][j])) continue;
		for (map_t::const_iterator p=all[i*10+j].begin();
		     p!=all[i*10+j].end(); ++p) {
		    if (p->second.size() != d*2-1) continue;
		    add(p->first, p->second, i, j, -1, 0, added);
		    add(p->first, p->second, i, j, +1, 0, added);
		    add(p->first, p->second, i, j, 0, -1, added);
		    add(p->first, p->second, i, j, 0, +1, added);
		}
	    }
	}
	string solution;
	for (int i=0; i<W; ++i) {
	    for (int j=0; j<W; ++j) {
		if (! isdigit(S[i][j])) continue;
		map_t::const_iterator p=all[i*10+j].find(q);
		if (p == all[i*10+j].end()) continue;
		if (solution == ""
		    || lexicographical_compare(p->second.begin(), p->second.end(),
					       solution.begin(), solution.end()))
		    solution = p->second;
	    }
	}
	if (solution != "") {
	    cout << solution << endl;
	    return;
	}
    }
}

int main() {
    cin >> T;
    for (int t=0; t<T; ++t) {
	cout << "Case #" << t+1 << ":\n";
	cin >> W >> Q;
	for (int i=0; i<W; ++i) cin >> S[i];
	for (int i=0; i<100; ++i) all[i].clear();
	for (int i=0; i<Q; ++i) {
	    cin >> q;
	    run();
	}
    }
}
