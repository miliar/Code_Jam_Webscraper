#include <string>
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <string.h>

using namespace std;

int main()
{
	freopen("f:\\C-large.in", "r", stdin);
	freopen("f:\\C-large.out", "w", stdout);

	int T, c = 0;
	scanf("%d", &T);
	while(T--)
	{
		int N, m_min = 1e7, sum = 0, m_or = 0;
		scanf("%d", &N);
		for(int i = 0; i < N; i++)
		{
			int t;
			scanf("%d", &t);

			m_min = min(m_min, t);
			sum += t;

			m_or ^= t;
		}

		printf("Case #%d: ", ++c);
		if(m_or)  printf("NO\n");
		else  printf("%d\n", sum - m_min);
	}
}