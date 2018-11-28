#include <map>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
void trim(string &s) {
     s = s.erase(s.find_last_not_of("\r\n") + 1);
     s = s.erase(0, s.find_first_not_of("\r\n"));
}
string readline() {
    string line;
    getline(cin, line); trim(line);
    return line;
}
void read1(int &a) {
    string l = readline();
    sscanf(l.c_str(), "%d", &a);
}
void read2(int &a, int &b) {
    string l = readline();
    sscanf(l.c_str(), "%d %d", &a, &b);
}
int minimal, am, N, V;
vector<int> tree, change;
void solver(int pos, int changes) {
    if (pos == am) {
        vector<int> tree2(N, 0);
	for (int x = N - 1; x > -1; x--) {
	    if (x >= am) {
	        tree2[x] = tree[x];
	    } else {
	        if (tree[x]) {
	            tree2[x] = tree2[(x*2+1)] && tree2[(x*2+2)];
		} else {
	            tree2[x] = tree2[(x*2+1)] || tree2[(x*2+2)];
		}
	    }
	}
	if (tree2[0] != V) return;
        if (changes < minimal || minimal == -1) minimal = changes;
        return;
    }
    solver(pos + 1, changes);
    if (change[pos]) {
        tree[pos] = 1 - tree[pos];
        solver(pos + 1, changes + 1);
	tree[pos] = 1 - tree[pos];
    }
}
void _case(int i) {
    int G, C;
    cin >> N >> V;
    tree.resize(N); change.resize(N);
    for (int x = 0; x < N; x++) tree[x] = change[x] = 0;
    for (int x = 0; x < (N - 1) / 2; x++) {
        cin >> tree[x] >> change[x];
    }
    for (int x = (N - 1) / 2; x < N; x++) {
        cin >> tree[x];
	change[x] = 0;
    }
    minimal = -1; am = (N - 1) /2;
    solver(0, 0);
    if (minimal > -1) 
        cout << "Case #" << i << ": " << minimal << endl;
    else
	cout << "Case #" << i << ": IMPOSSIBLE" << endl;
}
int main() {
    int n, i = 1;
    cin >> n;
    while (n--) _case(i++);
    return 0;
}

