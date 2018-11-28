/*
    Problem	:: A 
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
#define CLR(arr,val) memset((arr), (val) sizeof(arr))

const int MAXLEN = 102;
const int MAXS = 102;
const int MAXQ = 1002;
const int INF = 10005;

struct server_info
{
    char names[MAXLEN];

    bool operator <(const server_info &obj) const
    {
	  if(strcmp(names, obj.names) < 0)
		return true;
	  return false;
    }
};

server_info S[MAXS];

int store[MAXQ][MAXS];


class comp_serverInfo
{
	public:
	bool operator() (const server_info &a, const server_info &b)
	{
	    return (a < b);
	}
};



void init(int nS)
{
    int s;

    for(s=0; s<nS; s++)
	  store[0][s] = INF;

    return;
}


int compute(int nS)
{
    int nQ;
    int s, q, ind, min1, prev;
    struct server_info str, *p;
    int res = 0;

    init(nS);

    scanf( " %d " ,&nQ);

    if(nQ == 0)
	  return res;

    prev = -1;

    for(q=0; q<nQ; q++)
    {
	  gets(str.names);

	  if( binary_search(S, S+nS, str) == true )
	  {
		p = lower_bound(S, S+nS, str);
		ind = p - S;
	  }

	  else
		ind = -1;

	  min1 = prev;
	  prev = INF;

	  if(ind == -1)
	  {
		for(s=0; s<nS; s++)
		{
		    if(store[q-1][s] == -1)
		    {
			  store[q][s] = min1 + 1;
			  prev = min(prev, min1 + 1);
		    }
		    else
		    {
			  store[q][s] = min1;
			  prev = min(prev, min1);
		    }
		}
	  }

	  else
	  {
		for(s=0; s<nS; s++)
		{
		    if(s == ind)
		    {
			  store[q][s] = -1;
				continue;
		    }

		    if(store[q-1][s] == -1)
		    {
			  store[q][s] = min1 + 1;
			  prev = min(prev, min1 + 1);
		    }
		    else
		    {
			  if(store[q-1][s] == min1)
			  {
				store[q][s] = min1;
				prev = min(prev, min1);
			  }
			  else
			  {
				store[q][s] = min(min1+1, store[q-1][s]);
				prev = min(prev, store[q][s]);
			  }
		    }
		}
	  }

	  min1 = prev;
    }

    res = INF;

    q = nQ-1;

    for(s=0; s<nS; s++)
    {
	  if(store[q][s] != -1)
	  {
		if(store[q][s] < res)
		    res = store[q][s];
	  }
    }

    return res;
}



int main(void)
{
    // freopen("..//..//Inputs//A1.in", "rt", stdin);
    // freopen("..//..//Inputs//A1.out", "wt", stdout);

    int t, test;
    int s, nS;

    scanf( " %d" ,&test);

    for(t=1; t<=test; t++)
    {
	  scanf( " %d " ,&nS);

	  for(s=0; s<nS; s++)
		gets( S[s].names );

	  sort(S, S+nS, comp_serverInfo());
	  
	  printf( "Case #%d: %d\n" ,t ,compute(nS));
    }

    return 0;
}

