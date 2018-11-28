//#include <vector>
//#include <list>
//#include <map>
//#include <set>
//#include <deque>
//#include <queue>
//#include <stack>
//#include <bitset>
//#include <algorithm>
//#include <functional>
//#include <numeric>
//#include <utility>
//#include <sstream>
//#include <iostream>
//#include <iomanip>
//#include <cstdio>
//#include <cmath>
//#include <cstdlib>
//#include <cctype>
//#include <string>
//#include <cstring>
//#include <cstdio>
//#include <cmath>
//#include <cstdlib>
//#include <ctime>
//
//using namespace std;
//int main(){
//	int _T;
//	freopen("data_C.txt","r",stdin);
//	freopen("result_C.txt","w",stdout);
//	scanf("%d",&_T);
//	for(int _t=1;_t<=_T;_t++){
//		printf("Case #%d: ",_t);
//
//	}
//	return 0;
//}
#include<iostream>
#include<algorithm>
#include<functional>
#include<sstream>
#include<set>
#include<map>
using namespace std;

#define MAXN 102

int T, N, M;
long long a[MAXN],b[MAXN];
int A[MAXN], B[MAXN];

long long ans;

void dfs(int i, int j, long long sum)
{
	if(i>=N||j>=M)
	{
		if(sum>ans)
		{
			ans = sum;
		}
		return;
	}

	if(A[i]==B[j])
	{
		if(a[i]>b[j])
		{
			a[i]-=b[j];
			dfs(i, j+1, sum+b[j]);
			a[i]+=b[j];
		}
		else// if(a[i]<b[j])
		{
			b[j]-=a[i];
			dfs(i+1, j, sum+a[i]);
			b[j]+=a[i];
		}
	}
	else
	{
		dfs(i, j+1, sum);
		dfs(i+1, j, sum);
	}
}

int main()
{
freopen("data_C.txt","r",stdin);
freopen("Result_C.txt","w",stdout);
	scanf("%d\n", &T);
	for(int te=1;te<=T;++te)
	{
		cin>>N>>M;
		ans = 0;
		for(int i=0;i<N;++i)
		{
			cin>>a[i]>>A[i];
		}
		for(int i=0;i<M;++i)
		{
			cin>>b[i]>>B[i];
		}
		
		dfs(0,0,0);
		printf("Case #%d: %lld\n", te, ans);
	}
	return 0;
}