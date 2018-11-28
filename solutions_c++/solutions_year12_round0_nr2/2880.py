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


#define LARGE
//#define LARGE
int main()
{
#ifdef SMALL
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
#endif
#ifdef LARGE
	freopen("B-large.in","r",stdin);
	//freopen("A-small.in","r",stdin);
	freopen("B-large.out","w",stdout);
#endif

	int case_n;
	char back;

	scanf("%d", &case_n);
	scanf("%c",&back);
//	printf("%d ",case_n);

	int n,sur,point;
	int num=0;
	int count=0;
	int posi_case=0;
	
	for (int i=0; i<case_n; i++)
	{
		count=0;
		scanf("%d",&n);
		scanf("%d",&sur);
		scanf("%d",&point);

		posi_case = n;

		//printf("%d ",n);
		//printf("%d ",sur);
		//printf("%d    ",point);

		for(int j=0;j<n;j++)
		{
			scanf("%d",&num);
			//printf("%d  ",num);
			if(num==0)
			{
				if(point==0)
					count++;
				else
					posi_case--;
			}
			else if((num % 3)==0)
			{
				if((num/3) >= point)
					count++;
				if((num/3) <= point-2)
					posi_case --;
			}
			else if((num%3) ==1)
			{
				if(((num/3)+1) >= point)
					count++;
				if(((num/3)+1) <= point-1)
					posi_case--;
			}
			else if((num%3)==2)
			{
				if(((num/3)+1) >= point)
					count++;
				if(((num/3)+1) <= point-2)
					posi_case--;
			}		
		}
		count= count+max(min(sur,posi_case - count),0);
		printf("Case #%d: %d",i+1,count);
		printf("\n");
	}
	return 0;
}
