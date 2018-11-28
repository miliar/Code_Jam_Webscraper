/*
    Problem	::  A
*/

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>

using namespace std;

#define INF = 0x7F7F7F7F;
#define min(x,y) (x)<(y)?(x):(y)
#define max(x,y) (x)>(y)?(x):(y)
#define CLR(arr,val) memset((arr), (val), sizeof(arr))

class comp_asc
{
	public:
	bool operator () (const int a, const int b)
	{
		return a < b;	
	}
};


class comp_desc
{
	public:
	bool operator () (const int a, const int b)
	{
		return a > b;	
	}
};


const int MAX = 900;
int v1[MAX];
int v2[MAX];

int main(void)
{
    // freopen("..//..//Inputs//A1.in", "rt", stdin);
    // freopen("..//..//Inputs//A1.out", "wt", stdout);

    int t, test;
    int N, res;
    int i, s1, e1, s2, e2;

    scanf( " %d" ,&test);

    for(t=1; t<=test; t++)
    {
	  scanf( " %d" ,&N);

	  for(i=0; i<N; i++)
		scanf(" %d" ,&v1[i]);

	  for(i=0; i<N; i++)
		scanf(" %d" ,&v2[i]);

	  sort(v1, v1+N);
	  sort(v2, v2+N);

	  s1 = s2 = 0;
	  e1 = e2 = N-1;

	  res = 0;

	  while(s1 <= e1)
	  {
		if(v1[s1] < v2[s2])
		{
		    res += v1[s1] * v2[e2];
		    e2--;
		    s1++;
		}

		else if(v1[s1] > v2[s2])
		{
		    res += v2[s2] * v1[e1];
		    e1--;
		    s2++;
		}

		else 	// if(v1[s1] == v2[s2])
		{
		    if(v1[e1] > v2[e2])
		    {
			  res += v1[s1] * v2[e2];
			  e2--;
			  s1++;
		    }

		    else // if(v1[e1] <= v2[e2])
		    {
			  res += v2[s2] * v1[e1];
			  e1--;
			  s2++;
		    }
		}

	  }

	  printf( "Case #%d: %d\n" ,t ,res);
    }




    return 0;
}
