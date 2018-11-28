#include <iostream>
#include <algorithm>
#include <vector>
#include <stdio.h>
using namespace std;
int sum(vector<int> &vec)
{
	int max_size = vec.size();
	int res = 0,total=0;
    for (int i=0;i<max_size;i++)
	{
		res ^= vec[i];
		total += vec[i];
	}
	if (res != 0)
	return 0;
	nth_element(vec.begin(),vec.begin()+1,vec.end());
	return total - vec[0];
}
int main()
{
	vector<int> a;
	int t,n,tmp,res;
	freopen("1.in","r",stdin);
	freopen("2.in","w",stdout);
	scanf("%d",&t);
	for (int i=1;i<=t;i++)
	{
		scanf("%d",&n);
		while (n--) 
		{
			scanf("%d",&tmp);
			a.push_back(tmp);
		}
		res = sum(a);
		if (res == 0)
			printf("Case #%d: NO\n",i);
		else printf("Case #%d: %d\n",i,res);
		a.clear();
	}
  return 0;
}