#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <vector>
using namespace std;
vector<int> position[28];
int maxchoice[510][21];
char slogan[] = "welcome to code jam";
int length,ql, n;
char question[600];

int myhash(char v)
{
	if (v == ' ') return 26;
	else return v - 'a';
}
void findbest(int index ,int c_position)
{
	if (c_position == length - 1 && index < ql) 
	{
		maxchoice[index][c_position] = 1;
		return;
	}

	int tempans = 0;
	int nextindex;
	int pp = myhash(slogan[c_position + 1]);
	for (int i = 0; i < position[pp].size(); ++i)
		if (position[pp][i] > index)
		{
			nextindex = position[pp][i];
			if (maxchoice[nextindex][c_position + 1] != -1) tempans = (tempans + maxchoice[nextindex][c_position + 1]) % 1000;
			else
			{
				findbest(nextindex, c_position + 1);
				tempans = (tempans + maxchoice[nextindex][c_position + 1]) % 1000;
			}
		}
	maxchoice[index][c_position] = tempans % 1000;
}

int ans;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	length = strlen(slogan);
	scanf("%d\n", &n);
	for (int i = 1; i <= n; ++i)
	{
		ans = 0;
		gets(question);
		ql = strlen(question);
		memset(maxchoice, -1, sizeof(maxchoice));
		for (int j = 0; j <= 27; ++j) position[j].clear();
		for (int j = 0; j < strlen(question); ++j) position[myhash(question[j])].push_back(j);
		int ans = 0;
		for (int j = 0; j < position[myhash(slogan[0])].size(); ++j)
		{	
			int startindex = position[myhash(slogan[0])][j];
			findbest(startindex, 0);
			ans = (ans + (maxchoice[startindex][0] % 1000)) % 1000;
		}
		printf("Case #%d: %04d\n", i, ans);
	}
	return 0;
}