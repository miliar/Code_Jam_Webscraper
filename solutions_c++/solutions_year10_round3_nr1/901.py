#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
 
int main()
{
	int iTests;
	scanf("%d", &iTests);
	
	for(int iTestCnt = 1; iTestCnt <= iTests; iTestCnt++ )
	{
		vector< pair<int,int> > segments;
		int iSegments;
		scanf("%d", &iSegments);
		for(int i=0; i < iSegments; i++)
		{
			int a, b;
			scanf("%d%d", &a, &b);
			segments.push_back( make_pair( a, b ) );
		}
		
		int iRes = 0;
		
		for(int iFirst = 0; iFirst < iSegments; iFirst++ )
		{
			for(int iSecond = iFirst + 1; iSecond < iSegments; iSecond++ )
			{
				const int a1 = segments[ iFirst ].first;
				const int b1 = segments[ iFirst ].second;
				const int a2 = segments[ iSecond ].first;
				const int b2 = segments[ iSecond ].second;
				
				if( (a1-a2)*(b1-b2) < 0 )
					iRes++;
			}
		}
		printf("Case #%d: %d\n", iTestCnt, iRes);
	}
	return 0;
}
