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
	freopen("A-small-attempt7.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","r",stdin);
	//freopen("A-small.in","r",stdin);
	freopen("A-large.out","w",stdout);
#endif

	int case_n;
	//int c,d,n;
	char t;
	char z;
	char t1,t2,t3;

	int n,pd,pg;
	double temp;
	bool sign=false;
	int temp_int;
	//printf("A");

	vector<char> f1;
	vector<char> f2;
	vector<char> tr;
	vector<char> o1;
	vector<char> o2;

	scanf("%d",&case_n);
	//printf("%d\n",case_n);
	//scanf("%c",&z);
	//getchar();

	for (int i=0; i<case_n; i++)
	{
		scanf("%d",&n);
		getchar();

		scanf("%d",&pd);
			
		getchar();
		scanf("%d",&pg);
		getchar();

		//printf("%d,%d,%d\n",n,pd,pg);

		int j;
		for(j=1;j<=n;j++)
		{
			sign=false;
			if(pg==0&&pd==0){sign=true;break;}
			if(pg==0&&pd!=0){break;}
			//if(pg>pd){break;}
			temp=(double)((double)j*((double)pd/100.0));
			temp_int=(int)temp;
			//printf("%d\n",temp);
			if (temp<1.0)continue;
		
			if(temp!=(double)temp_int)continue;
// 			temp=(double)temp/pg*100.0;
// 			temp_int=(int)temp;
			// 			if(temp!=(double)temp_int)continue;
			else {
				//if((n*(double)pg/100.0)<=temp_int)
				//{
				if(pg!=0)
				{
					if(pg==100&&pd!=100);
					else
					{sign=true;
					break;
					}
				}
				//}

			}
		
		}

	
		if (sign==false)
		{
			printf("Case #%d: Broken\n",i+1,j);
		}
		else printf("Case #%d: Possible\n",i+1,j);
// 		{
// 			printf("Case #%d: %d Broken\n",i+1,j);
// 		}
// 		else printf("Case #%d: %d Possible\n",i+1,j);
	

	}
	return 0;
}
