#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
#include <cstring>
#include <set>
#include <stack>


using namespace std;

ifstream in("large.in");
ofstream out("large.out");

map <string, char> para;
set <string> op;
stack <char> st;

string em;

bool kaOp(char c)
{
	bool answer = false;
	stack <char> q;
	while (!st.empty())
	{
		q.push(st.top());

		if (op.find(em + c + st.top()) != op.end())
			answer = true;

		st.pop();
	}

	while (!q.empty())
	{
		st.push(q.top());
		q.pop();
	}
	
	return answer;
}

void clear()
{
	while (!st.empty())
		st.pop();
}

void tpel(int t)
{
	out << "Case #" << t << ": [";

	stack <char> q;
	while (!st.empty())
	{
		q.push(st.top());
		st.pop();
	}

	bool start = true;

	while (!q.empty())
	{
		if (start)
			out << q.top();
		else
			out << ", " << q.top();
		st.push(q.top());
		q.pop();		
		start = false;
	}
	out << "]" << endl;
}

int main()
{
	int test, t,numberOfPairs,numberOfOp,i,n;
	string s;
	
	em = "";

	in >> test;

	for (t = 1 ;t <= test; ++t)
	{
		para.clear();
		
		in >> numberOfPairs;
		while (numberOfPairs--)
		{
			in >> s;
			para[em + s[0] + s[1]] = s[2];
			para[em + s[1] + s[0]] = s[2];
		}

		op.clear();
		in >> numberOfOp;
		while (numberOfOp--)
		{
			in >> s;
			op.insert(s);
			op.insert(em + s[1] + s[0]);
		}

		in >> n >> s;

		clear();

		for (i = 0 ; i < s.size(); ++i)
		{			
			if (!st.empty())
			{
				string bar = em + st.top() + s[i];
				if (para.find(bar) != para.end())
				{
					st.pop();
					st.push(para[bar]);
				}
				else
				{
					if (kaOp(s[i]))
					{
						clear();
					}
					else
						st.push(s[i]);
				}			
			}
			else
				st.push(s[i]);
		}

		tpel(t);


	}

	return 0;
}