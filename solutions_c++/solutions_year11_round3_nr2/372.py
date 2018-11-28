//compiled in vc
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <complex>
// C++
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <climits>
#include <ctime>
using namespace std;


long long input[1000000+10];
long long C[1024];

long long DP[1000000+10][2];


void maxTestCase()
{
	int N = 10 , C = 1000;
	cout << N << endl;
	while(N--)
	{
		cout << 1000000 << " " << 100000000000 << " " << 1000000 << " " << 1000 << endl;
		for(int i = 0 ; i < C ; i++ )
		{
			cout << 10000<< endl;
		}
	}


}

int main()
{
	//maxTestCase();
//	return 0;
	//freopen("C:\\Code Jam\\1C\\B\\test.in" , "r" , stdin);


	int cases , Case = 1;
	scanf("%d" , &cases);

	
	

	while( cases-- )
	{
		printf("Case #%d: " , Case++);   
		long long L , t , n , c;
		scanf("%lld%lld%lld%lld" , &L , &t , &n , &c);  
		for(int i = 0 ; i < c; i++)
			scanf("%lld" , C+i);

		input[0] = 0;
		int yeah = 0;

		int boostStartAt = -1;
		long long ans = 0;

		long long ansAfter = 0 , anshalf = 0;
		for(int i = 1 ; i <= n ; i++)
		{
			input[i] = C[yeah++];
			yeah %=c;

			if( boostStartAt == -1 )
			{
				long long timeNeeded = input[i]*2LL;

				ansAfter += timeNeeded;
				anshalf = ansAfter;

				if( ansAfter >= t )
				{
					boostStartAt = i;
					if(L)
					anshalf = t + (anshalf-t)/2LL;

				}
				
			}
			
		}

		if( boostStartAt != -1  )
		{

			sort(input+boostStartAt+1 , input + n+1 );
			reverse(input+boostStartAt+1 , input + n+1 );
			for(int i = boostStartAt+1; i <= n; i++ )
			{
				if(L > 0 )
				{
					
					ansAfter += input[i];
					if( L > 1 ) anshalf += input[i];
					else anshalf += input[i]*2LL;;
					L--;
				}
				else
				{
					ansAfter += input[i]*2LL;
					anshalf +=  input[i]*2LL;
				}
			}



		}
			ans = ansAfter;
		if( anshalf > 0 && anshalf < ansAfter ) ans = anshalf;

		printf("%lld\n" , ans);

	
	}

	return 0;
}
