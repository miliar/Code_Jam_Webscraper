// GCJ 2010 Round1C P1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include "stdafx.h"
#include <conio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <stdlib.h>
#include <math.h>

#define INPUTF "A-small.in"
#define OUTPUTF "A-small.out"

//#define INPUTF "A-small-practice.in"
//#define OUTPUTF "A-small-practice.out"

#define MAXN 2000

typedef __int64 s64;
typedef __int64 s32;

typedef struct point
{
	s64 x,y;
	point(){}
	point(const s64& _x, const s64 &_y)
		:x(_x)
		,y(_y)
	{
	}
};
typedef struct line
{
	point a;
	point b;
	line(){}
	line(const point& _a, const point &_b)
		:a(_a)
		,b(_b)
	{
	}
};
s64 cross(const point &a,const point &b)
{
	return a.x*b.y-a.y*b.x;
}
s64 max(s64 a, s64 b)
{
	if(a>b)
		return a;
	return b;
}
s64 min(s64 a, s64 b)
{
	if(a<b)
		return a;
	return b;
}
bool intersect(const line& l1, const line& l2)
{
	if(max(l1.a.x,l1.b.x)<min(l2.a.x,l2.b.x))
		return false;
	if(max(l1.a.y,l1.b.y)<min(l2.a.y,l2.b.y))
		return false;
	if(max(l2.a.x,l2.b.x)<min(l1.a.x,l1.b.x))
		return false;
	if(max(l2.a.y,l2.b.y)<min(l1.a.y,l1.b.y))
		return false;
	bool b1 = false;
	bool b2 = false;
	{
		point p1(l1.b.x-l1.a.x,l1.b.y-l1.a.y);
		point p2(l2.a.x-l1.a.x,l2.a.y-l1.a.y);
		point p3(l2.b.x-l1.a.x,l2.b.y-l1.a.y);
		s64 c1 = cross(p1,p2);
		s64 c2 = cross(p1,p3);
		if(c1*c2>0)return false;
		b1 = true;
	}

	{
		point p1(l2.b.x-l2.a.x,l2.b.y-l2.a.y);
		point p2(l1.a.x-l2.a.x,l1.a.y-l2.a.y);
		point p3(l1.b.x-l2.a.x,l1.b.y-l2.a.y);
		s64 c1 = cross(p1,p2);
		s64 c2 = cross(p1,p3);
		if(c1*c2>0)return false;
		b2 = true;
	}
	return b1 && b2;
}
int _tmain(int argc, _TCHAR* argv[])
{
	__int64 T;
	__int64 N;
	//	__int64 res = 0;

	line WiFi[MAXN];

	FILE *Input,*Output;
	Input = fopen(INPUTF, "r");
	Output = fopen(OUTPUTF, "w");

	fscanf(Input,"%lld",&T);

	for (int i=0;i<T;i++)
	{
		s64 res = 0;
		point a(0,0);
		point b(1,0);

		fscanf(Input,"%lld",&N);

		for (int i=0;i<N;i++)
		{
			fscanf(Input,"%lld%lld",&a.y,&b.y);
			WiFi[i] = line(a,b);
		}

		for (int i=0;i<N;i++)
		{
			for (int j=i+1;j<N;j++)
			{
				if(intersect(WiFi[i],WiFi[j]))
					res++;
			}
		}

		fprintf(Output,"Case #%d: %lld\n",i+1,res);
	}

	

	fclose (Input);
	fclose (Output);

	return 0;
}