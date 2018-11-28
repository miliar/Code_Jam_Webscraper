#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int r, k, n;
int size[1001];

pair<int, int> cycleLength()
{
	int i = 0;
	int length = 0;
	int cur = 0;
	int sum = 0;
	
	while(i%n != 0 || length == 0)
	{
		printf("%d\n", i%n);
		cur = 0;
		while(cur + size[i%n] <= k)
		{
			cur += size[i%n];
			i++;
		}
		sum += cur;
		length++;
	}
	return make_pair(length, sum);
}



int main()
{
	freopen("C-small-attempt0.in.txt", "r", stdin);
	
	int nbCases;
	scanf("%d", &nbCases);
	for(int c = 1; c <= nbCases; c++)
	{
		scanf("%d%d%d", &r, &k, &n);
		for(int i =0;i < n; i++)
			scanf("%d", &size[i]);
		//pair<int,int> p = cycleLength();
		//int l = p.first;
		//int s = p.second;
		
		int res = 0;
		
		//while(l <= r)
		//{
			//res += s;
			//r -= l;
		//}
		int i = 0;
		for(int j = 0; j < r; j++)
		{
			int cur = 0;
			int start = i%n;
			bool first = true;
			while(cur + size[i%n] <= k && (start != i%n || first))
			{
				cur += size[i%n];
				i++;
				first = false;
			}
			res += cur;
		}
		
		printf("Case #%d: %d\n", c, res);	
	}
	
	return 0;
}