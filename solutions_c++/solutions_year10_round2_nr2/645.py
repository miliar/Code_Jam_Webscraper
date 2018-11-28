#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <stdlib.h>

using namespace std;

int main(int argc, char** argv)
{
	int t;
	FILE *f = fopen(argv[1], "rt");
	fscanf(f, "%d", &t);
	int crt = 0;
	
	while(crt<t)
	{
		int n, k, b, t;
		fscanf(f, "%i %i %i %i\n", &n, &k, &b, &t);
		
		vector<int> x, v;
		for (int i=0;i<n;i++)
		{
			int temp;
			fscanf(f, "%i", &temp);
			x.push_back(temp);
		}	
		for (int i=0;i<n;i++)
		{
			int temp;
			fscanf(f, "%i", &temp);
			v.push_back(temp);
		}
		
		int nr = 0;
		for (int i=0;i<n;i++)
		{
			if ((b-x[i]) <= v[i]*t)
				nr ++;
		}	
		if (nr < k) 
		{
			printf("Case #%i: IMPOSSIBLE\n", ++crt);
			continue;
		}
		
		nr = 0;
		int rez = 0;
		int count = 0;
		for (int i=n-1;i>=0 && count < k;i--)
		{
			if ((b-x[i]) > v[i]*t)
				nr++;
			else if ((b-x[i]) <= v[i]*t)
			{
				rez += nr;
				count ++;
			}
		}
		
		printf("Case #%i: %i\n", ++crt, rez);
	}
	
	return 0;
}
