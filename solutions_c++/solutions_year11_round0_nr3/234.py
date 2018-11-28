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
		int ans=0;
		int n;
		scanf("%d",&n);
		vi num;
		for(int i=0;i<n;++i)
		{
			int now;
			scanf("%d",&now);
			num.push_back(now);
			ans+=now;
		}
		sort(all(num));
		ans-=num[0];
		int check=0;
		for(int i=0;i<n;++i)
			check^=num[i];
		if(check==0)
			printf("Case #%d: %d\n",caseID+1,ans);
		else 
			printf("Case #%d: NO\n",caseID+1);
		
	}
	
	return 0;
}

