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
#include <queue>   
#include <map> 
#include <string.h> 
#include <queue> 
using namespace std;


/*  
bool arr[N];  
void getprim(){ arr[0]=1;arr[1]=1;int i;long long j;for(i=2;i<N;i++){if(arr[i]==0){ for(j=i,j=j*i;j<N;j+=i){arr[j]=1;}}}}  
*/  
//priority_queue  
//lower_bound,upper_bound  
//#define vs vector<string>
//#define N 4500005
//#define vi vector<int>
//typedef long long ll;
//next_permutation

//bool cmp(int a,int b)//从小到大
//{
//	return a<b;
//}

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;
int main()
{
    freopen("1.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T,i,j;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++)
	{
		int n,l,h;
		int arr[101];
		scanf("%d %d %d",&n,&l,&h);
		for(i=0;i<n;i++)
		{
			scanf("%d",&arr[i]);
		}
		for(i=l;i<=h;i++)
		{
			for(j=0;j<n;j++)
			{
				if(arr[j]%i==0 || i%arr[j]==0)continue;
				break;
			}
			if(j==n)
			{
				printf("Case #%d: %d\n",cas,i);
				break;
			}
		}
		if(i==h+1)
		{
			printf("Case #%d: NO\n",cas);
		}
	}
	return 0;
}