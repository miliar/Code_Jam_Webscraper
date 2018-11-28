#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <climits>
#include <algorithm>
#include <iostream>
#include <fstream>

using namespace std;
int tree[2080], depth, len;
int cache[2080][15];
int cost(int node, int modifier)
{
	if(len<=node)
		if(tree[node]+modifier<depth)
			return -3;
		else
			return 0;
	if(cache[node][modifier]!=-1)
		return cache[node][modifier];
	int r1=cost(node*2+1, modifier), r2=cost(node*2+2, modifier);
	int r3=tree[node], r4=cost(node*2+1, modifier+1), r5=cost(node*2+2, modifier+1);
	cache[node][modifier]=-3;
	if(r1!=-3 && r2!=-3)
		cache[node][modifier]=r1+r2;
	if(r3!=-3 && r4!=-3 && r5!=-3)
		if(cache[node][modifier]==-3)	cache[node][modifier]=r3+r4+r5;
		else
			cache[node][modifier]=min(r1+r2, r3+r4+r5);
	
	return cache[node][modifier];
	//Caching should hopefully work.
}
int main()
{
	int T;
	FILE *in=fopen("cupin.txt", "r");
	FILE *out=fopen("cupout.txt", "w");
	fscanf(in, "%d", &T);
	for(int t=0; t<T; t++)
	{
		for(int i=0; i<2080; i++)
			for(int j=0; j<15; j++)
				cache[i][j]=-1;
		for(int i=0; i<2080; i++)
			tree[i]=-1;
		fscanf(in, "%d", &depth);
		//len is (2^depth); this is the index of the first leaf
		len=1;
		for(int i=0; i<depth; i++)
			len*=2;
		len--;	//because we're 0-indexed, and there are 2^depth-1 items before it, so it's item 2^depth-1
		//*2+1 and *2+2 are the issues
		//So, 0->(1, 2)
		//So, 1->0 is given by -1, /2
		//and 2->0 is also given by -1, /2
		
		for(int i=0; i<len+1; i++)
			fscanf(in, "%d", &(tree[i+len]));
		//Now I'm given the rest of the tree in abysmal format. Let's see if I can't make this work...
		int l=len;
		while(l!=0)
		{
			int tmp=l;
			l--;
			l/=2;
			for(int i=l; i<tmp; i++)
				fscanf(in, "%d", &(tree[i]));
		}
		fprintf(out, "Case #%d: %d\n", t+1, cost(0, 0));
	}
	
	return 0;
}