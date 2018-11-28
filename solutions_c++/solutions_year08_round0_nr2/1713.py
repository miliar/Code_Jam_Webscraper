#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
using namespace std;
const int INF = 100000000;
struct S {
	int d, a;
	S(int nd = 0, int na = 0) : d(nd), a(na) {}
	bool operator< (const S & s) const { return d < s.d || (d == s.d && a < s.a); }
};

struct Q {
	int x;
	Q(int nx = 0) : x(nx) {}
	bool operator< (const Q q) const { return x > q.x; }
};
int main()
{
	int n;
	scanf("%d",&n);
	for (int a = 1; a <= n; ++a)
	{
		priority_queue<Q> q1,q2;
		int t,n1,n2;
		scanf("%d%d%d\n",&t,&n1,&n2);
		vector<S> v1, v2;
		int hd, md, ha, ma;
		for (int i = 0; i < n1; ++i) { scanf("%d:%d %d:%d\n",&hd,&md,&ha,&ma); v1.push_back(S(hd*60+md,ha*60+ma)); }
		for (int i = 0; i < n2; ++i) { scanf("%d:%d %d:%d\n",&hd,&md,&ha,&ma); v2.push_back(S(hd*60+md,ha*60+ma)); }
		v1.push_back(S(INF,INF));
		v2.push_back(S(INF,INF));
		sort(v1.begin(),v1.end());
		sort(v2.begin(),v2.end());
		int i1 = 0, i2 = 0;
		int r1 = 0, r2 = 0;
		q1.push(Q(INF));
		q2.push(Q(INF));
		while (i1 < n1 || i2 < n2)
		{
			if (v1[i1].d < v2[i2].d)
			{
				int tp = q1.top().x;
				if (tp <= v1[i1].d)
					q1.pop();
				else
					++r1;
				q2.push(Q(v1[i1].a+t));
				++i1;
			}
			else
			{
				int tp = q2.top().x;
				if (tp <= v2[i2].d)
					q2.pop();
				else
					++r2;
				q1.push(Q(v2[i2].a+t));
				++i2;
			}
		}
		while (!q1.empty()) q1.pop();
		while(!q2.empty()) q2.pop();
		cout << "Case #" << a << ": " << r1 << ' ' << r2 << endl;
	}
	return 0;
}

