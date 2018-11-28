#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <queue>
#include <stack>
#include <iterator>

using namespace std;

char combine[256][256];
bool oppose[256][256];

int main()
{
	int T;
	cin >> T;
	for(int iter = 0; iter < T; iter++)
	{
		memset(combine, 0, sizeof(combine));
		memset(oppose, 0, sizeof(oppose));

		stack<char> st;
		int C, D, N;

		cin >> C;
		for(int i = 0; i < C; i++)
		{
			char c1, c2, res;
			cin >> c1 >> c2 >> res;
			combine[c1][c2] = combine[c2][c1] = res;
		}

		cin >> D;
		for(int i = 0; i < D; i++)
		{
			char d1, d2;
			cin >> d1 >> d2;
			oppose[d1][d2] = oppose[d2][d1] = 1;
		}
		
		cin >> N;
		for(int i = 0; i < N; i++)
		{
			char ch;
			cin >> ch;

			while(!st.empty() && combine[ch][st.top()])
			{
				ch = combine[ch][st.top()];
				st.pop();
			}
			st.push(ch);

			stack<char> tmp;
			bool flag = 0;
			while(!st.empty())
			{
				if(oppose[st.top()][ch])
				{
					flag = 1;
					break;
				}
				tmp.push(st.top());
				st.pop();
			}
			if(flag)
			{
				while(!st.empty())
					st.pop();
			}else{
				while(!tmp.empty())
				{
					st.push(tmp.top());
					tmp.pop();
				}
			}
		}

		fprintf(stdout, "Case #%d: [", iter+1);

		vector<char> v;
		while(!st.empty())
		{
			v.push_back(st.top());
			st.pop();
		}
		for(vector<char>::reverse_iterator it = v.rbegin(); it != v.rend(); it++)
		{
			if(it != v.rbegin())
				fprintf(stdout, ", ");
			fprintf(stdout, "%c", *it);
		}
		fprintf(stdout, "]\n");
	}
	return 0;
}

