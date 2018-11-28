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

int gcd(int a, int b){ int t; while ( b > 0 ) { a %= b; t = a; a = b; b =t; } return a; }

int input[100];
int main()
{
	int cases , Case = 1;
	scanf("%d" , &cases);

	
	while( cases-- )
	{
		printf("Case #%d:" , Case++);   

		int n , L , H;
		scanf("%d%d%d" , &n,&L,&H);
		for(int i = 0 ; i < n ; i++ ) scanf("%d" , input+i);
		
		//brute
		char isOk = 0;
		for(int i = L; i <=H; i++)
		{

			for(int j = 0 ; j < n ; j++ )
			{
				int aa = i;
				int bb = input[j];
				if( aa < bb ) swap(aa,bb);
				if( aa%bb )
				{
					goto nextroud;
				}
			}
			isOk =1;
			printf(" %d\n" , i); break;
			nextroud:;
		}

		if(!isOk)
			puts(" NO");
	
	}

	return 0;
}
