#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <stdio.h>


using namespace std;

#define REP(i,n) for(int i = 0; i < (n); ++i)
#define FORE(it,x) for(typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define CLEAR(x,with) memset(x,with,sizeof(x))  

#define pb push_back
#define all(x) (x).begin(),(x).end()
#define sz(a) int((a).size())

typedef pair<int,int> pii;
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;


struct pqitem
{
	int time; 

	bool operator<(const pqitem &a) const 
	{ 
		return time > a.time; 
	} 
};

int main()
{
	string temp;
	int numCases;
	getline(cin, temp);
	stringstream ss(temp);
	ss >> numCases;

	for(int c=1; c<=numCases; c++)
	{
		int T, NA, NB;
		getline(cin, temp);
		stringstream ss_in(temp);
		ss_in >> T;

		getline(cin, temp);
		stringstream ss_in2(temp);
		ss_in2 >> NA >> NB;
		vector< pair<int, int> > NANA, NBNB;
		for(int i=0; i<NA; i++)
		{
			getline(cin, temp);
			int hour, min, hour2, min2;
			sscanf(temp.c_str(), "%d:%d %d:%d", &hour, &min, &hour2, &min2);
			pair<int, int> pair_of_info;
			pair_of_info.first = hour*60 + min;
			pair_of_info.second = hour2*60 + min2;
			NANA.push_back(pair_of_info);
		}
		for(int i=0; i<NB; i++)
		{
			getline(cin, temp);
			int hour, min, hour2, min2;
			sscanf(temp.c_str(), "%d:%d %d:%d", &hour, &min, &hour2, &min2);
			pair<int, int> pair_of_info;
			pair_of_info.first = hour*60 + min;
			pair_of_info.second = hour2*60 + min2;
			NBNB.push_back(pair_of_info);
		}
		sort( all(NANA) );
		sort( all(NBNB) );

		// start simulation

		priority_queue<pqitem> A_B, B_A;
		vector<int> AA, BB;

		int NANA_i = 0, NBNB_i = 0;
		int ans_A = 0, ans_B = 0;

		for(int i=0; i < 24*60; i++)
		{
			for(int j=0; j<(int)AA.size(); j++) AA[j]--;
			for(int j=0; j<(int)BB.size(); j++) BB[j]--;

			// arrive
			while(!A_B.empty())
			{
				pqitem cur = A_B.top();
				if(cur.time == i)
				{
					A_B.pop();
					BB.push_back(T);
				}
				else break;
			}
			while(!B_A.empty())
			{
				pqitem cur = B_A.top();
				if(cur.time == i)
				{
					B_A.pop();
					AA.push_back(T);
				}
				else break;
			}
			sort( all(AA) );
			sort( all(BB) );

			//departure
			if( NANA_i == (int)NANA.size() && NBNB_i == (int)NBNB.size() ) goto end_this;
			while(NANA_i != (int)NANA.size() && NANA[NANA_i].first == i)
			{
				if(AA.empty() || (!AA.empty() && AA[0] > 0))
					ans_A++;
				else AA.erase(AA.begin());

				pqitem temppq;
				temppq.time = NANA[NANA_i].second;
				A_B.push( temppq );
				NANA_i++;
			}
			while(NBNB_i != (int)NBNB.size() && NBNB[NBNB_i].first == i)
			{
				if(BB.empty() || (!BB.empty() && BB[0] > 0))
					ans_B++;
				else BB.erase(BB.begin());

				pqitem temppq;
				temppq.time = NBNB[NBNB_i].second;
				B_A.push( temppq );
				NBNB_i++;
			}
		}

end_this:;
		cout << "Case #" << c << ": " << ans_A << " " << ans_B << endl;
	}

	return 0;
}
