#include <cstdio>
#include <cstring>
#include <utility>
#include <algorithm>
using namespace std;
const int SIZE = 210;
const int INF = 2100000000;

int 	cas, T = 0;

int 	blen, glen;
int 	boy[SIZE], girl[SIZE];
int 	lab_boy[SIZE], lab_girl[SIZE];
int 	edg[SIZE][SIZE];

int 	a_size, b_size;
int 	lag;
int 	send[SIZE], receive[SIZE];


int DFS(int v)
{
    lab_boy[v] = 1;
    for(int i=0; i < glen; i++)
    	if(edg[v][i] && lab_girl[i] < 0)	 // 有从v->i的边 &&当前轮 DFS中i没有被访问
		{                                 
  			lab_girl[i] = 1;
 	   		if(girl[i] < 0 || DFS(girl[i]))
			{
   				boy[v] = i;
   				girl[i] = v;
     	       	return 1;
			}
   	 	}
    return 0;
}
void MaxMatch()
{
	memset(boy, 0xff, sizeof(boy));
 	memset(girl, 0xff, sizeof(girl));
 	
    for(int i=0; i < blen; i++)
    	if(boy[i] < 0)
		{
	        memset(lab_boy, 0xff, sizeof(lab_boy));
    	    memset(lab_girl, 0xff, sizeof(lab_girl));
    	    DFS(i);
  		}
}


int main()
{
	int 	i, j, k;
	
	freopen("B-large.in", "r", stdin);
	freopen("B_large_out.txt", "w", stdout);
	
	for (scanf("%d", &cas); cas; cas--)
	{
		scanf("%d %d %d", &lag, &a_size, &b_size);
		for (i=0; i<a_size; i++)
		{
			int 	h, m;
			scanf("%d:%d", &h, &m);
			send[i] = h * 60 + m;
			scanf("%d:%d", &h, &m);
			receive[i] = h * 60 + m;
		}
		for (i=0; i<b_size; i++)
		{
			int 	h, m;
			scanf("%d:%d", &h, &m);
			send[a_size + i] = h * 60 + m;
			scanf("%d:%d", &h, &m);
			receive[a_size + i] = h * 60 + m;
		}
		
		blen = glen = a_size + b_size;	
		memset(edg, 0, sizeof(edg));
		for (i=0; i<a_size; i++)
			for (j=a_size; j<blen; j++)
			{
				if (receive[i] + lag <= send[j])
				{
					edg[i][j] = 1;
				//	printf("match %d %d\n", i, j);
				}
			}
		for (i=a_size; i<blen; i++)
			for (j=0; j<a_size; j++)
			{
				if (receive[i] + lag <= send[j])
				{
					edg[i][j] = 1;
					//printf("match %d %d\n", i, j);
				}
			}
		
		MaxMatch();
		
		int 	ra, rb;
		ra = rb = 0;
		for (i=0; i<blen; i++)
			if (girl[i] < 0)
			{
				if (i < a_size)
					ra++;
				else
					rb++;
			}
		printf("Case #%d: %d %d\n", ++T, ra, rb);
		
	}
	return 0;
}
