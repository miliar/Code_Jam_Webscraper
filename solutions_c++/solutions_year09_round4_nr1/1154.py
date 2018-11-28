#include <stdio.h>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
typedef vector<int> IV;
typedef set<int> IS;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int nt;
	scanf("%d",&nt);
	for (int t=0;t<nt;t++)
	{
		int n;
		scanf("%d",&n);
		char s[45];
		int numbers[45];
		gets(s);
		for (int i=0;i<n;i++)
		{   
			gets(s);
			for (numbers[i]=n-1; numbers[i]>0 && s[numbers[i]]=='0'; numbers[i]--);
		}
		int ans=0;
		for (int i=0;i<n;i++)
			if (numbers[i]>i)
			{
				int k;
				for (k=i+1;numbers[k]>i;k++);
				for (;k>i;k--)
				{
					swap(numbers[k-1],numbers[k]);
					ans++;
				}
			}
		printf("Case #%d: %d\n",t+1,ans);
	}
	return 0;
}
