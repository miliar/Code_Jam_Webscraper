#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
using namespace std;
typedef unsigned long long LLU;
typedef long long LL;
typedef pair<int,int> pii;
const int INF=99999999;
const double PI=3.1415926535897932384626;
const double EPS=1E-11;

int main()
{
	freopen("test.in","r",stdin); freopen("test.out","w",stdout);
	int testn;
	scanf("%d",&testn);
	for(int tn=1;tn<=testn;tn++)
	{
		int num;
		scanf("%d",&num);
		int lo=1,ro=1,lb=1,rb=1;
		int s=0;
		for(int i=0;i<num;i++)
		{
			char c;
			while(isspace(c=getchar()));
			int t;
			scanf("%d",&t);
			if(c=='O')
			{
				if(t>=lo && t<=ro)
				{
					lo=t;
					ro=t;
					lb--;
					rb++;
					s++;
					//printf("A");
				}
				else if(t<lo)
				{
					lb-=lo-t+1;
					rb+=lo-t+1;
					s+=lo-t+1;
					lo=t;
					ro=t;
					//printf("b");
				}
				else
				{
					lb-=t-ro+1;
					rb+=t-ro+1;
					s+=t-ro+1;
					lo=t;
					ro=t;
					//printf("c");
				}
			}
			else
			{
				if(t>=lb && t<=rb)
				{
					lb=t;
					rb=t;
					lo--;
					ro++;
					s++;
					//printf("d");
				}
				else if(t<lb)
				{
					lo-=lb-t+1;
					ro+=lb-t+1;
					s+=lb-t+1;
					lb=t;
					rb=t;
					//printf("e");
				}
				else
				{
					lo-=t-rb+1;
					ro+=t-rb+1;
					s+=t-rb+1;
					lb=t;
					rb=t;
					//printf("f");
				}
			}
			//printf("%d\n",s);
		}
		printf("Case #%d: ",tn);
		printf("%d\n",s);
	}
}
