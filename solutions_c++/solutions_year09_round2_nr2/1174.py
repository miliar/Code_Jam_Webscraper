#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

void solve(void)
{
	char c;
	int i = 0;
	int a[30];
	scanf("%c", &c);
	while (c != '\n')
	{
		a[i] = c - '0';
		i++;
		scanf("%c", &c);
	}
	int length = i;
	if (!next_permutation(a, a + length))
	{
		for (i = length; i > 0; i--)
			a[i] = a[i - 1];
		length++;
		for (i = 1; i < length; i++)
			if (a[i] != 0)
			{
				a[0] = a[i];
				a[i] = 0;
				break;
			}
	}
	for (i = 0; i < length; i++)
		cout << a[i];
}

int main (void) 
{
	//freopen("input1.txt", "r", stdin);
	//freopen("B-small-attempt2.in", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("output1.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	char c;
	scanf("%c", &c);
	for (int i = 0; i < t; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
}