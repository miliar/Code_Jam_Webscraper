#include <algorithm> 
#include <cassert>
#include <cctype> 
#include <cstdio> 
#include <cstdlib> 
#include <cmath> 
#include <cstring> 
#include <iostream>
#include <map> 
#include <set> 
#include <string> 
#include <sstream>
#include <queue> 
#include <vector> 
using namespace std;

int T,N,M, res;
vector <string> ini, todo;
struct vertex;
vector <vertex> tr;


vector <string> parse(string s)
{
	vector <string> r;
	string cur="";
	for (int i=1; i<s.size(); i++)
	{
		if (s[i]=='/')
		{
			r.push_back(cur);
			cur="";
		}
		else cur+=s[i];
	}
	r.push_back(cur);
	return r;
}

struct vertex
{
public:
	string name;
	map <string, int> chi;
};

int add(string di)
{
	vector <string> li;
	li = parse(di);
	int  r=0, curv=0;
	vertex cur;
	for (int i=0; i<li.size(); i++)
	{
		if (tr[curv].chi.find(li[i])==tr[curv].chi.end())
		{
			cur.name=li[i];
			cur.chi.clear();
			tr.push_back(cur);
			tr[curv].chi.insert(make_pair(li[i],tr.size()-1));
			r++;
			curv=tr.size()-1;
		}
		else
			curv=tr[curv].chi[li[i]];
	}
	return r;
}





void solve()
{
	vertex cur;
	res=0;
	cur.name="";
	tr.clear();
	tr.push_back(cur);
	for (int i=0; i<N; i++)
		add(ini[i]);
	for (int i=0; i<M; i++)
		res += add(todo[i]);

}

void write(int i)
{
	printf("Case #%d: %d\n", i, res);

}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	char buf[1000];
	string s;


	scanf("%d",&T);
	gets(buf);

	for (int i=0; i<T; i++)
	{
		
		scanf("%d%d",&N, &M);
		gets(buf);
		ini.clear(); todo.clear();
		for (int j=0; j<N; j++)
		{
			gets(buf);
			s=buf;
			ini.push_back(s);
		}
		for (int j=0; j<M; j++)
		{
			gets(buf);
			s=buf;
			todo.push_back(s);
		}
		solve();
		write(i+1);
		
	}

	return 0;
}
