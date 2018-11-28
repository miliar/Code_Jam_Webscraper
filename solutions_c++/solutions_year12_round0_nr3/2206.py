#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>

using namespace std;

int makeRcyc(int num, int limit)
{
	char str[16];

	sprintf(str, "%d", num);

	int cnt = 0;
	int len = strlen(str);
	
	vector<int> v;

	for(int i=0; i<len-1; i++) 
	{
		str[len] = str[0]; 
		str[len+1] = '\0';

		sprintf(str, "%s", &str[1]);

		int rcyc = atoi(str);

		if (rcyc > num && rcyc <= limit) 
		{
			bool isEx = false;

			for(int j=0; j<v.size(); j++) 
			{
				if (v[j] == rcyc) {
					isEx = true;
					break;
				}
			}

			if (isEx) continue;
			
			v.push_back(rcyc);
			cnt++;
		}
	}

	return cnt;
}

int main()
{
	int t;

	scanf("%d", &t);

	for(int a=0; a<t; a++)
	{
		int A, B, ans = 0;

		scanf("%d %d", &A, &B);

		for(int i=A; i<=B; i++) {
			ans += makeRcyc(i, B);
		}
		
		printf("Case #%d: %d\n", a+1, ans);
	}
}
