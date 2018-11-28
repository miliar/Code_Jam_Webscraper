#include <iostream>
#include <fstream>

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

ifstream fin("GCJ Round 2 A.txt");
#define cin fin

ofstream fout("out.txt");
#define cout fout

set<vector<int> >st;

int Solve(vector<int>vec)
{
	st.clear();
	queue<pair<vector<int>, int> >q;
	pair<vector<int>, int>p = make_pair(vec, 0);
	q.push(p);
	st.insert(vec);

	while(!q.empty())
	{
		p = q.front();
		vec = p.first;
		q.pop();

		//cout<<p.second<<" "<<st.size()<<endl;

		int i;
		bool eshta = 1;
		for(i=0; i<vec.size(); i++)
		{
			if(vec[i] > i)
				eshta = 0;
		}
		if(eshta)
			return p.second;
		for(i=0; i<vec.size() - 1; i++)
		{
			if(vec[i+1] <= i)
			{
				vector<int> nVec = vec;
				nVec[i] = vec[i+1];
				nVec[i+1] = vec[i];
				if(st.find(nVec) == st.end())
				{
					st.insert(nVec);
					pair<vector<int>, int>nP = make_pair(nVec, p.second + 1);
					q.push(nP);
				}
			}
		}
	}
}

int main()
{
	int t, i, j, k, a;
	cin>>t;
	for(k=0; k<t; k++)
	{
		char ch;
		cin>>a;
		vector<int>m(a);
		
		for(i=0; i<a; i++)
		{
			m[i] = -1;
			for(j=0; j<a; j++)
			{
				cin>>ch;
				if(ch == '1')
					m[i] = j;
			}
		}
		st.insert(m);
		int ret = Solve(m);
		//for(j=0; j<a; j++)
		//{
		//	for(i=0; i<a; i++)
		//	{
		//		if(m[i] > i)
		//		{
		//			int tmp = m[i+1];
		//			m[i+1] = m[i];
		//			m[i] = tmp;
		//			ret++;
		//		}
		//	}
		//}
		cout<<"Case #"<<k+1<<": "<<ret<<endl;
	}
	return 0;
}