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
	freopen("1.txt","w",stdout);
	int T,cas,n,m;
	scanf("%d",&T);
	char str[105][105];
	for(cas=1;cas<=T;cas++)
	{
		scanf("%d",&n);
		int i,j,k;
		double a[105],b[105],c[105];
		for(i=0;i<n;i++)
		{
			scanf("%s",str[i]);
		}
		for(i=0;i<n;i++)
		{
			double fa=0,fb=0;
			for(j=0;j<n;j++)
			{
				if(str[i][j]=='.')continue;
				if(str[i][j]=='1')fa+=1;
				fb+=1;
			}
			if(fb==0)a[i]=0;
			else
				a[i]=fa/fb;
		}
		for(i=0;i<n;i++)
		{
			double fa=0,fb=0,fc,all=0;
			for(j=0;j<n;j++)
			{
				if(str[i][j]=='.')continue;
				fb+=1;
				fc=0;
				fa=0;
				for(k=0;k<n;k++)
				{
					if(k==i)continue;
					if(str[j][k]=='.')continue;
					fc+=1;
					if(str[j][k]=='1')fa+=1;
				}
				if(fc!=0)
				{
					all+=fa/fc;
				}
			}
			if(fb==0)b[i]=0;
			else
				b[i]=all/fb;
		}
		for(i=0;i<n;i++)
		{
			double fa=0,fb=0;
			for(j=0;j<n;j++)
			{
				if(str[i][j]=='.')continue;
				fb+=1;
				fa+=b[j];
			}
			if(fb==0)c[i]=0;
			else
				c[i]=fa/fb;
		}
		printf("Case #%d:\n",cas);
		for(i=0;i<n;i++)
		{
			printf("%.7lf\n",0.25*a[i]+0.5*b[i]+0.25*c[i]);
		}
	}
	return 0;
}