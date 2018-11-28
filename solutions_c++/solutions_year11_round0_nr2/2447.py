#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <iterator>
#include <algorithm>
#include <utility>

#include <cassert>

using namespace std;

int main()
{
	size_t tests;
	cin>>tests;
	for (size_t testn = 0; testn<tests; ++testn)
	{
		// read lists
		size_t c;
		cin>>c;
		map<pair<char, char>, char> combine;
		for (size_t i = 0; i<c; ++i)
		{
			string s;
			cin>>s;
			assert(s.size()==3);
			combine[make_pair(s[1], s[0])] = combine[make_pair(s[0], s[1])] = s[2];
		}
		size_t d;
		cin>>d;
		multimap<char, char> oppose;
		for (size_t i = 0; i<d; ++i)
		{
			string s;
			cin>>s;
			assert(s.size()==2);
			pair<char, char> a = make_pair(s[0], s[1]);
			oppose.insert(a);
			a = make_pair(s[1], s[0]);
			oppose.insert(a);
		}
		size_t n;
		cin>>n;
		string s;
		cin>>s;
		assert(n==s.size());
		typedef deque<char> buf_t;
		//typedef vector<char> buf_t;
		buf_t buf;
		typedef map<char, size_t> in_buf_t;
		in_buf_t in_buf;
		for (size_t i = 0; i<n; ++i)
		{
			if (buf.empty())
			{
				buf.push_back(s[i]);
				in_buf_t::iterator iter = in_buf.find(s[i]);
				if (iter==in_buf.end())
					in_buf[s[i]] = 1;
				else
					++iter->second;
			}
			else
			{
				map<pair<char, char>, char>::const_iterator combi = combine.find(make_pair(s[i], buf.back()));
				if (combi!=combine.end())
				{
					--in_buf[buf.back()];
					buf.pop_back();
					buf.push_back(combi->second);
					in_buf_t::iterator iter = in_buf.find(combi->second);
					if (iter==in_buf.end())
						in_buf[combi->second] = 1;
					else
						++iter->second;
				}
				else
				{
					pair<multimap<char, char>::iterator, multimap<char, char>::iterator> range = oppose.equal_range(s[i]);
					bool found = false;
					for (multimap<char, char>::iterator it = range.first; !found && it!=range.second; ++it)
					{
						map<char, size_t>::const_iterator iter = in_buf.find(it->second);
						if (iter!=in_buf.end() && iter->second)
							found = true;
						/*if (in_buf.find(it->second)!=in_buf.end() && in_buf[it->second])
							found = true;*/
					}
					if (found)
					{// clear
						buf.clear();
						in_buf.clear();
					}
					else
					{
						buf.push_back(s[i]);
						in_buf_t::iterator iter = in_buf.find(s[i]);
						if (iter==in_buf.end())
							in_buf[s[i]] = 1;
						else
							++iter->second;
					}
				}
			}
		}
		cout<<"Case #"<<testn+1<<": [";
		for (buf_t::const_iterator i = buf.begin(); i!=buf.end(); ++i)
		{
			if (i!=buf.begin())
				cout<<", ";
			cout<<*i;
		}
		cout<<"]"<<endl;
	}
}

