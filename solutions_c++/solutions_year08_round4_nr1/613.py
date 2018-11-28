#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <set>
#include <iterator>
#include <map>
#include <iomanip>
#include <cmath>

using namespace std;

enum Op {AND, OR, LEAF};

class Node;

vector<Node> tree;

class Node {

public:
	bool changeable;
	
	int minChanges[2];
	
	int value;
	
	int index;
	
	inline int father() { return (index-1) / 2; }
	inline int son1()   { return 2*index+1; } 
	inline int son2()   { return 2*index+2; }
	
	Op op;
	
	Node(Op _op, bool _c, int _index, int _value) : op(_op), changeable(_c), value(_value), index(_index) {
		minChanges[0] = minChanges[1] = -1;
	} 
	
	int changes(int v) {
		
	//	cout << "Trying to change node " << index << " into " << v << endl;
		
		if (minChanges[v] != -1) {
	//		cout << "Min changes is " << minChanges[v] << endl;
			return minChanges[v];
		}
		
		if (op == LEAF) {
	//		cout << "I am a leaf" << endl;
			if (v == value) return 0;
			else return INT_MAX/3;
		}

		int m = INT_MAX/3;
		
		if (v == 0) {
			if (op == AND || changeable) {
		//		cout << "AND: " << endl;
				m = min(m, tree[son1()].changes(0) + (op == OR && changeable));
				m = min(m, tree[son2()].changes(0) + (op == OR && changeable));
			//	cout << m << endl;
			}
			if (op == OR) {
	//			cout << "OR: " << endl;
				m = min(m, tree[son1()].changes(0)+tree[son2()].changes(0));
		//		cout << m << endl;
			}
		} else {
			if (op == OR || changeable) {
		//	cout << "OR : " << endl;
				m = min(m, tree[son1()].changes(1) + (op == AND && changeable));
				m = min(m, tree[son2()].changes(1) + (op == AND && changeable));
			//	cout << "END OR "<< m << endl;
			}
			if (op == AND) {
			//	cout << "AND: " << endl;
				m = min(m, tree[son1()].changes(1)+tree[son2()].changes(1));
			//	cout <<  m << endl;
			}
		}
		
	//	cout << "m is " << m << endl;
		return minChanges[v] = (m >= INT_MAX/3 ? INT_MAX/3:m);
	}
};

int main()
{
	int C;
	cin >> C;
	for (int c=0;c<C;c++) {

		cout << "Case #" << c+1 << ": ";

		int M, V;
		cin >> M >> V;
		
		tree.clear();
		
		for (int i=0;i<(M-1)/2; i++) {
			int G, C;
			cin >> G >> C;
			tree.push_back(Node((G==1?AND:OR), (C==1), i, -1));
		}

		for (int i=(M-1)/2;i<M; i++) {
			int I;
			cin >> I;
			tree.push_back(Node(LEAF, 0, i, I));
		}
		
		int c = tree[0].changes(V);
		if (c == INT_MAX/3) cout << "IMPOSSIBLE" << endl;
		else cout << c << endl;
	}
}
