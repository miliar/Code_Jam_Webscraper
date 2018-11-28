#include<cstdio>
#include<vector>
#include<string.h>
#include<algorithm>
using namespace std;
struct struc
{
	int but;
	int k;
};
vector<struc> blue;
vector<struc> or;
char str[1000];
int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t, n, i, j, k;
	char ch;
	scanf("%d", &t);
	for(int tt = 0; tt < t; ++tt)
	{
		scanf("%d", &n);
		blue.clear();
		or.clear();
		struc p;
		gets(str);
		j = 0;
		int len = strlen(str);
		for(i = 0; i < n; ++i)
		{
			for(; j < len && (str[j] != 'B' && str[j] != 'O'); ++j);
			sscanf(str + j, "%c", &ch);
			++j;
			sscanf(str + j, "%d", &k);
			p.but = k;
			p.k = i;
			if(ch == 'B')
				blue.push_back(p);
			else
				or.push_back(p);
		}
		p.but = 0;
		p.k = 1000;
		blue.push_back(p);
		or.push_back(p);
		reverse(blue.begin(), blue.end());
		reverse(or.begin(), or.end());
		
		int res = 0;
		int uk1 = 1, uk2 = 1;
		while(!(blue.size() == 1 && or.size() == 1))
		{
			int dist1 = abs(blue[blue.size() - 1].but - uk1);
			int dist2 = abs(or[or.size() - 1].but - uk2);
			if(blue[blue.size() - 1].k  < or[or.size() - 1].k)
			{
				if(dist1 == 0 && blue.size() != 1)
				{
					++res;
					blue.pop_back();
					if(dist2 > 0 && or.size() != 1)
						uk2 += or[or.size() - 1].but > uk2 ? 1 : -1;
					continue;
				}
				if(dist1 < dist2)
					dist2 = dist1;
				if(blue.size() != 1)
					uk1 += blue[blue.size() - 1].but > uk1 ? dist1 : -dist1;
				if(or.size() != 1)
					uk2 += or[or.size() - 1].but > uk2 ? dist2 : -dist2;
				res += dist1;
			}
			else
			{
				if(dist2 == 0 && or.size() != 1)
				{
					++res;
					or.pop_back();
					if(dist1 > 0 && blue.size() != 1)
						uk1 += blue[blue.size() - 1].but > uk1 ? 1 : -1;
					continue;
				}
				if(dist2 < dist1)
					dist1 = dist2;
				if(blue.size() != 1)
					uk1 += blue[blue.size() - 1].but > uk1 ? dist1 : -dist1;
				if(or.size() != 1)
					uk2 += or[or.size() - 1].but > uk2 ? dist2 : -dist2;
				res += dist2;
			}			
		}
		printf("Case #%d: %d\n", tt+1, res); 
	}
	return 0;
}