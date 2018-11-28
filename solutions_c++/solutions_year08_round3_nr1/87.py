#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<functional>

using namespace std;

int P,K,L;
int fre[1002];

int main()
{
	freopen("A-large.in","r", stdin);
	freopen("A-large.out", "w", stdout);
	int numCase;
	long long sum;
	cin >> numCase;
	for(int c=1; c<=numCase; ++c)
	{
		sum = 0;
		scanf("%d %d %d", &P,&K,&L);
		for(int i=0; i<L; ++i)
		{
			scanf("%d", fre+i);
		}
		sort(fre,fre+L,greater<int>());
		for(int i=0; i<L; i++)
		{
			sum += (long long)(i/K+1)*fre[i];
		}
		cout << "Case #" << c << ": " << sum << endl;
	}
	return 0;
}
