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

int q[9];

int main()
{
	int i, t, a, b, n, c=1;
	for(i=2,q[1]=1; i<=8; i++)
		q[i] = q[i-1]*10;
	cin >> t;
	while(t--)
	{
		int ans=0;
		cin >> a >> b;
		int s = 1;
		for(i=a; i<=b; i++)
		{
			while(i>=q[s+1])
				s++;
			int x=i%10*q[s]+i/10;
			while(x!=i)
			{
				//cout<<x<<endl;
				if(x>=a && x<=b && x>i)
					ans++;
				x=x%10*q[s]+x/10;
			}
		}
		printf("Case #%d: %d\n", c++, ans);
	}
}
