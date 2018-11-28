#include<stdio.h>
#include<string.h>
#include<math.h>
#include<fstream>
#include<assert.h>
#include<time.h>
#include<limits.h>
#include<ctype.h>
#include<stdlib.h>
#include<assert.h>
#include<string>
#include<vector>
#include<list>
#include<deque> 
#include<set>
#include<map>
#include<stack>
#include<algorithm>
#include<iostream>
#include<cassert>
#include<complex>
#include<fstream>
#include<memory>
#include<new>
#include<queue>       //priority_queue优先队列
#include<iterator>    //运用iostream的iterator
#include<functional>  //使用预定义的函数对象
#include<iomanip>     //setw()函数
#include<utility>     //pair类型
using namespace std;
typedef double ll;
#define PI 3.141592653589793 //牛人用的 PI=acos(-1)
typedef pair<string,string>Pair;
/**************************************************/
/*               Author:LinusRush
                 date  :2010-05-08                */
/**************************************************/
int main()
{
	FILE *aa;
	aa=fopen("a.txt","w");
	int cases,a,b,xx=1;
	scanf("%d",&cases);
	while(cases--)
	{
		int r,k,n,d[20];
		scanf("%d%d%d",&r,&k,&n);
		int i;
		for(i=0;i<n;++i)
			scanf("%d",&d[i]);
		int ans=0;
		for(i=0;i<r;++i)
		{
			int j,sum=0;
			for(j=0;j<n;++j)
			{
				if(sum+d[j]<=k)
					sum+=d[j];
				else
					break;
			}
			ans+=sum;
			int index=j,tmp[20];
			for(j=0;j<n;++j)
				tmp[j]=d[j];
			for(j=0;j<n-index;++j)
				d[j]=d[j+index];
			int aaa=0;
			for(j=n-index;j<n;++j)
				d[j]=tmp[aaa++];
		}
		fprintf(aa,"Case #%d: %d\n",xx++,ans);
	}
	fclose(aa);
	return 0;
}


