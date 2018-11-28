#include <string>
#include <vector>
#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

char comb[300][300];
int opp[300][300];

int main()
{
	int i,j,k;
	int T, ca;
	cin >> T;
	for(ca=1; ca<=T; ca++)
	{
		memset(comb, 0, sizeof(comb));
		memset(opp, 0, sizeof(opp));
		int C;
		cin >> C;
		for(i=0; i<C; i++)
		{
			string s;
			cin >> s;
			comb[s[0]][s[1]] = comb[s[1]][s[0]] = s[2];
		}
		int D;
		cin >> D;
		for(i=0; i<D; i++)
		{
			string s;
			cin >> s;
			opp[s[0]][s[1]] = opp[s[1]][s[0]] = 1;
		}
		vector<char> list;
		int N;
		cin >> N;
		string invoke;
		cin >> invoke;
		for(i=0; i<N; i++)
		{
			list.push_back(invoke[i]);
			while(list.size() > 1)
			{
				int s = list.size();
				char r;
				if ((r = comb[list[s-1]][list[s-2]]) != 0)
				{
					list.pop_back();
					list.pop_back();
					list.push_back(r);
				}
				else
				{
					int f = 0;
					for(j=0; j<list.size(); j++) for(k=j+1; k<list.size(); k++)
					{
						if (opp[list[j]][list[k]])
						{
							f = 1;
							break;
						}
						if (f) break;
					}
					if (f)
						list.clear();
					break;
				}
			}
		}
		printf("Case #%d: [", ca);
		for(i=0; i<list.size(); i++)
		{
			if (i > 0) printf(", ");
			printf("%c", list[i]);
		}
		printf("]\n");
	}
}
