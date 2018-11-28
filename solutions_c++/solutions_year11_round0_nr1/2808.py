#include <iostream>
#include <stdio.h>
#include <string>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <map>
#include <math.h>
#include <queue>
#include <stack>
#include <list>
#include <deque>
#include <set>
#include <numeric>
#include <functional>
#include <ctype.h>
#include <utility>
#include <cassert>
#include <time.h>
using namespace std;

#define  max(a,b)  ((a)>(b)?(a):(b))
#define  min(a,b)  ((a)<(b)?(a):(b))
#define out(x) (cout << #x << " = " << x <<endl)
const int inf = 0x3f3f3f3f;
const double eps = 1e-10;
#define N 100005

int a[1002];

struct node{
	char name;
	int but;
}dd[102];
int main()
{
	int T;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin >> T;
	int cases = 1;
    dd[0].name = 'O';
	dd[0].but = 1;
	dd[1].name = 'B';
	dd[1].but = 1;
	while(T--)
	{
		int i,j,k;
		int n;
		cin >> n;
	    for(i = 2;i < n+2;i++)
			cin >> dd[i].name >> dd[i].but;
		int ot = 0;
		int bt = 0;
		int ans = 0;
		if(dd[2].name == 'O')
		{
			ot = dd[2].but - 1 +1;
			ans = ot;
		}
		else
		{
			bt = dd[2].but;
			ans = bt;
		}
		for(i = 3; i < n+2; i++)
		{
             if(dd[i].name == dd[i-1].name)
			 {
				 
				 if(dd[i].name == 'O')
				 {
					 ans = abs(dd[i].but - dd[i-1].but) + 1 + ot;
					 ot = ans;
				 }
				 else 
				 {
					 ans = abs(dd[i].but - dd[i-1].but) + 1 + bt;
					 bt = ans;
				 }
			 }
			 else
			 {
				 for(j = i-1;j >= 0; j--)
				 {
					 if(dd[i].name == dd[j].name)
					 {
						 if(dd[i].name == 'O')
						 {
							 if(ot + abs(dd[i].but - dd[j].but) + 1 <= ans )
							 {
								 ans ++;
							 }
							 else
							 {
								 ans =  ot + abs(dd[i].but - dd[j].but) + 1;
							 }
							 ot = ans;
						 }
						 else
						 {
                             if(bt + abs(dd[i].but - dd[j].but) + 1 <= ans )
							 {
								 ans ++;
							 }
							 else
								 ans = bt + abs(dd[i].but - dd[j].but) + 1; 
							 bt = ans;
						 }
                         break;
					 }
				 }
			 }
			 
		}
		printf("Case #%d: %d\n",cases++,ans);
	}
	return 0;
}
