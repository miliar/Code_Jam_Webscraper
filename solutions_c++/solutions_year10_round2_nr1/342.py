#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <cstdio>
#include <map>
#include <set>
#include <sstream>
#include <strstream>
#include <queue>
#include <stack>
#include <set>
#include <cstring>
#include <string>

using namespace std;

ifstream in("large.in");
ofstream out("large.out");

set <string > st;

int make(string& s)
{
	//cout << s << endl;
	int i;
	int answer = 0;
	string stt = "" + s[0];
	for (i = 1; i < s.size() ; i++)
		if (s[i] != '/')
			stt = stt + s[i];
		else
		{
			if (st.find(stt) == st.end())
				answer++;
			st.insert(stt);
			stt = stt + s[i];
		}
	
	if (stt != "")
	{
		if (st.find(stt) == st.end())
			answer++;
		st.insert(stt);
	}

	return answer;

}

int main()
{
	int test,n,m,i;
	int answer;
	in >> test;
	string s;
	for (int t = 1; t <= test; t++)
	{
		st.clear();
		answer = 0;
		in >> n >> m;
		for (i = 0 ; i < n ; i ++)
		{
			in >> s;
			make(s);
		}

		for (i = 0 ; i < m ; i++)
		{
			in >> s;
			answer += make(s);
		}
		out << "Case #" << t << ": " << answer << endl;
	}
	return 0;
}