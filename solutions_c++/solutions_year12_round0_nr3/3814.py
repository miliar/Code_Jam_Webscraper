
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
using namespace std;

#include <sstream>
int *table;

int moveleft(unsigned m,int n)
{
	unsigned z;
	int k;
	k=8*sizeof(unsigned);
	z=(m>>n)|(m<<(k-n));
	return z;
}

#define SMALL
//#define LARGE
int main()
{
#ifdef SMALL
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
#endif
#ifdef LARGE
	freopen("C-large.in","r",stdin);
	//freopen("A-small.in","r",stdin);
	//freopen("C-large.out","w",stdout);
#endif
	
	int case_n;
	//printf("A");

	scanf("%d", &case_n);
	//printf("%d\n",case_n);

	int lower=0,upper=0;
	int count=0;
	char ori_c[20];
	char addori_c[40];
	char sub_c[20];

	int res[7];
	for (int i=0; i<case_n; i++)
	{
		count =0;
	
		scanf("%d",&lower);
		scanf("%d",&upper);
		//printf("%d ",lower);
		//printf("%d   ",upper);

		int tt=lower;
		int base=1;
		while(tt>=10)
		{
			tt=tt/10;
			base = base*10;
		}
		for(int m=lower;m<=upper;m++)
		{
			if(m>0&&m<10)continue;
			int test=m;
			int test0=m;
			int n=0;
			bool map=false;
			for(int k=0;k<7;k++)
			{
				res[k]=0;
			}
			
			while(test>=10)
			{
				test = test/10;
				
				test0 = test0/10+ (test0%10)*base;

				map=false;
				res[n]=test0;

				for(int k=0;k<n;k++)
				{
					if (res[k]==test0)
					{	
						map=true;
						break;
					}
				}
				n++;
				if(map==true)continue;
				if(test0 >=lower && test0 <=upper && test0>m)
				{
					//printf("%d %d\n",m,test0);
					count++;
				}
			}

		}
	
		printf("Case #%d: %d",i+1,count);
		printf("\n");

	}
	
	return 0;
}
