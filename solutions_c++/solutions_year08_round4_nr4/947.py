#include <iostream>
#include <math.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>

using namespace std;
string S,SP;

int judge()
{
	int len = SP.length();
	int ans = 1;
	for(int i = 1; i< len; ++i)
	{
		if(SP[i] == SP[i-1])
		{
		}
		else ans ++;
	}
	return ans;
}

int main()
{
	int N;
	int K;
	cin >> N;
	int p[5];
	char ch[1001];
	int t = 1;
	while(N--)
	{
		scanf("%d %s",&K,ch);
		S = ch;
		SP = S;
		for(int i = 0; i< K; ++i) p[i] = i+1;
		int T = S.length()/K;
		int Min = 100001;
		do
		{
			for(int j = 0; j< T; ++j)
			{
				for(int k = 0; k< K; ++k)
				{
					SP[j*K+k] = S[j*K+p[k]-1];
				}
			}
			int tt = judge();
			if(Min > tt) Min = tt;
		}while(next_permutation(p,p+K));
		printf("Case #%d: %d\n",t++,Min);
	}
	return 0;
}
