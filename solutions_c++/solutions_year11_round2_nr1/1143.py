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

char input[128][128];

int win[128];
int total[128];

double wp[128];
double owp[128];
double oowp[128];
int main()
{
	int cases , Case = 1;
	scanf("%d" , &cases);

	
	while( cases-- )
	{
		printf("Case #%d:\n" , Case++);
		int n;
		scanf("%d" , &n);
		for(int i = 0 ; i <n;i++)
		{
			scanf("%s" , &input[i]);

			win[i] = total[i] = 0;
			for(int j=0;j<n;j++)
			{
				if( input[i][j] == '1') win[i]++;
				if( input[i][j] !='.' ) total[i]++;
			}
			wp[i] = (double)win[i]/(double(total[i]));
		}

		for(int i = 0 ; i <n;i++)
		{
			owp[i] = 0;
			
			for(int j=0;j<n;j++)
			{
				if( input[i][j] !='.' && total[j]-1 > 0 )
				{
					int ww = win[j];
					if(input[i][j] == '0') ww--;
					owp[i] += ww/(double)(total[j]-1);
				}
			}
			owp[i] /= double(total[i]);
		}

		for(int i = 0 ; i <n;i++)
		{
			oowp[i] = 0;
			
			for(int j=0;j<n;j++)
			{
				if( input[i][j] !='.' )
				{
					oowp[i] += owp[j];
				}
			}
			oowp[i] /= double(total[i]);
		}

		for(int i = 0 ; i <n;i++)
			printf("%0.8lf\n" , 0.25*wp[i]  + 0.5*owp[i] +0.25*oowp[i]);

	
	}

	return 0;
}