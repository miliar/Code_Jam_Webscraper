#include "stdio.h"
#include <vector>
using namespace std;
int main()
{

	int T;
	scanf(" %d", &T);

	
	for( int test = 1 ; test <= T ; test++ )
	{
		int N;
		int kes = 0;
		vector<int> Wleft;
		vector<int> Wright;
		scanf(" %d", &N);
	
		for( int i = 0 ; i < N ; i++ )
		{
			int left , right;
			scanf(" %d %d", &left , &right);
			for( int j = 0 ; j < i ; j++ )
			{
				if( (Wleft[j] > left && Wright[j] < right) || (Wleft[j] < left && Wright[j] > right) ) 
					kes++;
			}
			Wleft.push_back( left );
			Wright.push_back( right );
		}
	
		printf("Case #%d: %d\n",test,kes);
	}


	return 0;
}
