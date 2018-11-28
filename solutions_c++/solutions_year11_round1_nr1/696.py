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



int main()
{
	freopen("1.in","r",stdin);
	freopen("out.txt","w",stdout);
	long long d,g,n;
	int T,cas=1,i;
	scanf("%d",&T);
	for(cas=1;cas<=T;cas++)
	{
		cin>>n>>d>>g;
		printf("Case #%d: ",cas);
		
		if( (g==100 && d!=100) || (g==0 && d!=0))
		{
			printf("Broken\n");
			continue;
		}
		if(n>=100)
		{
			printf("Possible");
		}
		else
		{
			for(i=1;i<=n;i++)
			{
				double ans=i;
				ans=i*d;
				ans/=100;
				if(ans-int(ans)==0)
				{
					printf("Possible");
					break;
				}
			}
			if(i==n+1)
			{
				printf("Broken");
			}
		}
		printf("\n");
	}
	return 0;
}
			