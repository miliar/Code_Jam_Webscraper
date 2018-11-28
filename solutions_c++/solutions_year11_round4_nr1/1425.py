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
//	return a>b;
//}
struct stu
{
	int len,w;
	bool operator <(const stu &t)const
	{
		return w<t.w;
	}
}arr[2006];
int main()
{
	freopen("1.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,cas;
	scanf("%d",&T);
	for(cas=1;cas<=T;cas++)
	{
		int x,s,r,n,all=0,st,en;
		double t;
		int i;
		scanf("%d %d %d %lf %d",&x,&s,&r,&t,&n);
		for(i=0;i<n;i++)
		{
			scanf("%d %d %d",&st,&en,&arr[i].w);
			all+=en-st;
			arr[i].len=en-st;
		}
		all=x-all;
		if(all!=0)
		{
			arr[n].len=all;
			arr[n].w=0;
			n++;
		}
		sort(arr,arr+n);
		double ans=0;
		for(i=0;i<n;i++)
		{
			double rt=double(arr[i].len)/(arr[i].w+r);
			if(rt>t)
			{
				ans+=t+( double(arr[i].len) - t*(arr[i].w+r) ) / (arr[i].w+s);
				t=0;
			}
			else
			{
				ans+=rt;
				t-=rt;
			}
		}
		printf("Case #%d: %.9lf\n",cas,ans);
	}
	return 0;
}