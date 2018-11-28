#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <memory.h>
using namespace std;

int power[50];
int on[50];

void go(int n)
{
	for(int i = 0; i < n; i++)
		if(power[i] == 1)
		{
			if(on[i] == 0)
				on[i] = 1;
			else
				on[i] = 0;
		};
	int j = 0;
	while(on[j] == 1 && j < n + 1)
	{
		power[++j] = 1;
	}
	j++;
	while(j < n + 1)
	{
		power[j] = 0;
		j++;
	}
}
int main()
{
    freopen("a.in","rt",stdin);
    freopen("a.out","wt",stdout);
	int t,cnt = 1;;
	cin >> t;
    while(t--)
	{
		memset(power,0,sizeof(power));
		memset(on,0,sizeof(on));
		power[0] = 1;	
		int n,k;
		cin >> n >> k;
		for(int i = 0; i < k; i++)
			go(n);
		if(power[n] == 1)
			cout << "Case #"<< cnt++ <<": ON\n";
		else
			cout << "Case #"<< cnt++ <<": OFF\n";
	}
	return 0;
}
