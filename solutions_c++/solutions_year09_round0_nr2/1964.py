// Q2

// MACROS
#define PRINT(X, K) cout << "Case #" << X << ": " << K << endl;
#define FOREACH(T, I, J) for (T::iterator I = J.begin(); I != J.end(); ++I)
#define FOREACH_CONST(T, I, J) for (T::const_iterator I = J.begin(); I != J.end(); ++I)

#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

class Graph;
class Node;
enum Direction {
	NORTH, WEST, EAST, SOUTH
};
typedef map<Direction, Node*> NodeChildren;

/**
 * *******************************************
 * NODE!!!
 * *******************************************
 */
class Node {

public:
	unsigned id;
	NodeChildren neighbours;

	// extras
	Graph *parent;
	int level;
	unsigned basin;

	Node(unsigned _id, Graph *p, int lv) : id(_id), parent(p), level(lv), basin(0) { }
	void connect(Node* n, Direction dir);
	static Direction opposite(Direction d);
	unsigned getBasin();
	static string getDir(Direction d) {
		switch(d) {
		case WEST:
			return "WEST";
		case EAST:
			return "EAST";
		case NORTH:
			return "NORTH";
		default:
			return "SOUTH";
		}
	}

};


/**
 * *******************************************
 * GRAPH!!!
 * *******************************************
 */

typedef map<unsigned, Node*> Nodes;
typedef map<unsigned, char> BasinLevels;

class Graph {

public:

	unsigned count;
	unsigned basin;
	unsigned rows, cols;
	Nodes nodes;

	// construct
	Graph(unsigned r, unsigned c) : count(0), basin(1), rows(r), cols(c) { }
	~Graph() {
		FOREACH(Nodes, nit, nodes) {
			delete nit->second;
		}
	}

	// insert
	void insert(int lv) {
		nodes[count] = new Node(count++, this, lv);
	}

	// link all
	void linkAll() {

		for (unsigned i = 0; i != rows; ++i) {
			for (unsigned j = 0; j != (cols-1); ++j) {
				nodes[i*cols + j]->connect(nodes[i*cols + 1 + j], EAST);
			}
		}

		for (unsigned i = 0; i != cols; ++i) {
			for (unsigned j = 0; j != (rows-1); ++j) {
				nodes[j * cols + i]->connect(nodes[((j+1) * cols) + i], SOUTH);
			}
		}

	}

	// solve basin
	void solveBasin() {
		FOREACH(Nodes, nit, nodes) {
			if (nit->second->basin == 0) {
				nit->second->getBasin();
			}
		}
	}

	void print(BasinLevels &bs) {

		for (unsigned i = 0; i != rows; ++i) {

			cout << bs[nodes[i*cols]->basin];
			for (unsigned j = 1; j != cols; ++j) {
				cout << ' ' << bs[nodes[i*cols + j]->basin];
			}
			cout << endl;

		}

	}


};

// connect
void Node::connect(Node* n, Direction dir) {
	neighbours[dir] = n;
	n->neighbours[opposite(dir)] = this;
}

// opposite
Direction Node::opposite(Direction d) {

	switch(d) {
	case WEST:
		return EAST;
	case EAST:
		return WEST;
	case NORTH:
		return SOUTH;
	default:
		return NORTH;
	}

}

unsigned Node::getBasin() {

	if (basin == 0) {
		string dir = "SELF";
		Node *target = this;
		FOREACH(NodeChildren, nit, neighbours) {
			if (nit->second->level < target->level) {
				target = nit->second;
				dir = getDir(nit->first);
			}
		}

		if (target == this) {
			basin = (parent->basin)++;
		} else {
			basin = target->getBasin();
		}

	}

	return basin;

}

int main(void) {

	/**
	 * T = number of maps
	 */
	stringstream ss("a b c d e f g h i j k l m n o p q r s t u v w x y z");
	unsigned n(1);
	char c;
	map<unsigned, char> basinlabels;
	while (ss >> c) {
		basinlabels[n++] = c;
	}

	unsigned T;
	cin >> T;

	for (unsigned tc = 0; tc != T; ++tc) {

		unsigned r, c, ttl, lvl;
		cin >> r >> c;
		ttl = r*c;

		Graph g(r,c);
		for (unsigned i = 0; i != ttl; ++i) {
			cin >> lvl;
			g.insert(lvl);
		}

		g.linkAll();
		g.solveBasin();
		cout << "Case #" << tc+1 << ':' << endl;
		g.print(basinlabels);

	}


	return 0;

}
