#include <cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class singer
{
	public:
		int t, score, supscore;
		void computeScore(int p)
		{
			if(t%3==0)
			{
				if(p<=t/3)
				{
					score = 1;
					supscore = 1;
				}
				else if(p==t/3+1)
				{
					score = 0;
					supscore = 1;
				}
				else
				{
					score = 0;
					supscore = 0;
				}
			}
			else if(t%3==1)
			{
				if(p<=t/3+1)
				{
					score = 1;
					supscore = 1;
				}
				else
				{
					score = 0;
					supscore = 0;
				}
			}
			else if(t%3==2)
			{
				if(p<=t/3+1)
				{
					score = 1;
					supscore = 1;
				}
				else if(p==t/3+2)
				{
					score = 0;
					supscore = 1;
				}
				else
				{
					score = 0;
					supscore = 0;
				}
			}
			else
			{
				cout << "DUPA!!!";
			}
			//cout << t << " " << score << " " << supscore << "\n";
		}
		bool operator<(const singer& s) const 
		{
			return supscore-score>s.supscore-s.score;
		}
};


int main(int argc, char *argv[])
{
    int t;
    cin >> t;
    singer lol;
    for(int icase=0;icase<t;++icase)
    {
		int n,s,p,t;
		int sum=0;
		vector<singer> tab;
		cin >> n >> s >> p;
		for(int i=0;i<n;++i)
		{
			cin >> t;
			if(t==0)
			{
				if(p==0)
					sum++;
			}
			else if(t==1)
			{
				if(p<=1)
					sum++;
			}
			else
			{
				tab.push_back(lol);
				tab.back().t = t;
				tab.back().computeScore(p);
			}
		}
		sort(tab.begin(), tab.end());
		for(int i=0;i<tab.size();++i)
			if(i<s)
				sum+=tab[i].supscore;
			else
				sum+=tab[i].score;
		cout << "Case #" << icase+1 << ": " << sum << "\n";
    } 
    return EXIT_SUCCESS;
}

