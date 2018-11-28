#include<iostream>
#include<map>
#include<vector>
#include<stdio.h>

using namespace std;

char car[] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};

map<char, int> ind;

bool opp[8][8];

void init(bool a[][8])
{
	int i,j;
	for (i = 0; i < 8; i++) for (j = 0; j < 8; j++) a[i][j] = 0;
	return;
}

void cas(int t)
{
	init(opp);

	int c, d, n, i, j, k;

	scanf("%d", &c);
	
	map<string, char> m;

	char s[100];
	char ch;

	for (i = 0; i < c; i++)
	{
		scanf("%s", s);
		ch = s[2];
		s[2] = '\0';
		m[s] = ch;
		s[0] = s[0]^s[1];
		s[1] = s[0]^s[1];
		s[0] = s[0]^s[1];
		m[s] = ch;
	}

	scanf("%d", &d);
	
	for (i = 0; i < d; i++)
	{
		scanf("%s", s);
		
		opp[ind[s[0]]-1][ind[s[1]]-1] = opp[ind[s[1]]-1][ind[s[0]]-1] = 1;
	}
	scanf("%d%s", &n, s);
	vector<bool> flag(n, true);
	char temp[2];
	temp[2] = '\0';
	for (i = 0; i < n;)
	{
		if (ind[s[i]])
		{
			for (j = i-1; j >= 0; j--)
			{
				if(flag[j] && ind[s[j]] && opp[ind[s[i]]-1][ind[s[j]]-1])
				{
					for (k = i; k >= 0; k--) flag[k] = false;
					i++;
					break;
				}
			}
		}
		if (i < n-1)
		{
			temp[0] = s[i];
			temp[1] = s[i+1];
			if (m[temp]) 
			{
				s[i+1] = m[temp];
				flag[i] = false;
				i++;	
			}
		}
		i++;
	}
	printf("Case #%d: [", t);
	for (i = 0; i < n; i++)
	{
		if (flag[i]) 
		{
			printf("%c", s[i]);
			if(i != (n-1)) printf(", ");
		}
	}
	printf("]\n");
	return;
}

int main()
{
	int t, i;
	
	for (i = 0; i < 8; i++)
		ind[car[i]] = i+1;
	
	scanf("%d", &t);
	
	for (i = 1; i <= t; i++)
		cas(i);
	return 0;
}
