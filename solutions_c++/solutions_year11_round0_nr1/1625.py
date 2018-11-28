#include <functional>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <string>
#include <vector>
#include <cstdio>
#include <bitset>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;
#define MAX 105

struct Robot
{
	int time,bottom,now;
	Robot(int t,int b,int n):time(t),bottom(b),now(n){}
};
vector<Robot> Orange;
vector<Robot> Blue;
int Orange_pos,Blue_pos;

int main()
{
	//freopen("A-large.in","r",stdin);
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	//printf("Algorithm is Beautiful!\n");
	int T,casetest=1;
	cin>>T;
	while(T--)
	{
		printf("Case #%d: ",casetest++);
		char id;
		int n,num;
		cin>>n;
		__int64 ans=0;
		int start=1;
		Orange.clear();
		Blue.clear();
		for(int i=0;i<n;i++)
		{
			cin>>id>>num;
			if(id=='O')Orange.push_back(Robot(i,num,1));
			if(id=='B')Blue.push_back(Robot(i,num,1));
		}
		Orange_pos=Blue_pos=0;
		int sz1=Orange.size(),sz2=Blue.size(),step;
		while(Orange_pos<sz1 && Blue_pos<sz2)
		{
			if((Orange[Orange_pos].time<Blue[Blue_pos].time))
			{
				 step=abs(Orange[Orange_pos].bottom-Orange[Orange_pos].now)+1;
			     ans=ans+step;
				 Orange_pos++;
				 if(Orange_pos<sz1)Orange[Orange_pos].now=Orange[Orange_pos-1].bottom;
				 if(abs(Blue[Blue_pos].now-Blue[Blue_pos].bottom)<=step)
					 Blue[Blue_pos].now=Blue[Blue_pos].bottom;
				 else
				 {
					 if(Blue[Blue_pos].now>Blue[Blue_pos].bottom)Blue[Blue_pos].now=Blue[Blue_pos].now-step;
					 else if(Blue[Blue_pos].now<Blue[Blue_pos].bottom)
						 Blue[Blue_pos].now=Blue[Blue_pos].now+step;
				 }
			}
			else if((Orange[Orange_pos].time>Blue[Blue_pos].time))
			{
				step=abs(Blue[Blue_pos].bottom-Blue[Blue_pos].now)+1;
				ans=ans+step;
				Blue_pos++;
				if(Blue_pos<sz2)Blue[Blue_pos].now=Blue[Blue_pos-1].bottom;
				if(abs(Orange[Orange_pos].now-Orange[Orange_pos].bottom)<=step)
					Orange[Orange_pos].now=Orange[Orange_pos].bottom;
				else
				{
					if(Orange[Orange_pos].now>Orange[Orange_pos].bottom)Orange[Orange_pos].now=Orange[Orange_pos].now-step;
					else if(Orange[Orange_pos].now<Orange[Orange_pos].bottom)
						Orange[Orange_pos].now=Orange[Orange_pos].now+step;
				}
			}

		}
		if(Orange_pos>=sz1)
		{
			while(Blue_pos<sz2)
			{
				ans+=abs(Blue[Blue_pos].bottom-Blue[Blue_pos].now)+1;
				Blue_pos++;
				if(Blue_pos<sz2)Blue[Blue_pos].now=Blue[Blue_pos-1].bottom;
			}
		}
		else if(Blue_pos>=sz2)
		{
			while(Orange_pos<sz1)
			{
				ans+=abs(Orange[Orange_pos].bottom-Orange[Orange_pos].now)+1;
				Orange_pos++;
				if(Orange_pos<sz1)Orange[Orange_pos].now=Orange[Orange_pos-1].bottom;
			}
		}
		printf("%I64d\n",ans);
	}
	return 0;
}