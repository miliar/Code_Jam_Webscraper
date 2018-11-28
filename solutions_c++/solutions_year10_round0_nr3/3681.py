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
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define SMALL 10
#define LARGE 1000
using namespace std;
int group[SMALL];
void cleargroup()
{
	int i=0;
	for(i=0;i<SMALL;i++)
	{
		group[i]=-1;
	}
}
int main()
{
    freopen("C-small-3.out","w",stdout);
    freopen("C-small-3.in","r",stdin);
    int T=0;
    int N=0;
    int R=0;
    int K=0;
    int i=0,j=0;
    int temp=0;
    int index=0;
    int cnt=0;
    int num=0;
    int k=0;
    int amount=0;
    scanf("%d",&T);
	for(i=0;i<T;i++)
	{
		index=0;
		num=0;
		amount=0;
		cleargroup();
		scanf("%d%d%d",&R,&K,&N);
		for(j=0;j<N;j++)
		{
			scanf("%d",&temp);
			group[j]=temp;
			amount+=temp;
		}
		if(amount<=K)
		{
			printf("Case #%d: %d\n",i+1,amount*R);
			continue;
		}
		while(R)
		{
			num = 0;
			while(num<=K)
			{
				index = index % N;
				num+=group[index];
				index++;
			}
			num-=group[index-1];
			index--;
			cnt+=num;
			R--;
		}
		printf("Case #%d: %d\n",i+1,cnt);
		cnt=0;
	}
    return 0;
}
