#include <functional>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <string>
#include <vector>
#include <cstdio>
#include <bitset>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;
typedef unsigned long long uint64;
typedef long long int64;
#define eps 1e-9
#define pi 3.1415926535897932384626433832795
#define MAX 10005

int N;
int L,H;
int data[MAX];
int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("B-large.in","r",stdin);
	//freopen("C-small-attempt1.in","r",stdin);
	//freopen("out.txt","w",stdout);
	int T,testcase=1;
	scanf("%d",&T);
	
	while(T--)
	{
		printf("Case #%d: ",testcase++);
		scanf("%d%d%d",&N,&L,&H);
		for(int i=0;i<N;i++)
			scanf("%d",&data[i]);
		if(L==1)
		{
			printf("1\n");
			continue;
		}
		int i;
		int j;
		bool flag=false;
		for(i=L;i<=H;i++)
		{
			for(j=0;j<N;j++)
			{
				if(i>data[j] && i%data[j]!=0)break;
				if(i<=data[j] && data[j]%i!=0)break;
			}
			if(j==N)
			{
				flag=true;break;
			}
		}
		if(flag)
			printf("%d\n",i);
		else
			printf("NO\n");
	}
	return 0;
}