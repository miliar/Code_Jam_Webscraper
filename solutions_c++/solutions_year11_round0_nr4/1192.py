#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <map>

#define FOR(i, s, e) for(int i=s; i<e; i++)
#define INP(arr) for(int i=0; i<arr.size(); i++) cin >> arr[i];

using namespace std;

int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w+", stdout);
	int t, n, x;
	cin >> t;
	
	for(int l=1; l<=t; l++)
	{
		cin >> n;
		int* a=new int[n+1];
		for(int i=1; i<=n; i++)
			scanf("%d", a+i);
		
		int k=1, s=0, p=n, temp, sum=0;
		while(p)
		{
			while(a[k]==0) k++;
			s=1;
			x=a[k];
			a[k]=0;
			p--;
			
			while(a[x])
			{
				temp=a[x];
				a[x]=0;
				s++;
				x = temp;
				p--;
				
			}
			if(s>1) sum+=s;
			
		}
		printf("Case #%d: %d.000000\n", l, sum);		
	}
	return 0;
}
