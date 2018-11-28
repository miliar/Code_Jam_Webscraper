#include <iostream>
#include <vector>

#include <cassert>

using namespace std;

int main()
{
	size_t tests;
	cin>>tests;
	for (size_t testn = 0; testn<tests; ++testn)
	{
		size_t n;
		cin>>n;
		vector<size_t> b, o;
		vector<pair<size_t, char> > u;
		for (size_t i = 0; i<n; ++i)
		{
			char c;
			size_t m;
			cin>>c>>m;
			u.push_back(make_pair(m-1, c));
			if (c=='O')
				o.push_back(m-1);
			else if (c=='B')
				b.push_back(m-1);
			else
				assert(false);
		}
		size_t ox = 0, bx = 0, oi = 0, bi = 0, tick = 0;
		while (oi<o.size() || bi<b.size())
		{
			++tick;
			bool pushed = false;
			if (oi<o.size())
			{
				if (!pushed && ox==o[oi] && u[oi+bi].second=='O' && u[oi+bi].first==o[oi])
				{
					// PUSH
					++oi;
					pushed = true;
				}
				else if (ox!=o[oi])
				{
					if (ox>o[oi])
						--ox;
					else if (ox<o[oi])
						++ox;
					else
						assert(false);
				}
			}
			if (bi<b.size())
			{
				if (!pushed && bx==b[bi] && u[oi+bi].second=='B' && u[oi+bi].first==b[bi])
				{
					// PUSH
					++bi;
					pushed = true;
				}
				else if (bx!=b[bi])
				{
					if (bx>b[bi])
						--bx;
					else if (bx<b[bi])
						++bx;
					else
						assert(false);
				}
			}
		}
		cout<<"Case #"<<testn+1<<": "<<tick<<endl;
	}
}

