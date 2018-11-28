#include<cstdio>
#include<string>

using namespace std;

struct node{
	string val;
	int next[128];
}pool[20000];

int cnt;

int insert(string v, int &cur)
{
	int i;
	for(i = 0; i < 128; i ++)
	{
		if(pool[cur].next[i] == 0)
		{
			pool[cur].next[i] = ++cnt;
			pool[cnt].val = v;
			memset(pool[cnt].next, 0, sizeof(int)*128);
			cur = cnt;
			break;
		}
		if(v == pool[pool[cur].next[i]].val)
		{
			cur = pool[cur].next[i];
			return 0;
		}
	}
	return 1;
}

int main()
{
	int T, cas;
	scanf("%d", &T);
	for(cas = 1; cas <=T; cas ++)
	{
		int N, M;
		int i, j, cur, ans;
		char s[128];
		string rec;
		scanf("%d %d", &N, &M);
		cnt = 0;
		memset(pool[0].next, 0, sizeof(int)*128);
		for(i = 0; i < N; i ++)
		{
			scanf("%s", s);
			cur = 0;
			rec = "";
			for(j = 1; s[j] != '\0'; j ++)
			{
				if(s[j] == '/')
				{
					if(rec != "")
					{
						insert(rec, cur);
						rec = "";
					}
				}
				else {
					rec += s[j];
				}
			}
			if(rec != "")
			{
				insert(rec, cur);
				rec = "";
			}
		}
		ans = 0;
		for(i = 0; i < M; i ++)
		{
			scanf("%s", s);
			cur = 0;
			rec = "";
			for(j = 1; s[j] != '\0'; j ++)
			{
				if(s[j] == '/')
				{
					if(rec != "")
					{
						ans += insert(rec, cur);
						rec = "";
					}
				}
				else {
					rec += s[j];
				}
			}
			if(rec != "")
			{
				ans += insert(rec, cur);
				rec = "";
			}
		}
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}
