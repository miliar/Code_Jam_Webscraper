#pragma warning (disable : 4786)

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>

using namespace std;

#define min(a,b) ((a) < (b) ? (a) : (b))
#define max(a,b) ((a) > (b) ? (a) : (b))

#define CLR(a) memset(a,0,sizeof(a))

int cases,caseno,n,m,tTime;

struct info
{
	int stTime,ndTime;
	bool operator < (const info &b) const
	{
		if(stTime!=b.stTime) return stTime < b.stTime;
		return ndTime < b.ndTime;
	}
}A[101],B[101];

void input()
{
	int i,x,y;
	char a[20],b[20];

	scanf("%d %d %d",&tTime,&n,&m);
	for(i=0;i<n;i++)
	{
		scanf("%s %s",a,b);
		sscanf(a," %d : %d ",&x,&y);
		A[i].stTime=x*60+y;
		sscanf(b," %d : %d ",&x,&y);
		A[i].ndTime=x*60+y;
	}
	for(i=0;i<m;i++)
	{
		scanf("%s %s",a,b);
		sscanf(a," %d : %d ",&x,&y);
		B[i].stTime=x*60+y;
		sscanf(b," %d : %d ",&x,&y);
		B[i].ndTime=x*60+y;
	}
}

void process()
{
	int ptrA,ptrB,cntA,cntB,x;
	bool flag;
	list <int> LA,LB;
	list <int> ::iterator l,l1;

	sort(A,A+n);
	sort(B,B+m);
	ptrA=ptrB=0;
	cntA=cntB=0;
	while(1)
	{
		if(ptrA==n && ptrB==m) break;

		if(ptrA==n) x=1;
		else if(ptrB==m) x=0;
		else
		{
			if(A[ptrA].stTime <= B[ptrB].stTime) x=0;
			else x=1;
		}
		if(x==0)
		{
			flag=false;
			for(l=LA.begin();l!=LA.end();l++)
			{
				if(*l<=A[ptrA].stTime)
				{
					LA.erase(l);
					flag=true;
					break;
				}
			}
			if(!flag) cntA++;
			LB.push_back(A[ptrA].ndTime+tTime);
			ptrA++;
		}
		else
		{
			flag=false;
			for(l=LB.begin();l!=LB.end();l++)
			{
				if(*l<=B[ptrB].stTime)
				{
					LB.erase(l);
					flag=true;
					break;
				}
			}
			if(!flag) cntB++;
			LA.push_back(B[ptrB].ndTime+tTime);
			ptrB++;
		}
	}
	printf("Case #%d: %d %d\n",++caseno,cntA,cntB);
}

int main()
{
	//freopen("Inputs\\B-large.in","r",stdin);
	//freopen("Inputs\\B1.ans","w",stdout);

	scanf("%d",&cases);
	while(cases--)
	{
		input();
		process();
	}
	return 0;
}