#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
using namespace std;

struct Node {
	int x, y, r;
};

int N;
vector<Node> ns;

double sq(int x)
{
	return x*x;
}
double dist(int x1, int y1, int x2, int y2)
{
	return sqrt(sq(x1-x2)+sq(y1-y2));
}

double dist(int i, int j)
{
	return dist(ns[i].x,ns[i].y, ns[j].x, ns[j].y);
}

double calc()
{
	if (N == 1) return ns[0].r;
	if (N == 2) {
		//return (ns[0].r+ns[1].r+dist(0,1))/2;
		return ns[0].r > ns[1].r ? ns[0].r : ns[1].r;
	}

	double d01 = (ns[0].r+ns[1].r+dist(0,1))/2;
	double t = ns[2].r;
	double ans = d01>t ? d01 : t;

	double d12 = (ns[1].r+ns[2].r+dist(1,2))/2;
	t = ns[0].r;
	if (d12 > t) t = d12;
	if (t < ans) ans = t;

	double d20 = (ns[2].r+ns[0].r+dist(2,0))/2;
	t = ns[1].r;
	if (d20 > t) t = d20;
	if (t < ans) ans = t;

	return ans;
}

int main(void)
{
	int T;
	cin >> T;
	for (int ca=1; ca<=T; ++ca) {
		cin >> N;
		ns.clear();
		for (int i=0; i<N; ++i) {
			Node node;
			cin >> node.x >> node.y >> node.r;
			ns.push_back(node);
		}

		cout << "Case #" << ca << ": " << calc() << endl;
	}
	return 0;
}
