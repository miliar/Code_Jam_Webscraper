#include <iostream>
#include <vector>
#include <set>
#include <map>

using namespace std;

void out(const vector<long long> &a1, const vector<long long> &a2)
{
	set<long long> s1(a1.begin(), a1.end());
	set<long long> s2(a2.begin(), a2.end());
	set<long long> s_int;

	for(set<long long>::const_iterator ii = s1.begin(); ii!=s1.end(); ++ii)
	{
		if(s2.find(*ii)!=s2.end())
			s_int.insert(*ii);
	}

	for(set<long long>::const_iterator ii = s1.begin(); ii!=s1.end(); ++ii)
	{
		if(s_int.find(*ii)==s_int.end())
			cout<<*ii<<" ";
	}

	cout<<endl;

	for(set<long long>::const_iterator ii = s2.begin(); ii!=s2.end(); ++ii)
	{
		if(s_int.find(*ii)==s_int.end())
			cout<<*ii<<" ";
	}

	cout<<endl;
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

		vector<long long> x; x.reserve(N);
		long long tm;

		for(int i=0; i<N; ++i)
		{
			cin>>tm;

			x.push_back(tm);
		}

		map<long long, vector<long long> > a;
		a[0] = vector<long long>();

		bool fin = false;

		for(int i=0; i<N; ++i)
		{
			map<long long, vector<long long> > tmp = a;

			for(map<long long, vector<long long> >::const_iterator ii=a.begin(); ii!=a.end(); ++ii)
			{
				long long new_val = ii->first + x[i];
				
				if( tmp.find(new_val)!=tmp.end() )
				{
					// finish
//					cout<<"fin at "<<new_val<<endl;

					vector<long long> a1 = tmp[new_val];
					vector<long long> a2 = ii->second;
					a2.push_back(x[i]);

					cout<<"Case #"<<t<<":"<<endl;
					out(a1,a2);

					fin = true;
					break;
				}
				else
				{
//					cout<<new_val<<endl;
					vector<long long> & s = tmp[new_val];
					s = ii->second;
					s.push_back(x[i]);					
				}
			}

			if(fin)break;
			a = tmp;
		}
	}
	
	return 0;
}