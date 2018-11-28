#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

class term
{
public:
	int value;
	int index;

	bool operator<(term& rhs)
	{
		return value < rhs.value;
	}
};

int _tmain(int argc, _TCHAR* argv[])
{

	FILE *fin, *fout;
	int T;
	fin = fopen("small.in","r");
	fout = fopen("small.out","w");

	fscanf(fin,"%d\n",&T);
	for(int j = 0; j < T; j++){
		int l, n, c;
		unsigned int time;
		fscanf(fin, "%d %u %d %d", &l, &time, &n, &c);
		vector<int> dis;
		unsigned int csum = 0;
		for(int i = 0; i < c; i++)
		{
			int a;
			fscanf(fin, "%d", &a);
			csum += a;
			dis.push_back(a);
		}

		unsigned int length  = time/2;
		unsigned int edge = length%csum;
		int circle = length/csum;

		unsigned int full = (n/c)*csum;
		for(int i = 0; i < n%c; i++)
		{
			full += dis[i];
		}

		int i = 0;
		printf("edge = %u, csum = %u, length = %u, time = %u\n",edge, csum, length, time);
		while(edge > edge-dis[i])
		{
			edge -= dis[i];
			i++;
		}

		unsigned int back = full - circle*csum - edge;
		unsigned int backCircle = back/csum;

		vector<term> terms;
		for(int k = 0; k <dis.size(); k++)
		{
			term aTerm;
			aTerm.value = dis[k];
			aTerm.index = k;
			terms.push_back(aTerm);
		}

		sort(terms.begin(), terms.end());
		int edgeSpeedUp = 0;
		for(int k = 0; k <= i; k++)
		{
			edgeSpeedUp += dis[k];
		}
		edgeSpeedUp -= length%csum;

		int betterIndex = -1;
		for(int k = terms.size() - 1; k >= 0; k--)
		{
			if(terms[k].value < edgeSpeedUp)
			{
				betterIndex = k;
				break;
			}
		}

		unsigned int speedUp = 0;
		for(int k = terms.size() - 1; k > betterIndex; k--)
		{
			if(l == 0)break;
			int count = 0;
			if(terms[k].index > i)
			{
				count = backCircle+1;
			}else{
				count = backCircle;
			}
			if(l < count)count = l;
			l -= count;
			speedUp += count*terms[k].value;
		}

		//use edge
		if(l > 0)
		{
			l--;
			speedUp += edgeSpeedUp;
		}

		for(int k = betterIndex; k > -1; k--)
		{
			if(l == 0)break;
			int count = 0;
			if(terms[k].index > i)
			{
				count = backCircle+1;
			}else{
				count = backCircle;
			}
			if(l < count)count = l;
			l -= count;
			speedUp += count*terms[k].value; 
		}

		printf("full = %u, speedUp = %u, edgeSpeedUp = %d\n", full, speedUp, edgeSpeedUp);
		printf("length = %u, csum = %u\n", length, csum);
		printf("===\n");

		fprintf(fout, "Case #%d: %u\n", j+1, full*2 - speedUp);
	}

	return 0;
}