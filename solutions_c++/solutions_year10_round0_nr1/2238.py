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
		scanf("%d%d",&a,&b);
		double x=pow(2,a)-1;
		int y=x;
		if(b!=0&&b>=y)
		{
			if((b==y||(b-y)%(y+1)==0))
				fprintf(aa,"Case #%d: ON\n",xx++);
			else
				fprintf(aa,"Case #%d: OFF\n",xx++);
		}
		else
			fprintf(aa,"Case #%d: OFF\n",xx++);
	}
	fclose(aa);
	return 0;
}


