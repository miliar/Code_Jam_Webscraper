#include <stdio.h>
#include <set>

using namespace std;

#define V 0x100000000ULL
#define Z(a,b) (a*0x100000000ULL+b)
#define X(a) (a/0x100000000ULL)
#define Y(a) (a%0x100000000ULL)

int t;

int main()
{
	scanf(" %d", &t);
	for(int cs=1; cs<=t; cs++)
	{
		set <unsigned long long> A;
		set <unsigned long long> B;
		int r, res=0;
		scanf(" %d", &r);
		for(int i=0; i<r; i++)
		{
			int x1, x2, y1, y2;
			scanf (" %d %d %d %d", &x1, &y1, &x2, &y2);
			for(int x=x1; x<=x2; x++)
				for(int y=y1; y<=y2; y++)
					A.insert(Z(x,y));
		}
		while(!A.empty())
		{
			res++;
			B.clear();
			for(set<unsigned long long>::iterator p=A.begin(); p!=A.end(); p++)
			{
				if (A.find(*p-V+1)!=A.end()) B.insert(*p+1);
				if ((A.find(*p-1)!=A.end()) || (A.find(*p-V)!=A.end())) B.insert(*p);
			}
			A=B;
		}
		printf("Case #%d: %d\n", cs, res);
	}
	return 0;
}
