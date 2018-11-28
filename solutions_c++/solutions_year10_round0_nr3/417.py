#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <utility>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <queue>
#include<iostream>
#define FALSE 0
#define TRUE 1
using namespace std;
typedef long long ll;
typedef pair<int,int> ipair;
#define SIZEARRAY(x) (sizeof(x)/sizeof(x[0]))
template<typename T>
T Euclid(T a,T b,T &x,T &y)
{
	if(a<0)
	{
		T d = Euclid(-a,b,x,y);
		x = -x;
		return d;
	}
	else if (b < 0)
	{
		T d= Euclid(a,-b,x,y);
		y = -y;
		return d;
	}
	else
	{
		if (a<b)
		{
			swap(a,b);
		}
		if (b == 0)
		{
			x = 1;
			y = 0;
			return a;
		}
		else
		{
			T d = Euclid(b,a%b,x,y);
			T t = x;
			x = y;
			y = t-(a/b)*y;
			return d;
		}
	}
}

int main()
{
	freopen("F:\\code\\topcoder\\C-large.in","r",stdin);
	freopen("F:\\code\\topcoder\\testout.txt","w",stdout);
	int caseNum;
	cin>>caseNum;
	int nowCase = 0;
	int R,K,N;
	int nums[1005];
	ll sums[1005];
	int next[1005];
	while(nowCase++<caseNum)
	{
		cerr<<nowCase<<endl;
		cin>>R>>K>>N;
		for (int i = 0;i<N;i++)
		{
			scanf("%d",nums+i);
		}
		ll tempSum = 0;
		for (int i = 0;i<N;i++)
		{
			tempSum+=nums[i];
		}
		if (tempSum<=K)
		{
			sums[0] = tempSum;
			next[0] = 0;
		}
		else
		{
			tempSum = 0;
			for (int i = 0;i<N;i++)
			{
				tempSum+=nums[i];
				if (tempSum>K)
				{
					tempSum-=nums[i];
					sums[0] = tempSum;
					next[0] = i;
					break;
				}
			}
			for (int i = 1;i<N;i++)
			{
				tempSum = sums[i-1]-nums[i-1];
				for (int j = next[i-1];;j++,j%=N)
				{
					tempSum+=nums[j];
					if (tempSum>K)
					{
						tempSum-=nums[j];
						sums[i] = tempSum;
						next[i] = j;
						break;
					}
				}
			}
		}
		ll res = 0;
		int start = 0;
		for (int i = 0;i<R;i++)
		{
			res+=sums[start];
			start = next[start];
		}
		cout << "Case #"<<nowCase<<": ";
		cout << res<<endl;
	}
}