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
#include <hash_set>
#include <hash_map>

using namespace std;
using namespace stdext;

struct rinfo
{
	int cnt;
	long long sum;

	rinfo(int c, long long s) : cnt(c), sum(s) { }
};

int main()
{
	int nTestCases;
	int r, k, n;

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
		fscanf (in_file, "%d", &r);
		fscanf (in_file, "%d", &k);
		fscanf (in_file, "%d", &n);

		int arr[1005];
		hash_map<int, rinfo> findex;
		hash_map<int, rinfo>::iterator it;
		hash_map<int, long long> sums;
		long long tsum=0;

		for (int j=0; j<n;++j)
		{
			fscanf (in_file, "%d", &arr[j]);
			tsum += arr[j];
		}

		if (tsum <= k)
		{
			fprintf (out_file, "Case #%d: %ld\n", i, (tsum * r));
			continue;
		}

		int count=0,index=0;
		bool found=false;
		long long osum=0, sum=0;
		int tdiff;
		tsum=0;


		for (;;)
		{
			sum=0;
			for(;;)
			{
				sum += arr[index];
				if (sum > k)
				{
					sum -= arr[index];

					osum+=sum;
					++count;

					if ((it=findex.find(index)) != findex.end())
					{
						tsum = (osum - (*it).second.sum);
						tdiff = count - (*it).second.cnt;
						found=true;
					}
					else
						findex.insert(make_pair(index, rinfo(count, osum)));

					sums.insert(make_pair(count, sum));

					break;
				}
				++index;
				index = index%n;
			}
			if (found || count==r)
				break;
		}

		//long long s=tsum;
		if (count != r)
		{
			int diff = r-count;
			osum += ((long long)(diff / tdiff)) * tsum;
			
			int extra=diff%tdiff;
			for (int l=(1+count-tdiff);l<=(extra+count-tdiff);++l)
				osum += sums[l];
		}


		fprintf (out_file, "Case #%d: %ld\n", i, osum);
	}


	fclose(in_file);
	fclose(out_file);

	return 0;
}