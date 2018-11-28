#include<iostream>
#include<deque>
using namespace std;

#define set_len 19

char set[set_len + 1] = "welcome to code jam";

struct process
{
	int word;
	int pos;
	string s;
};

int main()
{
	int i, j, k, n, l;
	deque<process> p;
	process ps, t;
	string s;

	scanf("%d ", &n);

	for(j = 1; j <= n; j++)
	{
		getline(cin, s);
		k = 0;

		for(i = 0; i < s.length(); i++)
		{
			if(s[i] == set[0])
			{
				ps.word = 1;
				ps.pos = i;
				ps.s += i+'0';
				p.push_back(ps);
			}
		}

		while(!p.empty())
		{
			ps = p.front();
			p.pop_front();

			for(i = ps.pos + 1; i < s.length(); i++)
			{
				if(s[i] == set[ps.word])
				{
					t = ps;
					t.word++;
					t.pos = i;
					t.s += i+'0';
					if(t.word == set_len) k++;
					p.push_back(t);
				}
			}
		}

		printf("Case #%d: %04d\n", j, k);
	}
}
