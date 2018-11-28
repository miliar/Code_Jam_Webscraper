#include <iostream>
#include <cstdio>
#include <algorithm>
#define MAXLENGTH  40
using namespace std;

int result;
int cnt;

int ugly(long long sum, long long before, int signal, char* tail)
{
//	printf("%d : %d %d %s\n", cnt, sum, before, tail);
	if( strlen(tail)==0 )
	{
		cnt++;
		sum += before * signal;
		if( sum%2==0 || sum%3==0 || sum%5==0 || sum%7==0 )
		{
//			printf("%d : find ugly : %d\n", cnt, sum);
			result++;
		}
		else
		{
//			printf("%d : not ugly : %d\n", cnt, sum);
		}
	}
	else
	{
		ugly(sum + before*signal, tail[0]-'0', 1, tail+1);
		ugly(sum + before*signal, tail[0]-'0', -1, tail+1);
		ugly(sum, before*10 + tail[0]-'0', signal, tail+1);
	}
}

int main()
{
	int i, j;
	int t, T;
	int length;
	char input[MAXLENGTH+1];

	scanf("%d", &T);

	for(t=1;t<=T;t++)
	{
		scanf("%s", input);

		length = strlen(input);
		result = 0;
		cnt = 0;
		ugly(0, input[0]-'0', 1, input+1);
		printf("Case #%d: %d\n", t, result);
	}
	return 0;
}

