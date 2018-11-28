// google codejam.cpp : Defines the entry point for the console application.
//

// BEGIN CUT HERE
#include <stdafx.h>
// END CUT HERE
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std;

#define REP(i,n) for(int i=0;i<n;++i)
#define VI vector<int>
#define VII vector<VI>
#define ALL(n) n.begin(),n.end()
#define LL long long
#define SIZE(o) o.size()

int dx4[]={0,0,-1,1};
int dy4[]={-1,1,0,0};


int main(int argc, _TCHAR* argv[])
{
	freopen("in","r",stdin);freopen("out","w",stdout);
	
	
	int testcase;
	scanf("%d",&testcase);
	
	int i,j,k;
	int caseID;
	

	REP(caseID,testcase)
	{
		int R,K,N;
		scanf("%d%d%d",&R,&K,&N);
		vector<int> num(N);
		REP(i,N)
		{
			scanf("%d",&num[i]);
		}
		int add[1000];
		memset(add,0,1000);
		LL sum[1000];
		memset(sum,0,2000);
		int last=0;
		LL ans=0;
		REP(i,R)
		{
			int nextid=last;
			LL now=0;
			REP(j,N)
			{
				LL next=now+num[(j+last)%N];
				if(next>K)
				{
					nextid=(j+last)%N;
					break;
				}
				now=next;
			}
			ans+=now;
			if(add[last]!=0)
			{
				int circle=i+1-add[last];
				LL clen=ans-sum[last];
				ans+=(R-i-1)/circle*clen;
				int left=(R-i-1)%circle;
				REP(j,N)
					if(add[j]-add[last]==left)
						ans+=sum[j]-sum[last];
				break;
			}
			add[last]=i+1;
			sum[last]=ans;
			last=nextid;
		}
		printf("Case #%d: ",caseID+1);
		cout<<ans<<endl;

		
	}
	
	
	return 0;
}

