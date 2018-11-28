#include <iostream>
#include <map>
#include <vector>
#include <set>
#include <fstream>
using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	cin >> T;
	for(int t(0); t < T; ++t)
	{
		map<pair<char,char>,char> combination;
		int C(0);
		cin >> C;
		char s1, s2, s3;
		for(int i(0); i < C; ++i)
		{
			cin >> s1 >> s2 >> s3;
			combination.insert(make_pair(make_pair(s1, s2), s3));
			combination.insert(make_pair(make_pair(s2, s1), s3));
		}
		int D(0);
		cin >> D;
		set<pair<char,char> > opposed;
		for(int i(0); i < D; ++i)
		{
			cin >> s1 >> s2;
			opposed.insert(make_pair(s1, s2));
			opposed.insert(make_pair(s2, s1));
		}
		int N(0);
		cin >> N;
		vector<char> let(N, '0');
		int end(0);
		map<pair<char,char>,char>::iterator comb;
		map<char,char>::iterator opos;
		cin >> let[0];
		int tmp(0);
		bool f(false);
		for(int i(1); i < N; ++i)
		{
			f = false;
			cin >> s1;
			let[++end] = s1;
			if(end > 0)
			{
				comb = combination.find(make_pair(let[end],let[end - 1]));
				if(comb != combination.end())
				{
					--end;
					let[end] = comb->second;
					f = true;
				}
			}
			for(int tmp(end - 1); tmp >= 0; --tmp)
			{
				if(opposed.find(make_pair(let[tmp], let[end])) != opposed.end())
				{
					end = -1;
					f = true;
					break;
				}
			}
			
		}
		cout << "Case #" << t + 1 << ": ["; 
		for(int i(0); i < end; ++i)
			cout << let[i] << ", ";
		if(end >= 0) 
			cout << let[end];
		cout << "]" << endl;
	}
	return 0;
}