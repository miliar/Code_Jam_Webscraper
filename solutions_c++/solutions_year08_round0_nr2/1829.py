/*
    Problem	:: B
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

#define min(x,y) (x)<(y)?x:y
#define max(x,y) (x)>(y)?x:y
#define CLR(arr,val) memset((arr), (val), sizeof(arr))

const int MAX = 205;
const int MAXTIME = 24*60;

const int A = 0;
const int B = 1;

struct tt
{
    int dt;
    int at;
    int start_station;
};


class comp_struct
{
    public:
    bool operator () (const tt &a, const tt &b)
    {
	  if(a.dt == b.dt)
	  {
		if(a.at == b.at)
		    return a.start_station < b.start_station;
		return a.at < b.at;
	  }

	  return a.dt < b.dt;
    }
};


struct tt trains[MAX];
int avail[2*MAXTIME+10][2];

int main(void)
{
    // freopen("..//..//Inputs//B2.in", "rt", stdin);
    // freopen("..//..//Inputs//B2.out", "wt", stdout);

    int t, test;
    int aN, bN;
    int i, j, total, T;
    int n1, n2;
    int h1, h2, m1, m2;

    scanf( " %d" ,&test);

    for(t=1; t<=test; t++)
    {
	  scanf( " %d" ,&T);
	  scanf( " %d %d" ,&aN ,&bN);
	  total = 0;

	  for(i=0; i<aN; i++)
	  {
		scanf( "%d:%d %d:%d" ,&h1 ,&m1, &h2, &m2);
		trains[total].dt = h1 * 60 + m1;
		trains[total].at = h2 * 60 + m2 + T;
		trains[total++].start_station = A;
	  }

	  for(i=0; i<bN; i++)
	  {
		scanf( "%d:%d %d:%d" ,&h1 ,&m1, &h2, &m2);
		trains[total].dt = h1 * 60 + m1;
		trains[total].at = h2 * 60 + m2 + T;
		trains[total++].start_station = B;
	  }

	  sort(trains, trains+total, comp_struct());

	  n1 = n2 = 0;

	  CLR(avail, 0);
	  avail[0][A] = avail[0][B] = 0;

	  for(i=0; i<MAXTIME; i++)
	  {
		if(i)
		{
		    avail[i][A] += avail[i-1][A];
		    avail[i][B] += avail[i-1][B];
		}

		for(j=0; j<total; j++)
		{
		    if(trains[j].dt > i)
			  break;

		    if(trains[j].dt == i)
		    {
			  if(trains[j].start_station == A)
			  {
				if(avail[trains[j].dt][A] > 0)
				{
				    avail[trains[j].dt][A]--;
				    avail[trains[j].at][B]++;
				}

				else
				{
				    avail[trains[j].dt][A] = 1;
				    avail[trains[j].dt][A]--;
				    avail[trains[j].at][B]++;
				    n1++;
				}
			  }

			  else // if(trains[j].start_station == B)
			  {
				if(avail[trains[j].dt][B] > 0)
				{
				    avail[trains[j].dt][B]--;
				    avail[trains[j].at][A]++;
				}

				else
				{
				    avail[trains[j].dt][B] = 1;
				    avail[trains[j].dt][B]--;
				    avail[trains[j].at][A]++;
				    n2++;
				}
			  }
		    }

		}

	  }

	  printf( "Case #%d: %d %d\n" ,t ,n1, n2);
    }

    return 0;
}
