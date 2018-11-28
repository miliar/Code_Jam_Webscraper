#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <set>

using namespace std;

int N, M;
set <string> st;

void make(string str)
{
	string s;
	int cur = 0;
	while(cur < str.size())
	{
		s.push_back(str[cur++]);
		while(cur < str.size() && str[cur] != '/')
			s.push_back(str[cur++]);
//		cout << s << endl;
		st.insert(s);		
	}
}

int count(string str)
{
	string s;
	int cur = 0, cnt = 0;
	while(cur < str.size())
	{
		s.push_back(str[cur++]);
		while(cur < str.size() && str[cur] != '/')
			s.push_back(str[cur++]);
		if(st.find(s) == st.end())	cnt ++;
		st.insert(s);	
	}
	return cnt;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.out", "w", stdout);
	
	int cases;	cin >> cases;
	for(int cas=1; cas<=cases; cas++)
	{
		st.clear();
		cin >> N >> M;
		string s;
		while(N --)
		{
			cin >> s;
			make(s);	
		}
		int cnt = 0;
		while(M --)
		{
			cin >> s;
			cnt += count(s);	
		}
		printf("Case #%d: %d\n", cas, cnt);
	}
	
	
	return 0;	
}
