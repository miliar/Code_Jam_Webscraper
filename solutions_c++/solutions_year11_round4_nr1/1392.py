#include <iostream>
#include <vector>
#include <cstring>
#include <map>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <queue>
#include <stack>
using namespace std;

main ()
{
	int t;
	cin >> t;

	for (int T = 1; T <= t; T++)
	{
		cout << "Case #" << T << ": ";
		int X,S,R,N;
		double tt;

		cin >> X >> S >> R >>tt >> N;
		double ans = 0;
		vector < pair < pair <int,int> , int > > tracks(N);
		for (int i = 0; i < N; i++)
		{
			cin >> tracks[i].first.first >> tracks[i].first.second >> tracks[i].second;
			
		}

		sort(tracks.begin(),tracks.end());
		vector < pair <int, pair <int,int> > > patch; 
		int x = 0;
		for (int i = 0; i < N; i++)
		{
			if (fabs(x-X) <= 1e-9) break;
			if (x < tracks[i].first.first)
			{
				pair <int,int> p(x,tracks[i].first.first);
				pair < int , pair <int,int> > q(0,p);
				patch.push_back(q);
			}
			
			if (tracks[i].first.second > X) x = X; 
			else x = tracks[i].first.second;			
			pair <int,int> p(tracks[i].first.first,x);
			pair <int, pair <int,int> > q(tracks[i].second,p);
			patch.push_back(q);
			
		}
		if (x < X)
		{
			pair <int,int> p(x,X);
			pair < int , pair <int,int> > q(0,p);
			patch.push_back(q);
		}

		sort(patch.begin(),patch.end());

		
                for(int i=0;i<patch.size();i++)
                {
                    double dist=patch[i].second.second-patch[i].second.first;
                    double speed=patch[i].first+R;
                    if(speed*tt>dist)
                    {
                        ans+=(double)dist/(double)speed;
                        tt-=(double)dist/(double)speed;
                    }
                    else
                    {
                        dist-=tt*speed;
                        ans+=tt;
                        tt=0;
                        double newspeed=patch[i].first+S;
                        ans+=dist/newspeed;
                    }
                }
		cout << fixed;
		cout << setprecision(8) << ans << "\n";
			
	}
}
