#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

class UnionFind {
public:
	UnionFind(int n_):n(n_), p(vector<int>(n)), rank(vector<int>(n, 0)) {for (int i = 0; i < n; ++i) p[i] = i;}
	int find(int a) {
		int root; for (root = a; p[root] != root; root = p[root]) ;
		while (p[a] != root) {int t = p[a]; p[a] = root; a = t;}
		return root;
	}
	void merge(int a, int b) { // aka union: merge a's and b's sets
		a = find(a); b = find(b); if (a == b) return;
		if (rank[a] > rank[b])
			p[b] = a;
		else {
			if (rank[a] == rank[b]) ++rank[b];
			p[a] = b;
		}
	}
	int n;
	vector<int> p, rank;
};

typedef vector<string> ret_t;

class Solver {
public:
    ret_t solve(vector<vector<int> > mp) {
        int h = mp.size();
        int w = mp[0].size();
        vector<string> ret(h, string(w, '?'));
        UnionFind U(h*w);
        for (int i = 0; i < h; ++i) for (int j = 0; j < w; ++j) {
            int to = -1;
            int toh = mp[i][j];
            if (i > 0 && mp[i-1][j] < toh) to = w*(i-1)+j, toh = mp[i-1][j];
            if (j > 0 && mp[i][j-1] < toh) to = w*i+(j-1), toh = mp[i][j-1];
            if (j<w-1 && mp[i][j+1] < toh) to = w*i+(j+1), toh = mp[i][j+1];
            if (i<h-1 && mp[i+1][j] < toh) to = w*(i+1)+j, toh = mp[i+1][j];
            if (to != -1) U.merge(w*i+j, to);
        }
        string label(h*w, '-');
        char letter = 'a';
        for (int i = 0; i < h; ++i) for (int j = 0; j < w; ++j) {
            if (label[U.find(w*i+j)] == '-') {
                label[U.find(w*i+j)] = letter;
                ret[i][j] = letter;
                letter++;
            }
            else {
                ret[i][j] = label[U.find(w*i+j)];
            }
        }
        return ret;
	}
};

int main(int argc, char ** argv) {
    string s;
    int N;
    getline(cin, s);
    {
        stringstream A(s);
        A >> N;
    }
    for (int no = 1; no <= N; ++no) {
        cerr << "Case " << no << " / " << N << endl;
        Solver solver;
        // *** get input ***
        getline(cin, s);
        int h, w;
        {
            stringstream A(s);
            A >> h >> w;
        }
        vector<vector<int> > mp(h, vector<int>(w));
        for (int i = 0; i < h; ++i) {
            getline(cin, s);
            stringstream A(s);
            for (int j = 0; j < w; ++j) A >> mp[i][j];
        }
        ret_t ret = solver.solve(mp);

        // *** give output ***
        //cout << "Case #" << no << ": " << ret << endl; // one line
        cout << "Case #" << no << ":\n"; // multi-line
        for (int i = 0; i < ret.size(); ++i) {
            for (int j = 0; j < ret[i].size(); ++j)
                cout << ret[i][j] << ' ';
            cout << endl;
        }
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
