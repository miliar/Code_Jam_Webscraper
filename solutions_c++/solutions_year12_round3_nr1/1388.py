#include <boost/graph/adjacency_list.hpp>
#include <boost/graph/depth_first_search.hpp>
#include <cassert>
#include <iostream>

using namespace std;
using boost::adjacency_list;
using boost::bidirectionalS;
using boost::default_color_type;
using boost::default_dfs_visitor;
using boost::vecS;
using boost::vertex_index;

typedef adjacency_list<vecS, vecS, bidirectionalS> Graph;

struct Visitor : default_dfs_visitor {
	bool& yes;
	Visitor(bool& yes) : yes(yes) { }

	void forward_or_cross_edge(
			Graph::edge_descriptor e,
			const Graph& g)
	{
		yes = true;
	}
};

static const char* testcase()
{
	unsigned n;
	cin >> n;
	assert(cin);
	Graph g(n);
	for (int ui = 0; ui < n; ++ui) {
		unsigned m;
		cin >> m;
		assert(cin);
		for (int i = 0; i < m; ++i) {
			unsigned vi;
			cin >> vi;
			assert(cin);
			assert(vi > 0);
			vi--;
			assert(vi < num_vertices(g));
			add_edge(ui, vi, g);
			cerr << ui << " -> " << vi << '\n';
		}
	}

	bool yes = false;
	Visitor vis(yes);
	Graph::vertex_iterator uit, ulast;
	for (tie(uit, ulast) = vertices(g);
			uit != ulast; ++uit) {
		Graph::vertex_descriptor u = *uit;
		if (in_degree(u, g) == 0) {
			std::vector<default_color_type> colorMap(num_vertices(g));
			depth_first_visit(g, u, vis,
					make_iterator_property_map(&colorMap[0],
						get(vertex_index, g)));
			if (yes)
				return "Yes";
		}
	}
	return "No";
}

int main()
{
	unsigned t;
	cin >> t;
	assert(cin);
	for (int i = 0; i < t; ++i) {
		cerr << "digraph " << i + 1 << '\n';
		cout << "Case #" << i + 1 << ": " << testcase() << '\n';
		cerr << "}\n";
	}
	return 0;
}
