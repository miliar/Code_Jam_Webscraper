#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>
#include <sstream>
#include <bitset>
using namespace std;


int main()
{
	
	
	//FILE *fp1 = fopen ("B-small-attempt0.in", "r");	
	//FILE *fp2 = fopen ("output2.txt", "w");
	FILE *fp1 = fopen ("B-large.in", "r");	
	FILE *fp2 = fopen ("output22.txt", "w");
	
	int T, n, s, p;
	fscanf (fp1, "%d\n", &T);
	
	for (int i = 0; i < T; ++i)
	{
		
		fscanf (fp1, "%d %d %d", &n, &s, &p);
		vector<int> scores(n);
		
		for (int j = 0; j < n; ++j)
		{
			int temp;
			fscanf (fp1, "%d", &temp);
			scores[j] = temp;
		}
		sort (scores.begin(), scores.end());
		reverse (scores.begin(), scores.end());
		
		int cnt =0, result = 0;
		for (int j = 0; j < n; ++j)
		{
			if (scores[j] == 0)
			{
				if (p == 0)
					result++;
				continue;
			}
			
			int quotient = scores[j] / 3;
			int remainder = scores[j] % 3;
			if (remainder !=0)
				quotient++;
			
			if (quotient >= p)
			{
				result++;
				continue;
			}
			
			bool flag = false;
			switch (remainder) {
				case 0:
					if (quotient + 1 >= p && cnt < s)
					{
						result++;
						cnt++;
						flag = true;
					}
					break;
				case 2:
					if (quotient + 1 >= p && cnt < s)
					{
						result++;
						cnt++;
						flag = true;
					}
					break;
				default:
					break;
			}
			
			if (!flag || cnt == s)
				break;
		}
		
		
		//print out
		fprintf (fp2, "Case #%d: %d\n", i + 1, result);
		
	}
	
	return 0;
	
}