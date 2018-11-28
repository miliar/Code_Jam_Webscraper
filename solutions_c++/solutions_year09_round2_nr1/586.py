#include <iostream>
#include <sstream>
#include <string>
#include <map>
#include <stdlib.h>
#include <iomanip>
using namespace std;
int C;
struct Node{
	double v;
	string s;
	int end;
} nodes[10000];
//int pos[][];
map<string, int> vv;
void built(int root, string s)
{
	int i;
	for(i = 0; i < s.length(); i++) if(s[i] == '(') break;
	s = s.substr(i+1);
	for(i = s.length() - 1; i >= 0; i--) if(s[i] == ')') break;
	s = s.substr(0, i);
	int k = 0, flag = 0, ii;
	for(i = 0; i < s.length(); i++)
	{
		if(s[i] == '(')
		{
			if(k == 0) ii = i;
			k++, flag = 1;
		}
		if(s[i] == ')') k--;
		if(flag && k == 0) break;
	}
	if(flag)
	{
		istringstream istr(s);
		istr>>nodes[root].v>>nodes[root].s;
		built((root<<1), s.substr(ii, i+1-ii));
		built((root<<1)+1, s.substr(i+1));
	}
	else
	{
		istringstream istr(s);
		istr>>nodes[root].v;
		nodes[root].end = 1;
	}
}
double value(int root)
{
	if(nodes[root].end) return nodes[root].v;
	if(vv[nodes[root].s])
	{
		return nodes[root].v * value(root<<1);
	}
	else
		return nodes[root].v * value((root<<1) + 1);
}
double solve()
{
	double ans = 0;
	return value(1);
}
int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
//	freopen("in.txt", "r", stdin);
//	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	cin>>C;
	int Case;
	for(Case = 1; Case <= C; Case++)
	{
		int i;
		for(i = 0; i < 10000; i++) nodes[i].end = 0, nodes[i].s = "", nodes[i].v = 0;
		int L;
		cin>>L;
		cin.ignore();
		string s = "";
		string t;
		while(L--) getline(cin, t), s = s + " " + t;
		built(1, s);
		int N, M;
		cin>>N;
		cout<<"Case #"<<Case<<":\n";
		
		while(N--)
		{
			vv.clear();
			cin>>t>>M;
			//double ans = 0;
			for(i = 0; i < M; i++)
			{
				cin>>t;
				vv[t] = 1;
			}
			cout<<fixed<<setprecision(7)<<solve()<<endl;
		}
		//printf("Case #%d: %d\n", Case, solve());
	}
}