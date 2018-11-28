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

using namespace std;

int main()
{
	long long cases,pd,pg,n;
	FILE* pFile=fopen("11.out","w");
	scanf("%lld",&cases);
	for(long long c=1;c<=cases;c++)
	{
		bool flag=0;
		scanf("%lld %lld %lld",&n,&pd,&pg);
		for(long long i=1;i<=n;i++)
			if((pd*i)%100==0)
			{
				flag=1;
				break;
			}
		if(pd<100&&pg==100||pd>0&&pg==0) flag=0;
		fprintf(pFile,"Case #%lld: ",c);
		if(!flag) fprintf(pFile,"Broken\n");
		else fprintf(pFile,"Possible\n");
	}
	return 0;
}