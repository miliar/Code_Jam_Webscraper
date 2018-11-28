#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int T;
char ch;
vector <char> a;

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	scanf("%d\n", &T);
	for(int t = 1; t <= T; t++)
	{
		scanf("%c", &ch);
		printf("Case #%d: ", t);
		a.clear();
		while(ch >= '0' && ch <= '9')
		{
			a.push_back(ch);
			scanf("%c", &ch);
		}
		if(!next_permutation(a.begin(), a.end()))
		{
			a.push_back('0');
			sort(a.begin(), a.end());
			if(a[0] == '0')
			{
				for(int j = 0; j < a.size(); j++)
					if(a[j] != '0')
					{
						swap(a[j], a[0]);
						break;
					}
			}
			else
				swap(a[1], a[a.size() - 1]);
		}
			for(int i = 0; i < a.size(); i++)
				printf("%c", a[i]);
		printf("\n");
	}
}
