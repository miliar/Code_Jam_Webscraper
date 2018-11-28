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
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 

using namespace std;

int GYS(int A , int B)
{
	int div = 2;
	int G = 1;
	while(div <= min(A,B))
	{
		if(A%div == 0 && B%div == 0)
		{
			A =A / div ;
			B = B/ div;
			G = G* div;
		}
		else
		{
			div++;
		}
	}
	return G;

}

int main()
{
	freopen("A-small.in" ,"r", stdin);
	freopen("A-small.out","w", stdout);
	int case_num =0;
	bool done = false;
	scanf("%d\n" , &case_num);
	for(int i = 1 ;i<=case_num ; i++)
	{
		long long Day_N = 0 ;
		int Tot_PD =0 ;
		int Tot_PG = 0;
		scanf("%d %d %d \n" , &Day_N ,&Tot_PD , &Tot_PG);
		int tmp_GYS = 0;
		int today_min = 1;
		if(Tot_PD == 100 || Tot_PD ==0 )
		{
			today_min = 1;
		}
		else
		{
			tmp_GYS = GYS(Tot_PD , 100 - Tot_PD);
			today_min = 100 / tmp_GYS;
		}
		bool res = true;
		if(Day_N < today_min )
		{
			res = false;
		}
		if(Tot_PD!=0 && Tot_PG ==0)
		{
			res = false;
		}
		if(Tot_PD!=100 && Tot_PG ==100)
		{
			res = false;
		}
		if(res == true)
		{
			printf("Case #%d: %s  \n",i , "Possible");
		}
		else
		{
			printf("Case #%d: %s  \n",i , "Broken");
		}
	}
	return 0;
}