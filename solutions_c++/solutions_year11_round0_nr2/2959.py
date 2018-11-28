#include <iostream>
#include <list>
#include <string>
#include <map>
#include <set>

using namespace std;

map<pair<char,char>,char> comb;
set<pair<char,char> > oppose;

void process(int t, string& s)
{
	int i;
	list<char> curr;
	curr.push_back(s[0]);
	for(i=1; i<s.size(); i++)
	{
		//cout << "processing i="<< i << ", c=" << s[i] << endl;
		char incoming=s[i];
		while(1)
		{
			if (curr.size() == 0) break;
			pair<char,char> p1 = make_pair(incoming, curr.back());
			pair<char,char> p2 = make_pair(curr.back(), incoming);
			if(comb.count(p1) > 0 || comb.count(p2) > 0)
			{	
				char out='?';
				if(comb.count(p1) > 0)
					out=comb[p1];
				else
					out=comb[p2];
				curr.pop_back();
				incoming = out;
			}
			else
				break;
		}
		bool cleared = false;
		list<char>::iterator it = curr.begin();
		for(; it!=curr.end(); it++)
		{
			if(oppose.count(make_pair(*it, incoming)) > 0 ||
			   oppose.count(make_pair(incoming, *it))> 0 )
			{
				curr.clear();
				cleared=true;
				break;
			}		
		}
		if (!cleared) curr.push_back(incoming);
	}
	
	cout << "Case #" << t << ": [";
	list<char>::iterator it = curr.begin();
	for(int cnt=0; it!=curr.end(); it++, cnt++)
	{
		if (cnt==0) cout << *it;
		else cout << ", " << *it;
	}
	cout << "]" << endl;
}

int main (int argc, char * const argv[]) {
    int T, C, D, N;
	cin >> T;
	for(int i=0; i<T; i++)
	{
		cin >> C;
		int j;
		for(j =0; j<C;j++)
		{
			string s;
			cin >> s;
			comb[make_pair(s[0],s[1])]=s[2];
			comb[make_pair(s[1],s[0])]=s[2];
		}
		cin >> D;
		for(j=0; j<D; j++)
		{
			string s;
			cin >> s;
			oppose.insert(make_pair(s[0], s[1]));
			oppose.insert(make_pair(s[0], s[1]));
		}
		cin >> N;
		string s;
		cin >> s;
		
		process(i+1, s);
		comb.clear();
		oppose.clear();
	}
    return 0;
}
