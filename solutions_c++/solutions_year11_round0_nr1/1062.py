#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <vector>
#include <list>
#include <algorithm>

using namespace std;

int sign(int a)
{
	if(a < 0)
		return -1;
	else if (a > 0)
		return 1;
	else return 0;
}

int main(int argc, char **argv)
{
	int T;
	freopen("A-large.in", "rb", stdin);
	freopen("A-large.out", "wb", stdout);

	scanf("%d", &T);

	for(int t = 0; t < T; t++)
	{
		vector< pair<int, int> > O;
		vector< pair<int, int> > B;

		int N;
		scanf("%d", &N);

		for(int n = 0; n < N; n++)
		{
			char c[2];
			int button;

			scanf("%s %d", c, &button);

			switch(c[0])
			{
			case 'O':
				O.push_back(pair<int,int>(button, B.size() - 1));
				break;
			case 'B':
				B.push_back(pair<int,int>(button, O.size() - 1));
				break;
			}
		}

		int Optr = 0, Bptr = 0;
		int Opos = 1, Bpos = 1;

		int time = 0;
		int n = 0;

		while(n < N)
		{
			int pushed = 0;
			if(Optr < O.size())
			{
				if(Opos != O[Optr].first)
				{
					Opos += sign(O[Optr].first - Opos);
				}
				else if(O[Optr].second < Bptr)
				{
					Optr++;
					pushed = 1;
					n++;
				}
			}

			if(Bptr < B.size())
			{
				if(Bpos != B[Bptr].first)
				{
					Bpos += sign(B[Bptr].first - Bpos);
				}
				else if(!pushed && B[Bptr].second < Optr)
				{
					Bptr++;
					n++;
				}
			}

			time++;
		}
		
		printf("Case #%d: %d\n", t + 1, time);
	}

	return 0;
}