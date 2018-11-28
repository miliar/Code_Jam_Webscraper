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
int startsWith[1020], len[1020];
int main()	//I work out which group I reach from each starting group
{
	int T;
	FILE *in=fopen("parin.txt", "r");
	FILE *out=fopen("parout.txt", "w");
	fscanf(in, "%d", &T);
	for(int t=1; t<=T; t++)
	{
		int r, k, n;	//num rides, size coaster, num groups
		fscanf(in, "%d%d%d", &r, &k, &n);
		int groups[1020];
		for(int i=0; i<n; i++)
			fscanf(in, "%d", groups+i);
		for(int i=0; i<n; i++)
		{
			int rt=groups[i], ind=(i+1)%n;
			while(rt+groups[ind]<=k && ind!=i)
			{
				rt+=groups[ind];
				ind++;
				if(ind==n)
					ind-=n;
			}
			len[i]=rt;
			startsWith[i]=ind;
		}
		long long val=0;
		int ind=0;
		for(int i=0; i<r; i++)
		{
			val+=len[ind];
			ind=startsWith[ind];
		}
		fprintf(out, "Case #%d: %lld\n", t, val);
	}
	return 0;
}
