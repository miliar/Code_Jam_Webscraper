#include<iostream>
#include<stdio.h>
using namespace std;
#include<vector>
#include<map>
#include<algorithm>
#include<string>

vector<int> v1(200);
vector<int> v2(200);
//FILE * fpr = fopen("test.in", "r");
//FILE * fpw = fopen("test.out", "w");
string read()
{
	char c;
	char temp[200];
	do
	{
		c = getchar();
	}while(!('0' <= c && c <= '9' || 'a' <= c && c <= 'z' ||'A' <= c && c <= 'Z' || c == ' '));
	temp[0] = c;
	int i = 1;
	while(1)
	{
		c = getchar();
		if(!('0' <= c && c <= '9' || 'a' <= c && c <= 'z' ||'A' <= c && c <= 'Z' || c == ' '))
			break;
		temp[i++] = c;
	}
	temp[i] = 0;
	string name(temp);
	return name;
}
int main()
{
	int n;
	int i;
	freopen( "test.in", "r", stdin );
	freopen( "test.out", "w", stdout );

	scanf("%d", &n);
	int s, q;
	map<string, int> Map;
	char temp[200];
	for(i = 0; i < n; i++)
	{
		Map.clear();
		scanf("%d", &s);
		char c;
		int j;
		for(j = 0; j < s; j++)
		{
			v1[j] = 0;
			string name = read();
			Map[name] = j;
		}
		scanf("%d", &q);
		string search_name = read();
		int num = Map[search_name];
		for(j = 0; j < s; j++)
		{
			v1[j] = 0;
			if(j == num)
				v1[j] = -1;
		}

		for(j = 1; j < q; j++)
		{
			string search_name = read();
			int num = Map[search_name];
			int k;
			for(k = 0; k < s; k++)
			{
				int r;
				if(k == num)
				{
					v2[k] = -1;
					continue;
				}
				int mn = 0x7fffffff;
				for(r = 0; r < s; r++)
				{
					if(v1[r] != -1)
					{
						int val;
						if(k == r)
							val = v1[r];
						else
							val = v1[r] + 1;
						if(mn > val)
							mn = val;
					}
				}
				v2[k] = mn;
			}
			v1.swap(v2);
		}
		int mn = 0x7ffffff;
		for(j = 0; j < s; j++)
			if(mn > v1[j] && v1[j] != -1)
				mn = v1[j];
		printf("Case #%d: %d\n", i + 1, mn);
	}
}