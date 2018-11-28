#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

	
int t;
int cal[19][550];
char word[] = "welcome to code jam";

int main()
{
	int s = strlen(word);
//	freopen("in.txt", "r", stdin);
	int n;
	scanf("%d", &n);
	int count = 1;
	char buf[1000];
	fgets(buf, 1000, stdin);
	while(n)
	{
		int t;
		fgets(buf, 1000, stdin);
		t = strlen(buf);
		int c=0;
		for(int i=0;i<t;++i)
		{
			if(buf[i] == word[0]) ++c;
			cal[0][i] = c;
		}

		for(int i=1;i<s;++i)
		{
			c = 0;
			for(int j=1;j<t;++j)
			{
				cal[i][j] = cal[i][j-1];
				if(buf[j] == word[i])
				{
					cal[i][j] += cal[i-1][j-1];
					cal[i][j] %= 10000;
				}
			}

		}

		cal[s-1][t-1] %= 10000;
		char pbuf[5];
		sprintf(pbuf, "%4d", cal[s-1][t-1]);
		for(int i=0;i<4;++i)
			if(pbuf[i] == 32) pbuf[i] = '0';

		printf("Case #%d: %s\n", count, pbuf);	
		--n;
		++count;
	}
	return 0;
}
