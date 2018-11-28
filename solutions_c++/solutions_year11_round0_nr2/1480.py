#include <string>
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <string.h>

using namespace std;

const int MAX = 300;
const int MAXE = 105;

char com[MAX][MAX];
char opp[MAX][MAX];

char ele[MAXE];

void go()
{
	memset(com, 0, sizeof(com));
	memset(opp, 0, sizeof(opp));

	int C, D, N;
	scanf("%d", &C);
	for(int i = 0; i < C; i++)
	{
		char ch[5];
		scanf("%s", ch);

		com[ch[0]][ch[1]] = ch[2];
		com[ch[1]][ch[0]] = ch[2];
	}

	scanf("%d", &D);
	for(int i = 0; i < D; i++)
	{
		char ch[5];
		scanf("%s", ch);
	
		opp[ch[0]][ch[1]] = 1;
		opp[ch[1]][ch[0]] = 1;	
	}

	scanf("%d%s", &N, ele);
	
	vector<char> ans;

	for(int i = 0; i < N; i++)
	{
		if(ans.size() == 0)
		{
			ans.push_back(ele[i]);
			continue;
		}
		
		char tmp = com[ele[i]][ans[ans.size() - 1]];

		if(tmp)  ans[ans.size() - 1] = tmp;
		else
		{
			int j, len = ans.size();
			for(j = 0; j < len; j++)
			{
				if(opp[ans[j]][ele[i]])
				{
					/*
					vector<char> ans_t;
					for(int k = 0; k < j; k++)
						ans_t.push_back(ans[k]);

					ans = ans_t;
					*/
					
					ans.clear();

					break;
				}
			}
			if(j == len)  ans.push_back(ele[i]);
		}
	}

	printf("[");
	if(ans.size())  
	{
		printf("%c", ans[0]);

		for(int i = 1; i < ans.size(); i++)
			printf(", %c", ans[i]);
	}
	printf("]\n");

}

int main()
{
	freopen("f:\\B-large.in", "r", stdin);
	freopen("f:\\B-large.out", "w", stdout);

	int T, c = 0;
	scanf("%d", &T);
	while(T--)
	{
		printf("Case #%d: ", ++c);
		go();
	}
}