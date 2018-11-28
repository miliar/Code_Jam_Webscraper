#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>

using namespace std;

const int INF = 2147483647;
const int MAXN = 20005;
int T, N, M;

char s1[MAXN];
char s2[MAXN];
int MAP[100]={24,7,4,18,14,2,21,23,3,20,8,6,11,1,10,17,25,19,13,22,9,15,5,12,0,'q'-'a'};
//int MAP[100];
int main()
{
	//memset(MAP,-1, sizeof(MAP));
	//for(int i = 1;i <= 3;++i)
	//{
	///	gets(s1);
	//	gets(s2);
	//	printf("%s\n%s\n", s1, s2);
	//	int len = strlen(s1);
	//	for(int j = 0;j < len;++j)
	//	{
	//		MAP[s1[j]-'a'] = s2[j]-'a';
	//	}
	//}
	//for(int i = 0;i < 26;++i)
	//{
	//	printf("%c->%d\n", i+'a', MAP[i]);
	//}
	//freopen("out.txt", "w", stdout);
	scanf("%d\n", &T);
	for(int t = 1;t <= T;++t)
	{
		gets(s1);
		int len = strlen(s1);
		for(int i = 0;i < len;++i)
		{
			if(s1[i] >= 'a' && s1[i] <= 'z')
			{
				s1[i] = 'a' + MAP[s1[i]-'a'];
			}
		}
		printf("Case #%d: %s\n",t, s1);
	}
	return 0;
}

