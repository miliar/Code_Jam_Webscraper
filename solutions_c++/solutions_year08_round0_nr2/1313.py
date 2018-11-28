#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <queue>
using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	
	int n;
	cin >> n;

	vector< pair< pair<int, int>, char> > sch;
	priority_queue<int> availA,availB;

	for(int test=0; test<n; test++)
	{
		int ansA=0, ansB=0;
		int T,na,nb;
		int tmp,t1,t2;
		char dummy;
		sch.clear();
		while(!availA.empty())
			availA.pop();
		while(!availB.empty())
			availB.pop();
		cin >> T >> na >> nb;
		for(int i=0; i<na; i++)
		{
			cin >> tmp;
			t1 = tmp*60;
			cin >> dummy >> tmp;
			t1 += tmp;

			cin >> tmp;
			t2 = tmp*60;
			cin >> dummy >> tmp;
			t2 += tmp;

			sch.push_back( make_pair(make_pair(t1,t2),'A') );
		}		
		for(int i=0; i<nb; i++)
		{
			cin >> tmp;
			t1 = tmp*60;
			cin >> dummy >> tmp;
			t1 += tmp;

			cin >> tmp;
			t2 = tmp*60;
			cin >> dummy >> tmp;
			t2 += tmp;

			sch.push_back( make_pair(make_pair(t1,t2),'B') );
		}
		sort(sch.begin(), sch.end());
		
		int m=sch.size();
		for(int i=0;i<m;i++)
		{
			if(sch[i].second == 'A')
			{
				if(availA.empty())
				{
					ansA++;					
				}
				else
				{
					if(-availA.top() <= sch[i].first.first)
						availA.pop();
					else
						ansA++;
				}
				availB.push(-sch[i].first.second - T);
			}
			else
			{
				if(availB.empty())
				{
					ansB++;					
				}
				else
				{
					if(-availB.top() <= sch[i].first.first)
						availB.pop();
					else
						ansB++;
				}
				availA.push(-sch[i].first.second - T);
			}
		}

		cout << "Case #" << test+1 << ": " << ansA << " " << ansB << endl;				
	}
	return 0;
}
