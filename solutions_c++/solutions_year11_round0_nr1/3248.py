#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <cctype>
#include <set>
#include <iostream>
#include <sstream>
#include <ctime>

using namespace std;

class Item
{
public:
	char robot;
	int button;
	Item(char r, int b)	:	robot(r), button(b)	{}
};

vector<Item> seq;

char buf[128];

int T, N;
int main()
{
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		seq.clear();
		scanf("%d", &N);
		for(int i = 0; i < N; i++)
		{
			int nb;
			scanf("%s", buf);
			scanf("%d", &nb);
			seq.push_back(Item(buf[0], nb));
		}
		int ans = 0;
		int posO = 1, posB = 1;
		int timeO = 0, timeB = 0;
		for(int i = 0; i < N; i++)
		{
			if(seq[i].robot == 'O')
			{
				int d = abs(posO - seq[i].button);
				if(timeO >= d)
				{
					timeO = 0;
					timeB++;
					ans++;
					posO = seq[i].button;
				}
				else
				{
					ans += d - timeO + 1;
					timeB += d - timeO + 1;
					timeO = 0;
					posO = seq[i].button;
				}
			}
			else
			{
				int d = abs(posB - seq[i].button);
				if(timeB >= d)
				{
					timeB = 0;
					timeO++;
					ans++;
					posB = seq[i].button;
				}
				else
				{
					ans += d - timeB + 1;
					timeO += d - timeB + 1;
					timeB = 0;
					posB = seq[i].button;
				}
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}