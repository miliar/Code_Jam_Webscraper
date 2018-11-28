#include <iostream>
#include <vector>
#include <queue>


using namespace std;


vector< pair< pair<int, int>, int> > TB;
//vector<int> TA;
priority_queue<int> Q[2];
int main()
{

	int N;
	int NA, NB, i;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin>>N;
	int tt = 0;
	
	while (N--)
	{
		int T;
		tt++;
		cin>>T;
		//while (T--)
		{
			cin>>NA>>NB;
			TB.clear();
			//TA.clear();
			for (i = 0; i < NA; i++)
			{
				int h1,h2,m;
				char ch;
				cin>>h1>>ch>>m;
				h1= h1 * 60 + m;
				cin>>h2>>ch>>m;
				h2 = h2 * 60 + m;
				TB.push_back(make_pair( make_pair(h1, h2), 0) );
			}

			for (i = 0; i < NB; i++)
			{
				int h1,h2,m;
				char ch;
				cin>>h1>>ch>>m;
				h1= h1 * 60 + m;
				cin>>h2>>ch>>m;
				h2 = h2 * 60 + m;
				TB.push_back(make_pair( make_pair(h1, h2), 1) );
			}
		}

			sort(TB.begin(), TB.end());

			while (!Q[0].empty()) Q[0].pop();
			while (!Q[1].empty()) Q[1].pop();
			


			int ans[2] = {0, 0};


			for (i = 0; i < NA + NB; i++)
			{
				int g = TB[i].second;
				//int t = -Q[g].top();
				if ( Q[g].empty() || ( (-Q[g].top()) > TB[i].first.first) )
				{
					ans[g]++;
					
				}
				else
				{
					Q[g].pop();
				}

				Q[1-g].push( -(TB[i].first.second + T) );
			}

			cout<<"Case #"<<tt<<": "<<ans[0]<<' '<<ans[1]<<endl;

	}

	return 0;
}