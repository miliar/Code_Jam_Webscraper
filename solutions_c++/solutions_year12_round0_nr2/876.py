#include<iostream>
#include<map>
#include<math.h>
#include<vector>
#include<string>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
typedef long long ll;
typedef vector<int>::iterator iv;
typedef map<string,int>::iterator im;

int a[100];

int f(int n, bool q)
{
	if(q)
		return n/3+(n%3!=0);
	else
		return n/3+1+(n%3==2);
}

int main()
{
	int t, n, s, p, c=1, i;
	cin >> t;
	while(t--)
	{
		cin >> n >> s >> p;
		int ans=0;
		for(int i=0; i<n; i++)
		{
			cin >> a[i];
			if(f(a[i], 1)>=p)
				ans++;
			else if((a[i]!=1&&a[i]!=0)&& s && f(a[i], 0)>=p)
				s--, ans++;
		}
		printf("Case #%d: %d\n", c++, ans);
	}
}
