#include<iostream>
#include<algorithm>
using namespace std;
int c,d,n;
char map1[26][26];
bool map2[26][26];
void init()
{
	int i,j;
	for( i = 0 ; i < 26 ; i ++)
		for(j = 0 ; j < 26 ; j ++)
			map1[i][j] = '\0';
	memset(map2,false,sizeof(map2));
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t;
	scanf("%d",&t);
	int i,j;
	int g = 1;
	while(t--)
	{
		scanf("%d",&c);
		init();
		for( i = 0 ; i < c ; i ++)
		{
			char ch[4];
			scanf("%s",ch);
			map1[ch[0]-'A'][ch[1]-'A'] = ch[2];
			map1[ch[1]-'A'][ch[0]-'A'] = ch[2];
		}
		scanf("%d",&d);
		for( i = 0 ; i < d ; i ++)
		{
			char ch[4];
			scanf("%s",ch);
			map2[ch[0]-'A'][ch[1]-'A'] = true;
			map2[ch[1]-'A'][ch[0]-'A'] = true;
		}
		string now = "";
		scanf("%d",&n);
		char ch[105];
		scanf("%s",ch);
		for( i = 0 ; ch[i] != '\0' ; i ++)
		{
			if(now.size() == 0)
				now += ch[i];
			else
			{

				int a = now[now.size()-1] -'A';
				int b = ch[i] -'A';
				if(map1[a][b] != '\0')
				{
					bool flag =false;
					char x = map1[a][b];
					for( j = 0 ; j < now.size() - 1 ; j ++)
					{
						if(map2[x-'A'][now[j]-'A'])
						{
							now = "";
							flag = true;
							break;
						}
					}
					if( !flag)
						now[now.size()-1] = x;
				}
				else
				{
					bool flag =false;
					for( j = 0 ; j < now.size() ; j ++)
					{
						if(map2[b][now[j]-'A'])
						{
							now = "";
							flag = true;
							break;
						}
					}
					if( !flag)
						now += (char)(b+'A');
				}
			}
		}
		printf("Case #%d: [",g++);
		for( i = 0 ; i < now.size() ; i ++)
		{
			if( i != 0)
				printf(", ");
			printf("%c",now[i]);
		}
		printf("]\n");


	}
	return 0;
}
/*
Case #1: [E, A]
Case #2: [R, I, R]
Case #3: [F, D, T]
Case #4: [Z, E, R, A]
Case #5: []


*/