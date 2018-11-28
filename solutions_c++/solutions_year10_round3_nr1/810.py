#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <cstdlib>
#include <stdlib.h>
#include <stack>
#include <cstdio>
#include <map>
#include <cmath>
#include <time.h>
using namespace std;

#define MAX(a,b) ((a>=b)?a:b)
#define MIN(a,b) ((a<=b)?a:b)
#define ABS(a) ((a<0)?-(a):a)

vector<pair<int,int> > mas;
bool chk(int a,int b)
{
	if(mas[a].first>mas[b].first && mas[a].second<mas[b].second)return true;
	if(mas[a].first<mas[b].first && mas[a].second>mas[b].second)return true;
	return false;
}
int main()
{
	//freopen("in.txt","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("out2.out","w",stdout);
	int T,n,a,b,count;
	scanf("%d",&T);
	for(int t=0;t<T;++t)
	{
		scanf("%d",&n);
		mas.clear(); count=0;
		for(int i=0;i<n;++i)
		{
			scanf("%d %d",&a,&b);
			mas.push_back(make_pair(a,b));
		}
		for(int j=0;j<mas.size();++j)
			for(int i=j+1;i<mas.size();++i)
				if(chk(j,i))++count;
		printf("Case #%d: ",t+1);
		printf("%d\n",count);
	}
	return 0;
}