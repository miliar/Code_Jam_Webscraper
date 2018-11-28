#include <iostream>
#include <stdio.h>
#include <set>
#include <map>
#include <list>
#include <algorithm>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <vector>

using namespace std;

struct node
{
	int b1;
	int b2;

	friend bool operator < (const node& n1, const node& n2)
	{
		if (n1.b1 < n2.b1)
			return true;
		//else if (n1.b1 == n2.b2 && n1.b2 < n2.b2)
		//	return true;

		return false;
	}
};

int main()
{
	int nTestCases;
	

	FILE *in_file;
	FILE *out_file;

	in_file = fopen("prob1_in.txt", "r");
	out_file = fopen("prob1_out.txt", "w+");

#define in_file stdin
#define out_file stdout

	if (in_file == NULL || out_file==NULL)
		return 0;

	fscanf(in_file, "%d\n", &nTestCases);

	for (int i=1; i<=nTestCases; ++i)
	{
		int N;
		set<node> nl;

		fscanf (in_file, "%d", &N);

		for (int j=0; j<N; ++j)
		{
			node n;
			fscanf (in_file, "%d", &n.b1);
			fscanf (in_file, "%d", &n.b2);

			nl.insert(n);
		}

		//sort (nl.begin(), nl.end());// nl.sort();

		int cnt=0;

		for (set<node>::iterator it=nl.begin(); it!=nl.end(); ++it)
		{
			node nd=*it;
			if (nd.b1 != nd.b2)
			{
				for (set<node>::iterator it1=nl.find(*it); it1!=nl.end(); ++it1)
				{
					if (((*it1).b1 > nd.b1 && (*it1).b2 < nd.b2))
					{
						++cnt;
					}
				}
			}

		}

		fprintf (out_file, "Case #%d: %d\n", i, cnt);
	}


	fclose(in_file);
	fclose(out_file);

	return 0;
}