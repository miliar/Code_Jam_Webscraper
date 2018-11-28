// zero.lin`s google_codejam.cpp 
//


#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstdlib>
#include <cctype>
#include <cmath>


#include "google_codejam\stdafx.h"
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vii;
typedef long long ll;

#define rep(i,n) for(int i=0;i<n;++i)
#define all(n) n.begin(),n.end()
#define sz(o) (int)(o.size())
#define mset(o,v) memset(o,v,sizeof(o))
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
#define mk(first,second) make_pair(first,second)
#define present(container, element) (container.find(element) != container.end()) 
#define cpresent(container, element) (find(all(container),element) != container.end())

const int inf=1<<28;
const double eps=1e-11;

int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	
	int testcase;
	scanf("%d",&testcase);
	
	rep(caseID,testcase)
	{
		float ans=0;
		int n;
		scanf("%d",&n);
		vi num;
		for(int i=0;i<n;++i)
		{
			int now;
			scanf("%d",&now);
			num.push_back(now);
		}
		vi o(num);
		sort(all(o));
		for(int i=0;i<n;++i)
			if(num[i]!=o[i])
				ans+=1;
		printf("Case #%d: %f\n",caseID+1,ans);
	}
	
	return 0;
}

