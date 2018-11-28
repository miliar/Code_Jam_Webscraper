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
		int n;
		scanf("%d",&n);
		int i,d[1005];
		for(i=0;i<n;++i)
			scanf("%d",&d[i]);
		int min=100000001;
		sort(d,d+n);
		for(i=0;i<n-1;++i)
			if(d[i+1]-d[i]<min&&d[i+1]-d[i])
				min=d[i+1]-d[i];	
		if(min==100000001)
		{
			fprintf(aa,"Case #%d: %d\n",xx++,0);
			continue;
		}
		int tmp=sqrt(min)+1,j,index=0;
		int h[100000];
		for(i=1;i<=tmp;++i)
		{
			if(min%i==0)
			{
				h[index++]=i;
				h[index++]=min/i;
			}
		}
		sort(h,h+index);
		//for(i=0;i<index;++i)printf("%d ",h[i]);printf("\n");
		int flag=0;
		for(j=index-1;j>=0;--j)
		{
			int x=h[j]-d[0]%h[j];
			for(i=1;i<n;++i)
				if((h[j]-d[i]%h[j])!=x)
					break;
			if(i==n)
			{
				flag=1;
				if(x==h[j])
					fprintf(aa,"Case #%d: %d\n",xx++,0);
				else
					fprintf(aa,"Case #%d: %d\n",xx++,x);
			}
			if(flag==1)
				break;
		}
		if(flag==0)
			fprintf(aa,"Case #%d: %d\n",xx++,0);
	}
	fclose(aa);
	return 0;
}



