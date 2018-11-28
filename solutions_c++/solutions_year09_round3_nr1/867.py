#include <cstdio>
#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>
#include <cmath>
using namespace std;

typedef struct node
{
	int index;
	int value;
} node;

int cmp(const void *a, const void *b)
{
	return ((node *)b)->value - ((node *)a)->value;
}
int main()
{
	freopen("A-large.in", "r", stdin);
	ofstream out("out1.txt");
	int T;
	int count = 1;
	scanf("%d", &T);
	while(T--)
	{
		__int64 result = 0;
		char s[62] = {0};
		char ss[62] = {0};
		node flag[36] = {0};
		for(int i=0; i<36; i++)
		{
			flag[i].value = -1;
			flag[i].index = i;
		}
		scanf("%s", ss);
		int ll =strlen(ss);
		if(ll == 1)
		{
			out << "Case #" << count << ": " << "1" << endl;
			count ++;
			continue;
		}

		for(int i=0; i<ll; i++)
		{
			s[i] = ss[ll-1-i];
		}
		
		int maxi = 0;
		int len = strlen(s);
		for(int i=0; i<len; i++)
		{
			if('0'<= s[i] && s[i] <= '9')
			{
				s[i] = s[i] - '0';
			}
			if('a' <= s[i] && s[i] <= 'z')
			{
				s[i] = s[i] - 'a' + 10;
			}
			if(flag[s[i]].value == -1)
			{
				maxi ++;
			}
			if(i > flag[s[i]].value)
			{
				flag[s[i]].value = i;
			}
		}
		if(maxi == 1)
		{
			for(int i=0; i<len; i++)
			{
				int tt = 1<<i;
				result += tt;
			}
			out << "Case #" << count << ": " << result << endl;
			count ++;
			continue;
		}


		qsort(flag, 36, sizeof(node), cmp);
		int tmp[36] = {0};
		tmp[flag[0].index] = 1;
		tmp[flag[1].index] = 0;
		for(int i=2; i<maxi; i++)
		{
			tmp[flag[i].index] = i;
		}

		__int64 mul = 1;
		for(int i=0; i<len; i++)
		{
			result += tmp[s[i]]*mul;
			mul *= maxi;
		}
		out << "Case #" << count << ": " << result << endl;
		count ++;
	}
	return 0;
}
