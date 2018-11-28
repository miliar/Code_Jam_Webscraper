#include <iostream>
#include <stdlib.h>
using namespace std;

struct node{
	int a;
	int b;
} wire[1002];

int n;

int func()
{
	int num;
	int i, j;

	if (n == 1)
	{
		return 0;
	}
	num = 0;
	for (i = 0; i < n-1; i++)
	{
		for (j = i+1; j < n; j++)
		{
			if ((wire[i].a - wire[j].a) * (wire[i].b - wire[j].b) < 0)
			{
				num++;
			}
		}
	}
	return num;
}

int main()
{
	//freopen("A-large.in", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int t;
	int i, j, result;
	cin>>t;
	for(j = 1; j <= t; j++)
	{
		cin>>n;
		for (i = 0; i < n; i++)
		{
			cin>>wire[i].a>>wire[i].b;
		}
		
		result = func();
		cout<<"Case #"<<j<<": "<<result<<endl;
	}
	return 0;
}