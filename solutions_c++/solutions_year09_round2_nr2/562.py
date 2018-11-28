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

int main()
{
	freopen("bin.txt","r",stdin);
	freopen("bout.txt","w",stdout);
	char num[25];
	int T;
	scanf("%d",&T);
	getchar();
	int i;
	vector <int>nums;
	for(i=1;i<=T;i++)
	{
		nums.clear();
		gets(num);
		for(int j=0;j<strlen(num);j++)
		{
			nums.push_back(num[j]-'0');
		}
		for(j--;j>0;j--)
		{
			if(nums[j-1]<nums[j])
				break;
		}
		if(j==0)
		{
			sort(nums.begin(),nums.end());
			int k=0;
			for(k=0;k<nums.size();k++)
				if(nums[k]!=0)
					break;
			int tmp = nums[k];
			nums.erase(nums.begin()+k);
			nums.insert(nums.begin(),0);
			nums.insert(nums.begin(),tmp);
		}else
		{
			int k=j;
			int min=nums[j];
			int mark = j;
			for(k=j;k<nums.size();k++)
			{
				if(nums[k]>nums[j-1] && nums[k]<min)
				{
					min = nums[k];
					mark = k;
				}
			}
			int tmp = nums[mark];
			nums[mark] = nums[j-1];
			nums[j-1] = min;
			sort(nums.begin()+j,nums.end());
		}
		int m=0;
		for(m=0;m<nums.size();m++)
			num[m] = nums[m]+'0';
		num[m] = '\0';
		printf("Case #%d: %s\n",i,num);
	}
	return 0;
}