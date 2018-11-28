#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>

using namespace std;

const int N = 128;

int min(int a, int b)
{
	return a < b ? a : b;
}

int max(int a, int b)
{
	return a > b ? a : b;
}

char In[4][128] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi"
				, "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
				, "de kr kd eoya kw aej tysr re ujdr lkgc jv"
				, "y qee"};
				
char Out[4][128] = {"our language is impossible to understand"
				, "there are twenty six factorial possibilities"
				, "so it is okay if you want to just give up"
				, "a zoo"};
				
char map[32];
bool used[32];

void Init()
{
	int i, j;
	for(i = 0; i < 4; i ++)
	{
		for(j = 0; j < strlen(In[i]); j ++)
		if(In[i][j] >= 'a' && In[i][j] <= 'z')
		{
			map[In[i][j]-'a'] = Out[i][j];
			used[Out[i][j]-'a'] = true;
		}
	}
	char ch;
	for(i = 0; i < 26; i ++)
	{
		if(!used[i])
		{
			ch = 'a' + i;
		}
	}
	for(i = 0; i < 26; i ++)
	{
		if(map[i] == '\0')
		{
			map[i] = ch;
		}
	}
}

char Ans[128];

int main()
{
	int i, j, k;
	Init();
	
	int T, cc = 0;
	
	scanf("%d", &T);
	while(T --)
	{
		int N, S, P, t[128];
		scanf("\n");
		gets(Ans);
		for(i = 0; i < strlen(Ans); i ++)
		if(Ans[i] >= 'a' && Ans[i] <= 'z')
		{
			Ans[i] = map[Ans[i]-'a'];
		}
		//puts(Ans);
		printf("Case #%d: %s\n", ++cc, Ans);
	}
	
	return 0;
}
