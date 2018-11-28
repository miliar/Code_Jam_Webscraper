#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <math.h>

class Location
{
	public:
		__int64 x;
		__int64 y;
		
		Location(__int64 x, __int64 y)
		{
			this->x = x;
			this->y = y;
		}
};

long double getArea(__int64 xa, __int64 ya, __int64 xb, __int64 yb, __int64 xc, __int64 yc)
{
	long double s = 0.5 * abs(xa * yc - xa * yb + xb * ya - xb * yc + xc * yb - xc * ya);
	
	return s;
}

double dist(Location* l1, Location* l2)
{
	return sqrt( (l1->x - l2->x)*(l1->x - l2->x) + (l1->y - l2->y)*(l1->y - l2->y) );
}

class Result
{
	public:
	Location* li;
	Location* lj;
	Location* lk;
	
	Result(Location* li, Location* lj, Location* lk)
	{
		this->li = li;
		this->lj = lj;
		this->lk = lk;
	}
};
Result** results;
long resultCount;

int isTriangleOk(Location** locations, __int64 n, __int64 i, __int64 j, __int64 k)
{
	Location* li = locations[i];
	Location* lj = locations[j];
	Location* lk = locations[k];
	
	if(li->x == lj->x && li->y == lj->y)
		return 0;
		
	if(li->x == lk->x && li->y == lk->y)
		return 0;		
	
	if(lj->x == lk->x && lj->y == lk->y)
		return 0;
/*	
	long double lij = dist(li, lj);
	long double lik = dist(li, lk);
	long double ljk = dist(lj, lk);
	
	if(lij + lik < ljk || lij + ljk < lik || lik + ljk < lij)
		return 0;
	*/
	if((li->x + lj->x + lk->x) % 3)
		return 0;
		
	if((li->y + lj->y + lk->y) % 3)
		return 0;

/*
for(long i = 0 ; i < resultCount; i++)
{
	if(
		(li == results[i]->li && lj == results[i]->lj && lk == results[i]->lk) ||
		(li == results[i]->li && lk == results[i]->lj && lj == results[i]->lk) ||
		(lj == results[i]->li && li == results[i]->lj && lk == results[i]->lk) ||
		(lj == results[i]->li && lk == results[i]->lj && li == results[i]->lk) ||
		(lk == results[i]->li && li == results[i]->lj && lj == results[i]->lk) ||
		(lk == results[i]->li && lj == results[i]->lj && li == results[i]->lk)
		)
		return 0;
}		

results[resultCount++] = new Result(li, lj, lk);	*/
return 1;
	__int64 xCenter =  (li->x + lj->x + lk->x) / 3;
	__int64 yCenter = (li->y + lj->y + lk->y) / 3;
	//printf("\nCenter = %d, %d", xCenter, yCenter);
	for(__int64 t = 0; t < n; t++)
		if(locations[t]->x == xCenter && locations[t]->y == yCenter)
			return 1;
	
	return 0;
}

int getTriangleCount(Location** locations, __int64 n)
{
	/*
	for(int i = 0; i < n; i++)
	{
		printf("\n### %d, %d", locations[i]->x, locations[i]->y);
	}
	*/
	__int64 triangleCount = 0;
	
	for(long i = 0; i < n; i++)
		for(long j = i; j < n; j++)
			for(long k = j; k < n; k++)
			{
				if(i == j || i == k || j == k)
					continue;
					
				if(isTriangleOk(locations, n, i, j, k))
				{
					//printf("\n\nT: (%d, %d) (%d, %d) (%d, %d)", locations[i]->x, locations[i]->y, locations[j]->x, locations[j]->y, locations[k]->x, locations[k]->y);
					triangleCount++;
				}
			}
			
	return triangleCount;
}

__int64 solveTestCase(FILE* fin)
{resultCount =0;
	__int64 n, a, b, c, d, x0, y0, m;
	
	fscanf(fin, "%I64d", &n);
	fscanf(fin, "%I64d", &a);
	fscanf(fin, "%I64d", &b);
	fscanf(fin, "%I64d", &c);
	fscanf(fin, "%I64d", &d);
	fscanf(fin, "%I64d", &x0);
	fscanf(fin, "%I64d", &y0);
	fscanf(fin, "%I64d", &m);
	
	Location** locations = (Location**)malloc(sizeof(Location*) * n);
	
	__int64 x = x0;
	__int64 y = y0;
	
	locations[0] = new Location(x, y);

	for(long i = 1; i <= n - 1; i++)
	{
  		x = (a * x + b) % m;
  		y = (c * y + d) % m;
  		
		locations[i] = new Location(x, y);
	}

	__int64 result = getTriangleCount(locations, n);

	for(long i = 0; i < n; i++)
		delete locations[i];
	
	free(locations);
	
	return result;
}

int main()
{
	FILE* fin = fopen("a.in.txt", "rb");
	FILE* fout = fopen("a.out.txt", "wb");
	results = (Result**)malloc(0xFFFFF);
	__int64 testCaseCount;
	
	fscanf(fin, "%I64d", &testCaseCount);
	
	for(__int64 i = 0; i < testCaseCount; i++)
	{
		__int64 result = solveTestCase(fin);
		printf("Case #%I64d: %I64d\n", i + 1, result);
		fprintf(fout, "Case #%I64d: %I64d\n", i + 1, result);
	}
	
	printf("press any key");
	getch();
	
	return 0;
}
