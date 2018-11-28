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
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
struct Next
{
	int index;
	int cost;
};
int main()
{
	if(freopen("C-small-attempt0.in", "r", stdin))
	freopen("C-small.out", "w", stdout);
	int T;
	cin>>T;
	int num=0;
	while(num++!=T)
	{
		int R;
		int k;
		int N;
		cin>>R>>k>>N;
		vector<int> Queue;
		int x;
		while(N--)
		{
			cin>>x;
			Queue.push_back(x);
		}
		vector<Next> Bank;
		int size=Queue.size();
		if(k>=accumulate(Queue.begin(),Queue.end(),0))
		{
			Next temp;
			temp.cost=accumulate(Queue.begin(),Queue.end(),0);
			temp.index=0;
			Bank.push_back(temp);
		}
		else
		{
			for(int i=0;i<size;i++)    //包含Queue.size（）这么多个元素
			{
				Next temp;
				int total=Queue[i];

				for(int j=i+1;(j%size)<size;j++) //遍历生成一个temp
				{
					if(total+Queue[j%size]>k)
					{
						temp.cost=total;
						temp.index=j%size;
						Bank.push_back(temp);
						break;
					}
					else
						total+=Queue[j%size];

				}

			}
		}
		int result=0;
		int y=0;
		/*for(int i=0;i<Bank.size();i++)
		{
			cout<<Bank[i].cost<<" "<<Bank[i].index<<endl; 
		}*/
		for(int i=0;i<R;i++)
		{
			result+=Bank[y].cost;
			y=Bank[y].index;
		}
		cout<<"Case #"<<num<<": "<<result<<endl;
	}
	return 0;
}
