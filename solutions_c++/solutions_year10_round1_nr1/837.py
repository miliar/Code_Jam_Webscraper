#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <cstdlib>
#include <stdlib.h>
#include <stack>
#include <cstdio>
#include <map>
#include <cmath>
#include <time.h>
using namespace std;

#define MAX(a,b) ((a>=b)?a:b)
#define MIN(a,b) ((a<=b)?a:b)
#define ABS(a) ((a<0)?-(a):a)

int main()
{
	//freopen("in.txt","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("out2.out","w",stdout);
	vector<string> mas;
	int T,n,count,k,f,count1,count2,res;
	string s;
	bool f1;
	scanf("%d",&T);
	for(int t=0;t<T;++t)
	{
		res=-1;
		scanf("%d %d",&n,&k);
		mas.clear();
		for(int i=0;i<n;++i){cin >>s; mas.push_back(s);}
		for(int j=0;j<n;++j)
		{
			count=0; f1=false;
			for(int i=0;i<mas[j].size();++i)
				if(mas[j][i]=='.' && f1){++count; mas[j].erase(i,1); --i;} else f1=true;
			for(int i=0;i<count;++i)mas[j]='.'+mas[j];
		}
		for(int j=0;j<n;++j)
		{
			if(res==0)break;
			count1=count2=0; f=-1;
			for(int i=0;i<n;++i)
			{
				if(mas[j][i]=='.')continue;
				else if(mas[j][i]=='R')
				{
					++count1; count2=0; 
					if(count1==k) 
					{
						if(res==-1 || res==1)res=1;
						else res=0;
					}
				}
				else
				{
					++count2; count1=0; 
					if(count2==k) 
					{
						if(res==-1 || res==2)res=2;
						else res=0;
					}
				}
			}
		}
		for(int i=0;i<n;++i)
		{
			if(res==0)break;
			count1=count2=0; f=-1;
			for(int j=0;j<n;++j)
			{
				if(mas[j][i]=='.'){count1=count2=0; continue;}
				else if(mas[j][i]=='R')
				{
					++count1; count2=0; 
					if(count1==k) 
					{
						if(res==-1 || res==1)res=1;
						else res=0;
					}
				}
				else
				{
					++count2; count1=0; 
					if(count2==k) 
					{
						if(res==-1 || res==2)res=2;
						else res=0;
					}
				}
			}
		}
		for(int j=0;j<n;++j)
		{
			if(res==0)break;
			for(int ii=0;ii<n;++ii)
			{
				count1=count2=0; f=-1;
				for(int i=0;ii+i<n && j+i<n;++i)
				{
					if(mas[j+i][ii+i]=='.'){count1=count2=0; continue;}
					else if(mas[j+i][ii+i]=='R')
					{
						++count1; count2=0; 
						if(count1==k) 
						{
							if(res==-1 || res==1)res=1;
							else res=0;
						}
					}
					else
					{
						++count2; count1=0; 
						if(count2==k) 
						{
							if(res==-1 || res==2)res=2;
							else res=0;
						}
					}
				}
			}
		}
		for(int j=0;j<n;++j)
		{
			if(res==0)break;
			for(int ii=0;ii<n;++ii)
			{
				count1=count2=0; f=-1;
				for(int i=0;ii+i<n && i<=j;++i)
				{
					if(mas[j-i][ii+i]=='.'){count1=count2=0; continue;}
					else if(mas[j-i][ii+i]=='R')
					{
						++count1; count2=0; 
						if(count1==k) 
						{
							if(res==-1 || res==1)res=1;
							else res=0;
						}
					}
					else
					{
						++count2; count1=0; 
						if(count2==k) 
						{
							if(res==-1 || res==2)res=2;
							else res=0;
						}
					}
				}
			}
		}
		printf("Case #%d: ",t+1);
		if(res==-1)printf("Neither\n");
		else if(res==0)printf("Both\n");
		else if(res==1)printf("Red\n");
		else printf("Blue\n");
	}
	return 0;
}