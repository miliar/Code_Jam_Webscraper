#include <vector>
#include <string>
#include <queue>
#include <map>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef double ret_t;
typedef int cost_t;

const int INF = 1000000000;

struct Pos {
public:
    Pos():x(0), y(0), cost(0) {
    }
    int x, y;
    
    cost_t cost;
};

class compare { // for queue
public:
    bool operator()(const Pos & a, const Pos & b) const {
	return a.cost > b.cost; // here > means lower costs go first
    }
};

class Solver {
public:
    vector<vector<cost_t> > m;
    priority_queue<Pos, vector<Pos>, compare> q;
    bool improvement(Pos p) {
	return p.cost <= m[p.x][p.y];
    }
    bool strictimprovement(Pos p) {
	return p.cost < m[p.x][p.y];
    }
    void visit(Pos p) {
	if (strictimprovement(p)) {
	    m[p.x][p.y] = p.cost;
	    q.push(p);
	}
    }
    ret_t solve(int lvl, int h, int w, vector<vector<int> > cei, vector<vector<int> > flr) {
	m = vector<vector<int> >(h, vector<int>(w, INF));
	Pos p;
	visit(p);
	do {
	    p = q.top();
	    q.pop();
	    if (p.x == h - 1 && p.y == w - 1) {
		return (double)p.cost / 10; // done
	    }
	    if (!improvement(p)) {
		continue;
	    }
	    
	    // explore from p:
	    for (int dx = -1; dx <= 1; ++dx) {
		for (int dy = -1; dy <= 1; ++dy) {
		    if (dx + dy == 0)
			continue;
		    if (dx - dy == 0)
			continue;
		    if (p.x + dx < 0 || p.x + dx >= h)
			continue;
		    if (p.y + dy < 0 || p.y + dy >= w)
		        continue;
		    Pos p2 = p;
			p2.x += dx;
			p2.y += dy;
			if (cei[p.x][p.y] < flr[p2.x][p2.y] + 50)
			    continue;
			if (cei[p2.x][p2.y] < flr[p.x][p.y] + 50)
			    continue;
			if (cei[p2.x][p2.y] < flr[p2.x][p2.y] + 50)
			    continue;
			int earliest = lvl + 50 - cei[p2.x][p2.y];
			p2.cost = max(p2.cost, earliest);
			if (p2.cost > 0) {
			    if (lvl - p2.cost - 20 >= flr[p.x][p.y])
				p2.cost += 10;
			    else
				p2.cost += 100;
			}
			visit(p2);
	        }
	    }
	} while (!q.empty());
	return INF;
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
        int lev, h, w;
	vector<vector<int> > cei;
	vector<vector<int> > flr;
        {
            stringstream A(s);
            A >> lev >> h >> w;
	    cei = vector<vector<int> >(h, vector<int>(w));
	    flr = vector<vector<int> >(h, vector<int>(w));
	    for (int i = 0; i < h; ++i) {
		getline(cin, s);
		stringstream B(s);
		for (int j = 0; j < w; ++j)
		    B >> cei[i][j];
	    }
	    for (int i = 0; i < h; ++i) {
		getline(cin, s);
		stringstream B(s);
		for (int j = 0; j < w; ++j)
		    B >> flr[i][j];
	    }
        }
        ret_t ret = solver.solve(lev, h, w, cei, flr);

        // *** give output ***
        cout << "Case #" << no << ": " << ret << endl; // one line
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
