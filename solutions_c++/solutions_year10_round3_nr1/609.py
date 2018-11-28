#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef pair<int,int> pii;
typedef long long ll;
const int maxn = 1000+5;
int r;
int line[maxn][2];
int N;
void init()
{
	
}
int solve()
{
	r = 0;
	for(int i=0;i<N;i++)
	{
		for(int j =0;j<N;j++)
		{
			if(i == j) continue;
			if(line[i][0] >line[j][0] && line[i][1] < line[j][1])
			{
				r++;
			}
			if(line[i][0] <line[j][0] && line[i][1] > line[j][1])
			{
				r++;
			}
		}
	}
	r /=2;
	return r;
}

int main()
{
//	freopen("a-test.in","r",stdin);//freopen("a-test.out","w",stdout);
//	freopen("a-small-attempt0.in","r",stdin);freopen("a-small.out","w",stdout);
	freopen("a-large.in","r",stdin);freopen("a-large.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		cin>>N;
		for(int i =0;i<N;i++)cin>>line[i][0]>>line[i][1];
		init();
		solve();
		cout<<"Case #"<<caseId<<": "<<r<<endl;
		
		cerr<<caseId<<"/"<<testcase<<endl;
	}
	return 0;
}












