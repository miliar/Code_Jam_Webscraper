#include <stdio.h>
#include <iostream>
#include <string>
#include <string.h>

using namespace std;

bool f[15][256];
string str[5000];
int l, d, n;

void Init()
{
	scanf("%d %d %d\n", &l, &d, &n);
	int i;
	for(i=0; i<d; i++)
	{
		cin >> str[i];
	}
}

void Build(string temp)
{
	memset(f, false, sizeof(f));
	int i, k;
	for(i=k=0; i<l; i++)
	{
		if(temp[k] != '(')
		{
			f[i][temp[k]] = true;
			k++;
		}
		else
		{
			k++;
			while(temp[k] != ')')
			{
				f[i][temp[k]] = true;
				k++;
			}
			k++;
		}
	}
}

inline bool Test(string s)
{
	int i;
	for(i=0; i<s.length(); i++)
	{
		if(!f[i][s[i]])
			return false;
	}
	return true;
}

void Compute()
{
	int caseno = 0, i;
	string temp;
	for(i=0; i<n; i++)
	{
		int cnt = 0;
		cin >> temp;
		caseno++;
		Build(temp);
		int k;
		for(k=0; k<d; k++)
		{
			if(Test(str[k]))
				cnt++;
		}
		printf("Case #%d: %d\n", caseno, cnt);
	}
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
    Init();
	Compute();
	return 0;
}