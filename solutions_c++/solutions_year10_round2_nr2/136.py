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
using namespace std;
#pragma comment(linker, "/STACK:20000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "B-large";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
  freopen((problem_name+".out").c_str(),"wt",stdout);
}

int main()
{

	init();

	int tst;
	scanf("%d\n",&tst);
	for (int cas=1;cas<=tst;cas++)
	{
		int n,k,b,t;
		scanf("%d%d%d%d",&n,&k,&b,&t);
		pair <int ,int> mas[1010];
		for (int i=0;i<n;i++)
			scanf("%d",&mas[i].first);
		for (int i=0;i<n;i++)
			scanf("%d",&mas[i].second);
		//sort(mas,mas+n);
		long long  c=0;
		int res=0;
		for (int i=n-1;i>=0;i--)
		{
			if (k==0) break;
			if ( mas[i].second*(long long)t>= (b-mas[i].first))			
			{
				k--;
				res+=c;			
			} else 
				c++;
		}

		if (k!=0) printf("Case #%d: IMPOSSIBLE\n",cas); else
		printf("Case #%d: %d\n",cas,res);
	}
	
	
	

  return 0;
}
