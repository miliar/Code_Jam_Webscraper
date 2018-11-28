#include <iostream>
#include <vector>
using namespace std;


struct Node {
	bool C; // changeable
	int G; // 0 = OR, 1 = AND
	int v; // value, or -1 (interior node)
	int min; // minimum subtree changes to alter value; -1 if impossible
	Node(bool C = false, int G = 0, int v = -1, int min = -1)
		: C(C), G(G), v(v), min(min) { }
};


int N, M, V;
vector<Node> nodes;


void test(Node& node, int v1, int v2, int G, int req, int *min) {
	int v = ((G == 0) ? (v1 || v2) : (v1 && v2));
	if (v != node.v) {
		if ((-1 == *min) || (req < *min))
			*min = req;
	}
}


int main()
{
	cin >> N;
	for (int testCase=1; testCase<=N; ++testCase) {
		cin >> M >> V;
		nodes.assign(M+1, Node());
		for (int i=1; i<=M; ++i) {
			if (i <= ((M-1)/2)) {
				int G, C;
				cin >> G >> C;
				nodes[i] = Node(C, G, -1);
			} else {
				int v;
				cin >> v;
				nodes[i] = Node(false, 0, v);
			}
		}
		for (int i = (M-1)/2; i >= 1; --i) {
			Node& node = nodes[i];
			Node& node1 = nodes[i*2];
			Node& node2 = nodes[i*2 + 1];
			if (node.G == 0)
				node.v = node1.v || node2.v;
			else
				node.v = node1.v && node2.v;
			if (node.C) test(node, node1.v, node2.v, 1-node.G, 1, &node.min);
			if (node1.min >= 0) test(node, !node1.v, node2.v, node.G, node1.min, &node.min);
			if (node2.min >= 0) test(node, node1.v, !node2.v, node.G, node2.min, &node.min);
			if (node1.min >= 0 && node2.min >= 0) test(node, !node1.v, !node2.v, node.G, node1.min + node2.min, &node.min);
			if (node.C && node1.min >= 0) test(node, !node1.v, node2.v, 1 - node.G, node1.min + 1, &node.min);
			if (node.C && node2.min >= 0) test(node, node1.v, !node2.v, 1 - node.G, node2.min + 1, &node.min);
			if (node.C && node1.min >= 0 && node2.min >= 0) test(node, !node1.v, !node2.v, 1 - node.G, node1.min + node2.min + 1, &node.min);
		}
		cout << "Case #" << testCase << ": ";
		if (nodes[1].v == V) {
			cout << "0";
		} else {
			if (nodes[1].min == -1)
				cout << "IMPOSSIBLE";
			else
				cout << nodes[1].min;
		}
		cout << endl;
	}
}
