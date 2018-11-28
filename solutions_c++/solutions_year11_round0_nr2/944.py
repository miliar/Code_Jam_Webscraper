#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <deque>
#include <string>
#include <cmath>
#include <set>
#include <queue>
#include <map>
#define eps 1e-11
using namespace std;
int c, d, n, t; vector<vector<int> > cmb, cl; char ch; char s[110]; vector<int> q; deque<int> x;
int main()
{
	scanf("%d", &t);
	for (int T=0; T<t; T++)
	{
		cmb.assign(27, vector<int>(27, 0)); cl.assign(27, vector<int>(27, 0)); q.assign(27, 0); x.clear();
		scanf("%d", &c);
		for (int i=0; i<c; i++)
		{
			scanf(" %s", s);
			for (int j=0; j<3; j++) s[j]=toupper(s[j])-'A'+1;
			cmb[s[0]][s[1]]=cmb[s[1]][s[0]]=s[2];
		}
		scanf("%d", &d);
		for (int i=0; i<d; i++)
		{
			scanf(" %s", s);
			for (int j=0; j<2; j++) s[j]=toupper(s[j])-'A'+1;
			cl[s[0]][s[1]]=cl[s[1]][s[0]]=1;
		}
		scanf("%d", &n); scanf(" %s", s);
		for (int i=0; i<n; i++)
		{
			s[i]=toupper(s[i])-'A'+1;
			if (x.empty()) x.push_back(s[i]), q[s[i]]++;
			else
			{
				if (ch=cmb[x.back()][s[i]])
				{
					q[x.back()]--; x.pop_back(); q[ch]++; x.push_back(ch);
				}
				else
				{
					for (int j=1; j<27; j++)
						if (q[j] && cl[j][s[i]])
						{
							q.assign(27, 0); x.clear();
							break;
						}
					if (!x.empty()) x.push_back(s[i]), q[s[i]]++;
				}
				
			}
		}
		printf("Case #%d: [", T+1);
		if (!x.empty()) printf("%c", x.front()+'A'-1), x.pop_front();
		while (!x.empty()) printf(", %c", x.front()+'A'-1), x.pop_front();
		printf("]\n");
	}
	return 0;
}
