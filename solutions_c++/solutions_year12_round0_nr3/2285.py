#include <cstdio>
#include <cmath>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <utility>
#include <stack>
#include <queue>
#include <map>
#include <set>

#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define pi 2*acos(0.0)
#define eps 1e-9
#define PII pair<int,int> 
#define PDD pair<double,double>
#define LL long long
#define INF 1000000000

using namespace std;

int T,i,A,B,M,sum;
int ten[10];
set<int> s;

int main()
{
	ten[0]=1;
	for(i=1;i<10;i++) ten[i]=ten[i-1]*10;
	
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		scanf("%d %d",&A,&B);
		sum=0;
		for(M=A+1;M<=B;M++)
		{
			int bts=(int)ceil(log10(M)),temp=M;
			s.clear();
			for(int x=0;x<bts;x++)
			{
				int added = temp/ten[bts-1];
				temp=(temp%ten[bts-1])*10+added;
				if(s.find(temp)==s.end()) s.insert(temp);
			}
			
			for(set<int>::iterator it=s.begin();it!=s.end();it++)
			{
				temp = *it;
				if(temp<M && A<=temp && temp<=B) sum++;
			}
		}
		printf("Case #%d: %d\n",i,sum);
	}
	return 0;
}

