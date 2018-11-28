#include <iostream>
#include <vector>
#include <map>

using namespace std;

bool check(vector<pair<int, int> > & a, int D)
{
	vector<char> reached; reached.resize(a.size());
	reached[0] = true;
	vector<int> dist; dist.resize(a.size());
	dist[0] = a[0].first;
	int last_rc = 1;

	for(int i=0; i<a.size(); ++i)
	{
		if(!reached[i])return false;
		int rc = a[i].first + dist[i];
		if(rc>=D)return true;

		for(int j=last_rc; j<a.size(); ++j)
		{
			if(a[j].first<=rc)
			{
				reached[j] = 1;
				++last_rc;
				dist[j] = min(a[j].first - a[i].first, a[j].second);
			}
			else
			{
				break;
			}
		}
	}

	return false;
}

int main()
{
//	freopen("k:/input.txt", "rt", stdin);
	int T;

	cin>>T;

	for(int t=1; t<=T; ++t)
	{
		int N;

		cin>>N;

		vector< pair<int, int> > a;
		map<int, int> tmp;

		int d, l, D;

		for(int i=0; i<N; ++i)
		{
			cin>>d>>l;
			if(tmp[d]<l)tmp[d] = l;
		}

		for(map<int, int>::iterator ii = tmp.begin(); ii!=tmp.end(); ++ii)
		{
			a.push_back(*ii);
		}

		cin>>D;

		cout<<"Case #"<<t<<": ";
		if(check(a, D))
		{
			cout<<"YES"<<endl;
		}
		else
		{
			cout<<"NO"<<endl;
		}
	}

	return 0;
}