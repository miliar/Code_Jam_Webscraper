#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <fstream>
#include <ctype.h>

#define MIN(x,y) ((x)<(y))?(x):(y)
#define MAX(x,y) ((x)>(y))?(x):(y)

#define rep(i,b) for(int i = 0; i < (b); i++)
#define fo(i,a,b) for(int i = (a); i < (b); i++)
#define fos(i,a,b) for(int i = (a); i < (int)(b).size(); i++)


#include <sstream>
#include <conio.h>

using namespace std;

struct train
{
	int h1;
	int m1;
	int h2;
	int m2;
};

int number[2000];

int T;

vector<int> calc(vector<train> a, vector<train> b)
{
	vector<int> res;
	res.resize(2,0);
	if (a.size() == 0 && b.size() == 0)
	{
		return res;
	} 

	vector<train> nearA;
	vector<train> nearB;

	while(a.size() != 0 || b.size() != 0)
	{
		int h = -1;
		int m = -1;
		bool isA = false;
		int index = -1;

		fos(i, 0, a)
		{
			if (h == -1 || 
				h > a[i].h1 ||
				(h == a[i].h1 && m > a[i].m1))
			{
				isA = true;
				index = i;
				h = a[i].h1;
				m = a[i].m1;
			}
		}

		fos(i, 0, b)
		{
			if (h == -1 || 
				h > b[i].h1 ||
				(h == b[i].h1 && m > b[i].m1))
			{
				isA = false;
				index = i;
				h = b[i].h1;
				m = b[i].m1;
			}			
		}

		train t = isA ? a[index] : b [index];

		if (isA)
		{
			res[0] ++;
			fos(i, 0, nearA)
			{
				if (nearA[i].h2*60 + nearA[i].m2 + T <= t.h1*60 + t.m1)
				{
					res[0] --;
					nearA.erase(nearA.begin() + i);
					break;
				}
			}
		}
		else
		{
			res[1] ++;
			fos(i, 0, nearB)
			{
				if (nearB[i].h2*60 + nearB[i].m2 + T <= t.h1*60 + t.m1)
				{
					res[1] --;
					nearB.erase(nearB.begin() + i);
					break;
				}
			}
		}

		if (isA)
		{
			nearB.push_back(t);
			a.erase(a.begin() + index);
		}
		else
		{
			nearA.push_back(t);
			b.erase(b.begin() + index);
		}
	}

	return res;
}

int main( int argc, char* argv[] )
{
	FILE* in = fopen("B-Large.in", "r");

	int N = 0;
	fscanf(in, "%d\n", &N);
	

	FILE* out = fopen("B-Large.out", "w");

	fo(i, 0, N)
	{
		T = 0;
		fscanf(in, "%d\n", &T);
	
		int A = 0;
		int B = 0;

		fscanf(in, "%d %d\n", &A, &B);
		
		vector<train> a;

		fo(i,0,A)
		{
			train t; 
			fscanf(in, "%d:%d %d:%d\n", &t.h1, &t.m1, &t.h2, &t.m2);
			a.push_back(t);	
		}

		vector<train> b;

		fo(i,0,B)
		{
			train t; 
			fscanf(in, "%d:%d %d:%d\n", &t.h1, &t.m1, &t.h2, &t.m2);
			b.push_back(t);
		}

		vector<int> res = calc(a, b);
		fprintf(out, "Case #%d: %d %d\n", i + 1, res[0], res[1]);	
	}
	fclose (out);

	fclose (in);


	return 0;
}
