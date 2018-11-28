#include<iostream>
#include<algorithm>
#include<complex>
#include<cstdio>
using namespace std;
int eto(int i, int j)
{
	return i*257 + j + 1;
}

complex<int> inv(int i){
	complex<int> j(i/257,i%257-1);
	return j;
}
#ifndef _sbl_graph
#define _sbl_graph
#include<vector>
struct graph {
	typedef std::vector<int> VI;
	VI info, next, to;
	graph(int n = 0, int m = 0) : to(2), next(2) {
		m += 2;
		info.resize(n);
		next.reserve(m);
		to.reserve(m);
	}
	int edge_size() {
		return to.size()-2;
	}
	int vertex_size(){
		return info.size();
	}
	void expand(int i) {
		if (info.size() < i + 1)
			info.resize(i + 1);
	}
	void add(int i, int j) {
		expand(i), expand(j);
		to.push_back(j);
		next.push_back(info[i]);
		info[i] = to.size() - 1;
	}
	void del_back() {
		int i;
		for (i = 0; i < info.size(); i++)
			if (info[i] == to.size() - 1) {
				info[i] = next.back();
				break;
			}
		to.pop_back();
		next.pop_back();
	}
	void clear() {
		info.clear();
		next.resize(2);
		to.resize(2);
	}
};
#endif 
#ifndef _sbl_dijkstra
#define _sbl_dijkstra
#include<utility>
#include<queue>
#include<climits>


struct graph_with_edge_cost: public graph {
	VI cost;
	graph_with_edge_cost(int n = 0, int m = 0) : graph(n, m), cost(2) {
		cost.reserve(m + 2);
	}
	void add(int i, int j, int k) {
		//cout<<inv(i)<<" --> "<<inv(j)<<" : "<<k<<endl;
		graph::add(i, j);
		cost.push_back(k);
	}
	void del_back() {
		graph::del_back();
		cost.pop_back();
	}
	void clear() {
		graph::clear();
		cost.resize(2);
	}
	VI shortest_path(int be, int en = -1, VI father = VI());    
	VI spfa(int be, int en = -1, VI father = VI());    
	int minimum_spanning_tree(int be = 0, VI father = VI());    
};

std::vector<int> graph_with_edge_cost::shortest_path(int be, int en , VI father)
{
	int i, j, y;
	std::pair<int, int>t;
	VI d(info.size(), INT_MAX), &f = father;
	d[j = be] = 0;
	std::priority_queue<std::pair<int, int> > p;
	while (1) {
		for (i = info[j]; i; i = next[i])
			if (d[y=to[i]] - cost[i] > d[j]) {
				d[y] = d[j] + cost[i];
				if (!f.empty())
					f[y] = j;
				p.push(std::make_pair(-d[y], y));
			}
		do {
			if (p.empty())
				return d;
			t = p.top();
			p.pop();
		} while (d[t.second] != -t.first);
		j = t.second;
		if (j == en)
			break;
	}
	return d;
}
#endif


int a[200], n, D, I, M;

bool can(int a, int b)
{
	if (a == -1 || b == -1)
		return 1;
	if (abs(a - b) <= M)
		return 1;
	return 0;
}


int get_ans()
{
	graph_with_edge_cost g;
	int s = eto(n, -1), t = s + 1;
	for (int i = 0; i <= n; i++)
		for (int j = -1; j <= (i == n ? -1 : 255); j++) {
			int now = eto(i, j);
			if (i == 0)
				g.add(now, t, 0);
			else {
				g.add(now, eto(i - 1, j), D);
				if(i<n)
				for (int l = 0; l <= 255; l++)
					if (can(j, l))
						g.add(now, eto(i, l), I);
				for (int l = 0; l <= 255; l++)
					if (can(j, l))
						g.add(now, eto(i - 1, l), abs(a[i-1] - l));
			}
		}
	return g.shortest_path(s, t)[t];
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int kase;
	cin >> kase;
	for (int kk = 1; kk <= kase; kk++) {
		cout << "Case #" << kk << ": ";
		cin >> D >> I >> M >> n;
		for (int i = 0; i < n; i++)
			cin >> a[i];
		cout << get_ans() << endl;
	}
}
