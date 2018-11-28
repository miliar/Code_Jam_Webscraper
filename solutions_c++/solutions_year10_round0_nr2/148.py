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
	freopen("F:\\code\\topcoder\\B-small-attempt0.in","r",stdin);
	freopen("F:\\code\\topcoder\\testout.txt","w",stdout);
	int caseNum;
	cin>>caseNum;
	int N;
	int nums[1000];
	for (int i = 0;i<caseNum;i++)
	{
		cin>>N;
		for (int i = 0;i<N;i++)
		{
			cin>>nums[i];
		}
		int x,y;
		int divNum;
		divNum = abs(nums[1]-nums[0]);
		for (int j = 2;j<N;j++)
		{
			divNum = Euclid(abs(nums[j]-nums[j-1]),divNum,x,y);
		}
		cout << "Case #"<<i+1<<": ";
		int temp = nums[0]%divNum;
		if (temp != 0)
		{
			temp = divNum-temp;
		}
		cout<<temp<<endl;
	}

	return 0;
}