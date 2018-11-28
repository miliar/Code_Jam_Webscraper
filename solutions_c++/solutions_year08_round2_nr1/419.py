// Was build with STL libraries of standard MS VisualStudio 2005 SP1
// Target application was console win 32 application with multibite character set setting. 
// Used software were licensed to Align Technology Inc

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <math.h>
#define M_PI       3.14159265358979323846

/////////////////////////////////////////////////////////////////

int hashMe(int X, int Y)
{
	return (X%3)+3*(Y%3);
}

int main(int argc, char* argv[])
{
	int numOfCases;
	scanf("%d", &numOfCases);
	for(int cn = 0; cn < numOfCases; cn++)
	{
		int n, A, B, C, D, x0, y0, M;
		scanf("%d%d%d%d%d%d%d%d", &n, &A, &B, &C, &D, &x0, &y0, &M);
//		printf("%d %d %d %d %d %d %d %d\n", n, A, B, C, D, x0, y0, M);

		std::vector<int> counts(9, 0);
		int X = x0, Y = y0;
		counts[hashMe(X, Y)]++;
		for(int i = 1; i < n; i++)
		{
			X = (__int64(A) * __int64(X) + __int64(B)) % __int64(M);
			Y = (__int64(C) * __int64(Y) + __int64(D)) % __int64(M);
			counts[hashMe(X, Y)]++;
		}
		int count = 0;
		for(int i = 0; i < 9; i++)
		{
			count += (counts[i]*(counts[i]-1)*(counts[i]-2))/6;
			for(int j = i+1; j < 9; j++)
			{
				X = (18 - i-j)%3;
				Y = (18 - i/3 - j/3)%3;
				int third = hashMe(X, Y);
				if(third > j)
					count += counts[i]*counts[j]*counts[third];
			}
		}
		std::cout << "Case #" << (cn+1) << ": " << count << "\n";
	}
	return 0;
}

