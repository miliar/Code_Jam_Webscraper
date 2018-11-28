#include <stdio.h>
#include <sstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <list>
#include <iomanip>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <cassert>
#include <string.h>
#include <windows.h>
using namespace std;
#pragma comment(linker, "/STACK:20000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "C-large";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
  freopen((problem_name+".out").c_str(),"wt",stdout);
}

long long mas[1010];
long long cur[1010];
long long step[1010];


int main()
{
	init();


	int tst;
	scanf("%d",&tst);

	
	for (int cas=1;cas<=tst;cas++)
	{
		long long r,k,n;
		scanf("%lld%lld%lld",&r,&k,&n);
		long long sum=0;
		for (int i=0;i<n;i++) {
			scanf("%lld",&mas[i]);
			sum+=mas[i];
		}
		memset(cur,0,sizeof(cur));
		memset(step,0,sizeof(step));

		step[0]=1;
		int pos=0;
		long long res=0;
	//	long long add = (k/sum)*sum;
	//	k%=sum;
		for (int i=1;i<=r;i++)
		{
			long long s = 0;
			while (s+mas[pos]<=k && s+mas[pos]<=sum)
			{
				s+=mas[pos];
				pos++;
				if (pos==n) pos=0;
			}
			if (step[pos])
			{
				long long len = (i+1)-step[pos];
				long long left = (r-i)/len;
				s+=left*((res+s)-cur[pos]);
				i+=left*len;			
			}		
			step[pos]=i+1;
			res+=s;
			cur[pos]=res;
		}

		printf("Case #%d: %lld\n",cas,res);
	
	}
	


  return 0;
}
