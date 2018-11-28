#include <stdio.h>
#include <stdlib.h>

#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>

#include <math.h>

#define PI 3.14159

using namespace std;
struct point
{
	long long int x,y;
	point(){}
	point(long long int a, long long int b)
	{
		x=a;y=b;
	}
	/*
	point(point &a)
	{
		x=a.x;
		y=a.y;
	}*/

};
int main()
{
	long long int i,j,k,l,m,n;
	int testId, nTests;

	scanf("%d", &nTests);
	for(testId=1;testId<=nTests;testId++)
	{
		long long int n, A, B, C, D, x0, y0, M;
		vector<point> v;
		point p;
		//XXX  -- Read input --  XXX

		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		long long int X = x0, Y = y0;
		p.x=X;p.y=Y; v.push_back(p);
		for(i = 1; i<n; i++)
		{
  			X = (A * X + B) % M;
  			Y = (C * Y + D) % M;
			p.x=X;p.y=Y; v.push_back(p);
		}

		//XXX  -- Process input --  XXX
		long long int tot=0;
		vector<point>::iterator iter1, iter2, iter3;
		for(iter1=v.begin(); iter1!=v.end(); iter1++)
		{
			for(iter2=v.begin(); iter2!=v.end(); iter2++)
			{
				if (iter1 == iter2)
					continue;
				for(iter3=v.begin(); iter3!=v.end(); iter3++)
				{
					if (iter1 == iter3 || iter2 == iter3)
						continue;
					//cout << "(" << iter1->x <<"," << iter1->y<<") ";
					//cout << "(" << iter2->x <<"," << iter2->y<<") ";
					//cout << "(" << iter3->x <<"," << iter3->y<<") " << endl;
					if ( ( (iter1->x + iter2->x + iter3->x)%3 == 0) &&
					     ( (iter1->y + iter2->y + iter3->y)%3 == 0))
				    {
						tot++;
				    }
				}
			}
		}

		if(tot%6!=0)
		{
			printf("ERROR... tot %d\n", tot);
		}

		//XXX  -- Print output --  XXX
		printf("Case #%d: %d\n",testId, tot/6);

	}

	return 0;
}
