#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

struct train
{
	int pos;
	int a, b;
};
bool operator<(const train& a, const train& b)
{
	return a.a < b.a;
}

int tc, ntc;
int k, na, nb;
int ntr;
train tr[500];

multiset<int> xA, xB;

int main()
{
	scanf("%d",&ntc);
	int i;
	int h1,m1,h2,m2;
	int resA, resB;
	for (tc=1; tc<=ntc; tc++)
	{
		scanf("%d",&k);
		scanf("%d %d",&na, &nb);
		
		ntr = 0;
		for (i=0; i<na; i++)
		{
			scanf("%d:%d %d:%d\n",&h1,&m1,&h2,&m2);
			tr[ntr].a = h1*60 + m1;
			tr[ntr].b = h2*60 + m2;
			tr[ntr].pos = 0;
			ntr++;
		}
		
		for (i=0; i<nb; i++)
		{
			scanf("%d:%d %d:%d\n",&h1,&m1,&h2,&m2);
			tr[ntr].a = h1*60 + m1;
			tr[ntr].b = h2*60 + m2;
			tr[ntr].pos = 1;
			ntr++;
		}
		
		sort(tr, tr+ntr);
		resA = resB = 0;
		
		xA.clear();
		xB.clear();
		
		multiset<int> :: iterator it;
		for (i=0; i<ntr; i++)
		{
			if (tr[i].pos == 0) // A to B
			{
				it = xA.upper_bound( tr[i].a - k );
				if (it == xA.begin()) resA++;
				else
				{
					it--;
					xA.erase(it);
				}
				
				xB.insert( tr[i].b );
			}
			else // B to A
			{
				it = xB.upper_bound( tr[i].a - k );
				if (it == xB.begin()) resB++;
				else
				{
					it--;
					xB.erase(it);
				}
				xA.insert( tr[i].b );
			}
		}		
		
		printf("Case #%d: %d %d\n",tc, resA, resB);
	}
}