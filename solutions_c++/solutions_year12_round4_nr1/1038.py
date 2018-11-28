#include <iostream>
#include <stack>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <string>
using namespace std;

#define A first
#define B second

bool visit[20000];

class comp
{
	public:
	comp (){};
	bool operator() (const pair<int, int>& a, const pair<int, int>& b) const
	{
		if (a.A != b.A)
			return a.A > b.A;
		return a.B > b.B;
	}
};

priority_queue<pair<int, int>, vector<pair<int, int> >, comp> Q;

int main()
{
	int i, j, k, D, N, T, d;
	pair<int, int> vine[20000]; //<dist, length>
	pair<int, int> temp;
	scanf("%d", &T);
	for (int t=1; t<=T; ++t)
	{
		scanf("%d", &N);
		for (i=0; i<N; ++i)
		{
			scanf("%d %d", &vine[i].A, &vine[i].B);
			visit[i] = false;
		}
		scanf("%d", &D);
		Q.push(make_pair(0, 0)); //pos, n
		j = 0;
		//visit.clear();
		visit[0] = true;
		while (!Q.empty())
		{
			temp = Q.top();
			Q.pop();
			d = vine[temp.B].A-temp.A;
			//cout << temp.A << " " << temp.B << " " << d << endl;
			if (vine[temp.B].A + d >= D)
			{
				//cout << temp.A << " " << vine[temp.B].A << " " << d << endl;
				printf("Case #%d: YES\n", t);
				j = 1;
				while (!Q.empty())
					Q.pop();
			}
			else
			{
				for (i=temp.B+1; i<N; ++i)
					if (vine[temp.B].A+d >= vine[i].A)
					{
						k=max(vine[temp.B].A, vine[i].A-vine[i].B);
						if (!visit[i])
						{
							visit[i] = true;
							Q.push(make_pair(k, i));
						}
					}
					else
						break;
			}
		}
		if (!j)
		{
			printf("Case #%d: NO\n", t);
		}
	}
	return 0;
}
