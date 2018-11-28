#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int l, d, n, cnt;
char stack[30];
vector<char>word[30];
char dist[5000][30];
bool check(int id)
{
	for(int i=0; i<l; i++)
		if(!binary_search(word[i].begin(), word[i].end(), dist[id][i])) return 0;
	return 1;
}
int main()
{
	char str[1000];
	int i, j, k=0, pos;
	while(cin >> l >> d >> n)
	{
		for(i=0; i<d; i++)
			cin >> dist[i];
		while(n--)
		{
			cin >> str;
			pos = 0;
			for(i=0; i<l; i++)
			{
				word[i].clear();
				if(str[pos]=='(')
				{
					for(j=pos+1; str[j]!=')'; j++)
						word[i].push_back(str[j]);
					pos = j+1;
				}
				else
				{
					word[i].push_back(str[pos]);
					pos++;
				}
				sort(word[i].begin(), word[i].end());
			}
			
			cnt = 0;
			for(i=0; i<d; i++)
				if(check(i)) cnt++;
			printf("Case #%d: %d\n", ++k, cnt);
		}
	}
}
	
