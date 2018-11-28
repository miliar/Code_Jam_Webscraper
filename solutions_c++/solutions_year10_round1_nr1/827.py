#include <iostream>
#include <string>
#include <math.h>
#include <vector>
#include <algorithm>
using namespace std;

const int MAX = 55;

int a, b, kk;
char ch[MAX][MAX];

void ro()
{
	char t[MAX][MAX];
	for(int i = 0; i < a; i++)  for(int j = 0; j < b; j++)
		t[j][a - 1 - i] = ch[i][j];
	for(int i = 0; i < b; i++)  
	{
		for(int j = 0; j < a; j++)
			ch[i][j] = t[i][j];
	}
}

int judge(char x)
{
	for(int i = 0; i < a; i++)
	{
		for(int j = 0; j < a; j++)
		{
			int k;
			for(k = 0; k < kk; k++)
			{
				if(i + k >= a || j + k >= a)  break;
				if(ch[i + k][j + k] != x)  break;
			}
			if(k >= kk)  return 1;
			for(k = 0; k < kk; k++)
			{
				if(i >= a || j + k >= a)  break;
				if(ch[i][j + k] != x)  break;
			}		
			if(k >= kk)  return 1;
			for(k = 0; k < kk; k++)
			{
				if(i + k >= a || j >= a)  break;
				if(ch[i + k][j] != x)  break;
			}
			if(k >= kk)  return 1;
			for(k = 0; k < kk; k++)
			{
				if(i - k < 0 || j + k >= a)  break;
				if(ch[i - k][j + k] != x)  break;
			}
			if(k >= kk)  return 1;
		}
	}
	return 0;
}

void go()
{
	for(int i = 0; i < a; i++)
	{
		for(int j = 0; j < a; j++)
		{
			for(int k = 0; k < a - 1; k++)
			{
				if(ch[i][k] != '.' && ch[i][k + 1] == '.')
					swap(ch[i][k], ch[i][k + 1]);
			}
		}
	}
	ro();
	int r = judge('R');
	int b = judge('B');
	if(r && b)  printf("Both\n");
	else if(r)  printf("Red\n");
	else if(b)  printf("Blue\n");
	else  printf("Neither\n");
}

int main()
{
	freopen("d:\\A-large.in", "r", stdin);
	freopen("d:\\A-large.out", "w", stdout);

	int T, c = 0;
	scanf("%d", &T);
	while(T--)
	{
		scanf("%d%d", &a, &kk);
		b = a;
		for(int i = 0; i < a; i++)  scanf("%s", &ch[i]);
		printf("Case #%d: ", ++c);
		go();
	}
}
