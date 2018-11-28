#include <stack>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

using namespace std;

int index(char c)
{
	return c-65;
}


int main()
{
	freopen("B-small-attempt2.in","r",stdin);
	freopen("B-small-attempt2.out","w",stdout);

	int n = 0;
	scanf("%d", &n);

	for (int i = 0; i < n; ++i)
	{
		char combtable[50][50] = {0};
		char conftable[50] = {0};
		char opfound[50] = {0};
		int comb = 0, conf = 0, l = 0;
		scanf("%d", &comb);
		for (int j = 0; j < comb; ++j)
		{
			char pat[4];
			scanf("%s", &pat);
			int first = index(pat[0]);
			int second = index(pat[1]);
			combtable[first][second] = pat[2];
			combtable[second][first] = pat[2];
		}
		scanf("%d", &conf);
		for (int j = 0; j < conf; ++j)
		{
			char pat[3];
			scanf("%s", &pat);
			int first = index(pat[0]);
			int second = index(pat[1]);
			conftable[first] = pat[1];
			conftable[second] = pat[0];
		}
		scanf("%d ", &l);
		stack<char> var;
		var.push('^');

		for (int j = 0; j < l; ++j)
		{
			char c;
			scanf("%c", &c);

			int c_index = index(c);
			int top_index = index(var.top());
			
			if (combtable[c_index][top_index] != 0) //combine
			{
				var.pop();
				var.push(combtable[c_index][top_index]);
				--opfound[top_index];
				++opfound[combtable[c_index][top_index]-65];
			} 
			else //not combine
			{
				if (conftable[c_index] == 0 || opfound[conftable[c_index]-65] == 0) //not conflict
				{
					var.push(c);
					++opfound[c_index];
				} 
				else //conflict
				{
					while(var.top() != '^')
					{
						--opfound[index(var.top())];
						var.pop();
					}
				}
			}
		}
		
		stack<char> output;
		while(var.top() != '^')
		{
			output.push(var.top());
			var.pop();
		}
		printf("Case #%d: [", i+1);
		while (!output.empty())
		{
			printf("%c", output.top());
			if (output.size() > 1) 
			{
				printf(", ");
			}
			output.pop();
		}
		printf("]\n");
		

	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}