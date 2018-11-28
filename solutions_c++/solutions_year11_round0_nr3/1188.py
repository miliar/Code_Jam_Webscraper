// 2011_1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int wrong_sum(int a, int b)
{
	return (a+b)-2*(a&b);
}

int correct_sum(int a, int b)
{
	return (a+b)-2*(a&b);
}

void add_bits(vector<int>& bits, int b)
{
	int index = 0; 
	while(b)
	{
		if(b&1) bits[index]++;
		index++;
		b = b/2;
	}
}

int targed(vector<int> bits)
{
	int result = 0; 
	int cur = 1;
	for(int i = 0; i<bits.size(); i++)
	{
		if((bits[i]/2)&1) result += cur;
		cur *= 2;
	}
	return result;
}

int _tmain(int argc, _TCHAR* argv[])
{
	FILE * in	= fopen("C-large (1).in","rt");
	FILE * out	= fopen("out_large.txt","wt");

	int n;
	fscanf(in,"%d\n",&n);
	for(int i = 0; i<n; i++)
	{
		int k;
		fscanf(in,"%d\n",&k);
		int allsum = 0;
		int allsumcor = 0;
		vector<int> candies;
		vector<int> bits(100);
		for(int i = 0; i<k; i++)
		{
			int c;
			fscanf(in,"%d ",&c);
			candies.push_back(c);
			allsum = wrong_sum(allsum, c);
			allsumcor += c;
		}
		if(allsum != 0)
		{
			fprintf(out,"Case #%d: NO\n",i+1);
			continue;
		}

		sort(candies.begin(),candies.end());
		fprintf(out,"Case #%d: %d\n",i+1,allsumcor-candies[0]);
	}
	fclose(in);
	fclose(out);
	return 0;
}

