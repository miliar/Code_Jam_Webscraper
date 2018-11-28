#include<iostream>
#include<queue>
#include<map>
#include<cstring>
using namespace std;

map<string, int> Map;
bool F[110];
string Q[1010];

string Name()
{
	string s;
	char ch;
	while((ch = getchar()) != '\n')
		s += ch;
	return s;
}

int main()
{
	freopen("A_L.in", "r", stdin);
	freopen("A_L.out", "w", stdout);
	int T, i, n, N, k = 0, res;
	scanf("%d", &T);
	while (T--)
	{
		++k;
		Map.clear();
		scanf("%d", &N);
		getchar();
		for (i = 0; i < N; ++i)
			Map[Name()] = i;
		cin>>n;
		getchar();
		for (i = 0; i < n; ++i)
			Q[i] = Name();
		i = res = 0;
		while (i < n && (!Map.count(Q[i]))) ++i;
		int tmp = Map[Q[i]];
		--i;
		while(n - i)
		{
			i++;
			while (i < n && Map[Q[i]] != tmp) ++i;
			memset(F, 0, sizeof(F));
			int t = 0;
			while ( t < N && i < n)
			{
				if(Map.count(Q[i]))
				if(!F[Map[Q[i]]])
				{
					F[Map[Q[i]]] = 1;
					++t;
					if (!(t - N))
					{
						tmp = Map[Q[i]];
						break;
					}
				}
				i++;
			}
			if(t == N)
				--i;
			++res;
		}
		printf("Case #%d: %d\n", k, res - 1);
	}
}
/*
10
5
Yeehaw
NSM
Dont Ask
B9
Googol
10
Yeehaw
Yeehaw
Googol
B9
Googol
NSM
B9
NSM
Dont Ask
Googol
5
Yeehaw
NSM
Dont Ask
B9
Googol
7
Googol
Dont Ask
NSM
NSM
Yeehaw
Yeehaw
Googol
*/
