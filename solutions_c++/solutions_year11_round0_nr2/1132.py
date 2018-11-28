#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

map<string, string> comb;
set<string> opp;
string lst[500];

bool Check(int pos)
{
	for(int i=0; i<pos; i++)
	{
		string s = lst[pos];
		s += lst[i];
		if(opp.find(s) != opp.end()) return true;
	}
	return false;
}

bool Check(int pos, string t)
{
	for(int i=0; i<pos; i++)
	{
		string s = t;
		s += lst[i];
		if(opp.find(s) != opp.end()) return true;
	}
	return false;
}


int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	//freopen("XXX-large.out", "w", stdout);
	int test, cas = 1;
	cin>>test;
	while(test--)
	{
		int i, j;
		int C, D, N;
		char buf[500];
		comb.clear();
		opp.clear();
		cin>>C;
		for(i=0; i<C; i++)
		{
			string s, t;
			scanf("%s", buf);
			s = buf[0];
			s += buf[1];
			t = buf[2];
			comb[s] = t;
			//cout << " add " << s << "->" << t << endl;
			s =  buf[1];
			s += buf[0];
			comb[s] = t;
			//cout << " add " << s << "->" << t << endl;
		}
		cin>>D;
		for (i=0; i<D; i++)
		{
			string s;
			scanf("%s", buf);
			s = buf[0];
			s += buf[1];
			opp.insert(s);
			//cout << "add " << s << endl;
			s = buf[1];
			s += buf[0];
			opp.insert(s);
			//cout << "add " << s << endl;
		}
		cin>>N;
		scanf("%s", buf);
	
		int M = 1;
		lst[0] = buf[0];
		i = 1;
		while(i<N)
		{
			string nw = "";
			nw = buf[i];
			lst[M++] = nw;

			while(M>=2)
			{
				string s = lst[M-2] + lst[M-1];
				if(comb.find(s) != comb.end())
				{
					lst[M-2] = comb[s];
					M--;
				}
				else if(Check(M-1))
				{
					M = 0;
					break;
				}
				else break;
			}

			i++;
		}
		cout << "Case #" << cas++ << ": ";
		if(M>0)
		{
			cout<<"[";
			for(i=0; i<M-1; i++) cout << lst[i] <<", ";
			cout << lst[i] << "]\n";
		}
		else cout << "[]" << endl;
		
	}
	return 0;
}