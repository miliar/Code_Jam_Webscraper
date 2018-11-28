#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define LL long long
#define LD long double
#define pi 3.1415926535897932384626433
#define sqr(a) ((a)*(a))

using namespace std;

int T,N,S,P;

int main()
{	
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	scanf("%d\n", &T);

	for (int Case = 1; Case <= T; Case ++)
	{
		int ans = 0;
		int usedSup = 0;
		int t;
		scanf("%d%d%d",&N,&S,&P);
		
		for (int i=0;i<N;i++)
		{
			scanf("%d",&t);
			if (P == 0)
			{
				ans = N;
				string temp;
				getline(cin,temp);
				break;
			}
			if (t != 0)
			{	
				if (t >= (P*3-2)){
					ans++;
				}
				else if (t >= (P*3-4)  &&  usedSup<S){
					ans++;
					usedSup++;
				}
			}
		}
		
		cout << "Case #" << Case << ": " << ans << endl;	
	}
		
	return 0;
}