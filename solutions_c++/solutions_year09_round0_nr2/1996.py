#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <numeric>
#include <list>
#include <bitset>
#include <cstring>
#include <sys/time.h>
#include <sys/signal.h>
#include <unistd.h>
#include <stack>
#include <cmath>
#include <map>
#include <streambuf>
#include <ctime>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
#define FOR(x,a,e) for( x=a; x<=(e); ++x)
#define FORL(x,a,e) for(int x=a; x<(e); ++x)
#define FORD(x,a,e) for(int x=a; x>=(e); --x)
#define FORDG(x,a,e) for(int x=a; x>(e); --x)
#define REP(x,n) for(int x =0;x<(n); ++x)
#define VAR(v,n) __typeof(n) v = (n)
#define ALL(c) (c).begin(),(c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i,c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second

int main()
{
	int T,H,W;
	cin >> T;
	int i,j,k;
	FORL(i,0,T)
	{
		cin >> H;
		cin >> W;
		vector<vector<int> > data(H,vector<int>());
		vector<vector<int> > scores(H,vector<int>());
		map<int, vector<pair<int,int> > >areas;
		int areas_counter = 0;

		FORL(j,0,H)
		{
			(data[j]).assign(W,-1);
			(scores[j]).assign(W,-1);
		}

		FORL(j,0,H)
		{
			FORL(k,0,W)
			{
				cin >> data[j][k];
			}
		}
		FORL(j,0,H)
		{
			FORL(k,0,W)
			{
				//cout<<"J = "<<j<<" K = "<<k<<endl;
				pair<int,int> dest = make_pair(0,0);
				int altitude       = 1000001;
				if (j>0 && data[j-1][k] < data[j][k] && data[j-1][k] < altitude)
				{
					altitude = data[j-1][k];
					dest     = make_pair(j-1,k);
				}

				if (k>0 && data[j][k-1] < data[j][k] && data[j][k-1] < altitude)
				{
					altitude = data[j][k-1];
					dest     = make_pair(j,k-1);
				}

				if (k<(W-1) && data[j][k+1] < data[j][k] && data[j][k+1] < altitude)
				{
					altitude = data[j][k+1];
					dest     = make_pair(j,k+1);
				}

				if (j<(H-1) && data[j+1][k] < data[j][k] && data[j+1][k] < altitude)
				{
					altitude = data[j+1][k];
					dest     = make_pair(j+1,k);
				}

				//cout<<"Altitude = "<<altitude<<endl;
				//cout<<"Scores   = "<<scores[j][k]<<" "<<scores[dest.ST][dest.ND]<<endl;
				if (altitude == 1000001)
				{
					if (scores[j][k] == -1)
					{
						scores[j][k] = ++areas_counter;
						areas[areas_counter] = vector<pair<int,int> >();
						(areas[areas_counter]).PB(make_pair(j,k));
					}
				}
				else
				{
					if (scores[j][k] != -1 && scores[dest.ST][dest.ND] == -1)
					{
						scores[dest.ST][dest.ND] = scores[j][k];
						(areas[scores[j][k]]).PB(make_pair(dest.ST, dest.ND));
					}
					else if (scores[j][k] == -1 && scores[dest.ST][dest.ND] != -1)
					{
						scores[j][k] = scores[dest.ST][dest.ND];
						(areas[scores[dest.ST][dest.ND]]).PB(make_pair(j,k));
					}
					else if (scores[j][k] == -1 && scores[dest.ST][dest.ND] == -1)
					{
						++areas_counter;
						scores[dest.ST][dest.ND] = areas_counter;
						scores[j][k]             = areas_counter;
						areas[areas_counter] = vector<pair<int,int> >();
						(areas[areas_counter]).PB(make_pair(j,k));
						(areas[areas_counter]).PB(make_pair(dest.ST,dest.ND));
					}
					else
					{
						if (scores[j][k] < scores[dest.ST][dest.ND])
						{
							vector<pair<int,int> > to_change;
							FOREACH(it, areas[scores[dest.ST][dest.ND]])
							{
								to_change.PB(make_pair(it->ST,it->ND));
							}
							(areas[scores[dest.ST][dest.ND]]).clear();
							FOREACH(it, to_change)
							{
								scores[it->ST][it->ND] = scores[j][k];
								(areas[scores[j][k]]).PB(*it);

							}
						}
						else if (scores[j][k] > scores[dest.ST][dest.ND])
						{
							vector<pair<int,int> > to_change;
							FOREACH(it, areas[scores[j][k]])
							{
								to_change.PB(make_pair(it->ST,it->ND));
							}
							(areas[scores[j][k]]).clear();
							FOREACH(it, to_change)
							{
								scores[it->ST][it->ND] = scores[dest.ST][dest.ND];
								(areas[scores[dest.ST][dest.ND]]).PB(*it);

							}
						}
					}
				}
			}
		}

		int diff = 0;
		vector<int> differences(areas_counter+1,0);
		int l;
		FOR(l,1,areas_counter)
		{
			if ( SIZE(areas[l]) == 0)
				++diff;
			else
				differences[l] += diff;
		}

		cout<<"Case #"<<i+1<<":"<<endl;
		FORL(j,0,H)
		{
			bool p = false;
			FORL(k,0,W)
			{
				scores[j][k] -= differences[scores[j][k]];
				if (p) cout<<" ";
				cout<<(char)(96+scores[j][k]);
				p = true;
			}
			cout<<endl;
		}
	}
	return 0;
}
