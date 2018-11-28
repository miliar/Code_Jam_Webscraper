#include<iostream>
#include<cmath>
#include<math.h>
using namespace std;
#define INF 1<<30
#define N 808

int main()
{
	int t,i,j,k,r,n;
	freopen("C:\\Documents and Settings\\v-guozh\\Desktop\\in.txt","r",stdin);
   freopen("C:\\Documents and Settings\\v-guozh\\Desktop\\a.out","w",stdout);

    int ss[100]={5, 27, 143, 751, 935, 607, 903, 991, 335, 47, 943, 471, 55, 447,463, 991, 95, 607, 263, 151, 855, 527, 743, 351, 135, 407, 903, 791, 135, 647};
	scanf("%d",&t);
	for(r=0; r<t; r++)
	{
	    scanf("%d",&n);
	    printf("Case #%d: %d%d%d\n",r+1,ss[n-1]/100,(ss[n-1]%100)/10,ss[n-1]%10);
	}
	return 0;
}
