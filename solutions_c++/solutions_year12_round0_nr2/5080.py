
/*
Dinesh Reddy
National Institute of Technology,Warangal.
*/
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <set>
#include <sstream>
#include <list>
#include <map>
#include <queue>
#include <stack>

#define pb push_back
#define mp make_pair
#define all(x) x.begin(),x.end()
#define rep(i,n) for(int i=0;i<n;i++)
#define print(x) cout<<#x<<" is "<<x<<endl;
#define inf 2000000000
#define Pair pair<int,int>
#define eps 1e-8

using namespace std;

int main(){
	int t;
	scanf("%d",&t);
	int su;
	int cse=1;
	while(t--)
	{
		int n,s,p;
		scanf("%d%d%d",&n,&s,&p);
		int sum=0,pc=0;
		rep(i,n)
		{
			scanf("%d",&su);
			if(su<p)
				continue;
			if(su>=3*p-2)
				sum++;
			else if(su==3*p-3 && pc<s)
			{
				pc++;
				sum++;
			}
			else if(su==3*p-4 && pc<s)
			{
				pc++;
				sum++;
			}
		}
		printf("Case #%d: %d\n",cse++,sum);
	}
	return 0;
}
