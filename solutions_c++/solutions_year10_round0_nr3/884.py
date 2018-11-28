#include <iostream>
#include <set>
#include <vector>
#include <cassert>
using namespace std;

typedef long long LL;

bool lookup(set<vector<int> > sv, vector<int> v)
{
	set<vector<int> >::const_iterator it;
	for(it=sv.begin(); it!=sv.end(); ++it)
	{
		int n = v.size();
		int i;
		for(i=0; i < n; i++)
		{
			if ((*it)[i] != v[i])
				break;
		}
		if (i >= n) return true;
	}
	return false;
}

LL solve()
{
	LL ret = 0;
	LL R, k;
	int N;
	cin >> R >> k >> N;
	vector<int> groups;
	for(int i=0; i < N; i++)
	{ int g; cin >> g; groups.push_back(g); }

	//cout << R << " " << k << " " << N << endl;

	set<vector<int> > confs;
	int r;
	for(r=0; r < R; r++)
	{
		if (confs.find(groups) != confs.end())
			break;
		confs.insert(groups);
		LL sum = 0;
		int p;
		for(p=0; p < N; p++)
		{
			if (sum + groups[p] > k)
				break;
			sum += groups[p];
		}
//		cout << sum << endl;
		assert(sum <= k);

		ret += sum;
//		cout << "p " << p << endl;
		p = p%N;
		vector<int> g2;
		for(int i=p; i < N; i++)
			g2.push_back(groups[i]);
		for(int i=0; i < p; i++)
			g2.push_back(groups[i]);
		groups = g2;
	}
//	cout << r << endl;
//	cout << confs.size() << " " << ret << endl;
	if (r < R)
	{
		LL loop= 0LL;
		LL len = 0LL;
		vector<int> lead = groups;
//		int cnt = 0;
		do
		{
		++len; //cout << len << endl;
		LL sum = 0;
		int p;
		for(p=0; p < N; p++)
		{
			if (sum + groups[p] > k)
				break;
			sum += groups[p];
		}
		loop += sum;
		p = p%N;
		vector<int> g2;
		for(int i=p; i < N; i++)
			g2.push_back(groups[i]);
		for(int i=0; i < p; i++)
			g2.push_back(groups[i]);
		groups = g2;
//		cnt++; assert(cnt < N);
		} while(groups != lead);

		ret += (R-r)/len * loop;

		assert(groups == lead);
		int lim = (R-r)%len;
		for(int rr=0; rr < lim; rr++)
		{
		LL sum = 0;
		int p;
		for(p=0; p < N; p++)
		{
			if (sum + groups[p] > k)
				break;
			sum += groups[p];
		}
		ret += sum;
		p = p%N;
		vector<int> g2;
		for(int i=p; i < N; i++)
			g2.push_back(groups[i]);
		for(int i=0; i < p; i++)
			g2.push_back(groups[i]);
		groups = g2;
		}
	}
	return ret;
}

int main()
{
	int ncase; cin >> ncase;
	for(int icase = 0; icase < ncase; ++icase)
	{
		LL ret = solve();
		cout << "Case #" << (icase+1) << ": " << ret << endl;
	}
}
