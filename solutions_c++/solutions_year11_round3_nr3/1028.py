#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <stdint.h>
#include <stdlib.h>
using namespace std;

#define SMALL
//#define LARGE
int main()
{
#ifdef SMALL
	//freopen("A-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0 (1).in", "r", stdin);
	freopen("B-small.out", "w", stdout);
#endif
#ifdef LARGE
	freopen("B-large.in","r",stdin);
	//freopen("A-small.in","r",stdin);
	freopen("B-large.out","w",stdout);
#endif

	int case_n;
	int n,l,h;
	int ans;
	int mat[10000];
	//int c,d,n;
	char t;
	char z;
	char t1,t2,t3;
	bool sign=false;



	vector<char> f1;
	vector<char> f2;
	vector<char> tr;
	vector<char> o1;
	vector<char> o2;

	scanf("%d",&case_n);
	///printf("%d\n",case_n);
	//scanf("%c",&z);
	//getchar();

	for (int i=0; i<case_n; i++)
	{
		sign=false;
		ans=0;
		scanf("%d",&n);
		getchar();

		scanf("%d",&l);

		getchar();
		scanf("%d",&h);
		getchar();

		//printf("%d,%d,%d\n",n,l,h);

		for(int j=0;j<n;j++)
		{
			scanf("%d",&mat[j]);
			getchar();

		}

		for(int j=l;j<=h;j++)
		{
			int m;
			for(m=0;m<n;m++)
			{
				if(mat[m]%j==0||j%mat[m]==0)continue;
				else 
				{
					break;
				}
				
			}
			if(m==n)
			{
				sign=true;
				ans=j;
				break;
			}
		}


		if (sign==false)
		{
			printf("Case #%d: NO\n",i+1);
		}
		else printf("Case #%d: %d\n",i+1,ans);
	}
	return 0;
}
