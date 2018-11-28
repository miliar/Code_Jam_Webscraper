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


#define SIZE 1024
int in[SIZE];

int main()
{
	int cases , Case = 1;
	scanf("%d" , &cases);

	while( cases-- )
	{
		printf("Case #%d: " , Case++);
		int n;
		scanf("%d" , &n) ;

		int wtf = 0;
		for(int i=0;i<n;i++) { scanf("%d" , &in[i]); if( in[i] != i+1 )wtf++; }
		printf("%.8lf\n" , 1.0*wtf); //huh..?
	}

	return 0;
}