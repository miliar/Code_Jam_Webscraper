#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
int main()
{
	freopen("A-small-attempt0.in","r",stdin); freopen("A-small-attempt0.out","w",stdout);
	//freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	//freopen("B-small-attempt0.in","r",stdin); freopen("B-small-attempt0.out","w",stdout);
	//freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
	//freopen("C-small-attempt0.in","r",stdin); freopen("C-small-attempt0.out","w",stdout);
	//freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
	int cases;
	scanf("%d",&cases);
	int A,B;
	for(int cas=1;cas<=cases;cas++)
	{
		int N;
		scanf("%d",&N);
		vector<pair<int,int> >grid;
		for(int i=0;i<N;i++)
		{
			scanf("%d%d",&A,&B);
			grid.push_back(make_pair(A,B));
		}
		sort(grid.begin(),grid.end());
		int ans=0;
		for(int i=0;i<grid.size();i++)
		{
			for(int j=i+1;j<grid.size();j++)
				if(grid[j].second<=grid[i].second)
					ans++;
		}
		printf("Case #%d: %d\n",cas,ans);
	}
}

