#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef long long ll;

void main()
{
	FILE* fpIn = fopen("D:\\A-small-attempt0.in", "r");
	if(fpIn == NULL)
		printf("Unable to read file");

	FILE *fpOut = fopen("C:\\output.txt", "w");
	if(fpOut == NULL)
		printf("Unable to create a output file");


	long total_tests = 1;
	long case_num = 1;

	long result = 0;
	vector<long> freq;
	
	fscanf(fpIn, "%d", &total_tests);
	long p, k, l;

	while(case_num<=total_tests)
	{
		fscanf(fpIn, "%ld%ld%ld", &p, &k, &l);

		long lf;
		while(l>0)
		{
			fscanf(fpIn, "%ld", &lf);
			freq.push_back(lf);
			l--;
		}

		sort(freq.begin(), freq.end());

		vector<long>::reverse_iterator iter1;
		long size = 1;
		int factor = 1;
		long sum = 0;
		for(iter1 = freq.rbegin(); iter1 != freq.rend(); iter1++, size++)
		{
			sum += *iter1;
			if(size == k)
			{
				result += (sum*factor);
				sum = 0;
				size = 0;
				factor++;
			}
		}
		
		if(sum)
			result += (sum*factor);

		fprintf(fpOut, "Case #%ld: %ld\n",case_num, result);
		case_num++;
		result = 0;
		freq.clear();
	}
}