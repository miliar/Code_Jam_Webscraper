#include <iostream>
#include <iomanip>
#include <vector>
#include <map>
#include <string>

#include <cstdio>
#include <cassert>

using namespace std;

typedef long double d_t;

d_t get_wp(const string &game)
{
	size_t n = game.size();
	size_t w = 0;
	size_t p = 0;
	for (size_t j = 0; j<n; ++j)
	{
		if (game[j]!='.')
		{
			++p;
			if (game[j]=='1')
				++w;
		}
	}
	return static_cast<d_t>(w)/static_cast<d_t>(p);
}

int main(int argc, char **argv)
{
	freopen(argv[1], "r", stdin);
	size_t tests;
	cin>>tests;
	for (size_t testn = 1; testn<=tests; ++testn)
	{
		size_t n;
		cin>>n;
		vector<string> games(n);
		for (size_t i = 0; i<n; ++i)
		{
			cin>>games[i];
			assert(games[i].size()==n);
			assert(games[i][i]=='.');
		}
		vector<d_t> wp(n), owp(n), oowp(n);
		//wp
		for (size_t i = 0; i<n; ++i)
		{
			wp[i] = get_wp(games[i]);
		}
		//owp
		for (size_t i = 0; i<n; ++i)
		{
			size_t p = 0;
			owp[i] = 0;
			for (size_t j = 0; j<n; ++j)
			{
				if (games[i][j]!='.')
				{
					++p;
					string game = games[j];
					game[i] = '.';
					owp[i] += get_wp(game);
				}
			}
			owp[i]/=p;
		}
		//oowp
		for (size_t i = 0; i<n; ++i)
		{
			size_t p = 0;
			oowp[i] = 0;
			for (size_t j = 0; j<n; ++j)
			{
				if (games[i][j]!='.')
				{
					++p;
					oowp[i]+=owp[j];
				}
			}
			oowp[i]/=p;
		}
		cout<<"Case #"<<testn<<":"<<endl;
		for (size_t i = 0; i<n; ++i)
		{
			cout<<fixed<<setprecision(12)<<( (wp[i]/4) + (owp[i]/2) + (oowp[i]/4) )<<endl;
		}
	}
}

