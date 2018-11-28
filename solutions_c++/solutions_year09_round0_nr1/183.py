#include "stdafx.h"

#include <fstream>
#include <string>
#include <vector>
#include <set>
using namespace std;

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	int L,D,N; // L is length, D is number of alien words, N is number of test cases
	fin >> L >> D >> N;

	vector<set<string> > comp(L);
	for (int i=0; i<D; ++i) {
		string s; fin >> s; comp.back().insert(s); }

	for (int i=L-1; i>0; --i)
		for (set<string>::iterator it = comp[i].begin(), end = comp[i].end(); it!=end; ++it)
			comp[i-1].insert(it->substr(0,i));

	for (int z=1; z<=N; ++z)
	{
		int pos = 0, cl = 0;
		set<string> last, next;
		string s; fin >> s;
		while (pos < int(s.length()))
		{
			int loc1 = s.find("(", pos), loc2 = s.find(")", pos);
			if (loc1 < 0) loc1 = s.length();
			if (loc1 > pos)
			{
				string ss = s.substr(pos, loc1-pos);
				if (pos == 0)
				{
					if (comp[ss.length()-1].count(ss) > 0)
						next.insert(ss);
				}
				else
				{
					for (set<string>::iterator it = last.begin(), end = last.end(); it!=end; ++it)
					{
						string newss = *it + ss;
						if (comp[newss.length()-1].count(newss) > 0)
							next.insert(newss);
					}
				}
				pos = loc1;
			}
			else
			{
				vector<string> chars;
				for (int i=loc1+1; i<loc2; ++i)
					chars.push_back(s.substr(i,1));
				
				if (pos == 0)
				{
					for (int i=0; i<int(chars.size()); ++i)
						if (comp[0].count(chars[i]) > 0)
							next.insert(chars[i]);
				}
				else
				{
					for (set<string>::iterator it = last.begin(), end = last.end(); it!=end; ++it)
						for (int i=0; i<int(chars.size()); ++i)
						{
							string newss = *it + chars[i];
							if (comp[newss.length()-1].count(newss) > 0)
								next.insert(newss);
						}
				}
				pos = loc2+1;
			}
			last.swap(next); next.clear();
		}

		fout << "Case #" << z << ": " << last.size() << endl;
	}

	return 0;
}

