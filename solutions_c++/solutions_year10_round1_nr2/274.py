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
#include <ctime>

using namespace std;

int dp[255+10][100+10];
int a[100+10];
int D,I,M,N;
const int oo = 1000000000;

void checkmin(int &a,int b){if(b<a)a=b;}

int solve(int pre,int index)
{
	if(index==N)return 0;
	if(dp[pre][index]!=-1)return dp[pre][index];
	int &ret = dp[pre][index];
	ret = oo;
	//delete
	checkmin(ret,D+solve(pre,index+1));
	//change value
	for(int i=0;i<256;i++)
	{
		int tmp = abs(a[index]-i);
		if(pre!=i && M==0)continue;
		if(abs(pre-i)>M)
			tmp += (abs(pre-i)/M+(abs(pre-i)%M==0?-1:0))*I;
		checkmin(ret,tmp+solve(i,index+1));
	}
	return ret;
}
int main()
{
	//freopen("B-small-attempt0.in","r",stdin);freopen("B-small-output.txt","w",stdout);
	//freopen("B-small-attempt3.in","r",stdin);freopen("B-small-output.txt","w",stdout);
	freopen("B-large.in","r",stdin);freopen("B-large-output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int Case=1;Case<=T;Case++)
	{
		
		scanf("%d %d %d %d",&D,&I,&M,&N);
		int i,j;
		for(i=0;i<N;i++)
			scanf("%d",&a[i]);
		
		int ret = oo;
		memset(dp,-1,sizeof(dp));
// 		if(M==0)
// 		{
// 			sort(a,a+N);
// 			int maxN = 0;
// 			int tmp = 1;
// 			for(i=1;i<N;i++)
// 			{
// 				if(a[i]==a[i-1])
// 					tmp++;
// 				else
// 				{
// 					if(tmp>maxN)
// 						maxN=tmp;
// 					tmp=1;
// 				}
// 			}
// 			if(tmp>maxN)maxN=tmp;
// 			ret = D*(N-tmp);
// 		}else
		for(i=0;i<256;i++)
			checkmin(ret,solve(i,0));
		printf("Case #%d: %d\n",Case,ret);
	}
}
