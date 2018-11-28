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
	freopen("A-large (2).in", "r", stdin);
	freopen("A-large.out", "w", stdout);
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

	int r,c;
	char temp;
	char mat[50][50];
	bool ocu[50][50];
	bool broken=false;;

	vector<char> f1;
	vector<char> f2;
	vector<char> tr;
	vector<char> o1;
	vector<char> o2;

	scanf("%d",&case_n);
//	printf("%d\n",case_n);
	//scanf("%c",&z);
	//getchar();

	for (int i=0; i<case_n; i++)
	{

		for (int m=0;m<50;m++)
		{
			for (int n=0;n<50;n++)
			{
				ocu[m][n]=false;
			}
		}
		broken=false;
		scanf("%d",&r);
		getchar();

		scanf("%d",&c);

		getchar();
	//	printf("%d,%d\n",r,c);
		for (int m=0;m<r;m++)
		{
			for (int n=0;n<c;n++)
			{
				mat[m][n]=getchar();
				if (mat[m][n]=='.')
				{
					ocu[m][n]=true;
				}
			}
			getchar();
		}

	
		for (int m=0;m<r-1;m++)
		{
			for (int n=0;n<c-1;n++)
			{
				if(ocu[m][n]==true)continue;
				if(mat[m][n+1]=='#'&&mat[m+1][n+1]=='#'&&mat[m+1][n]=='#')
				{
					ocu[m][n]=true;
					ocu[m+1][n]=true;
					ocu[m][n+1]=true;
					ocu[m+1][n+1]=true;

					mat[m][n]=mat[m+1][n+1]='/';
					mat[m+1][n]=mat[m][n+1]='\\';
		
				}
			}
		}

		for (int m=0;m<r;m++)
		{
			for (int n=0;n<c;n++)
			{
				if(mat[m][n]=='#')
				{
broken=true;
break;
				};
			}
		}

printf("Case #%d:\n",i+1);

		if (broken==true)
		{
			printf("Impossible\n");
		}
		else
		{
			for (int m=0;m<r;m++)
			{
				for (int n=0;n<c;n++)
				{
					printf("%c",mat[m][n]);
				}
				printf("\n");
			}
		}
	}
	return 0;
}
