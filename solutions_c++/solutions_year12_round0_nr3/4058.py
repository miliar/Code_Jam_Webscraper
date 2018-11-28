#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
using namespace std;

int GetBits(int n)
{
	int bit = 0;
	while(n)
	{
		n /= 10;
		bit++;
	}
	return bit;
}

int pow10(int k)
{
	int i;
	int ans = 1;
	for(i = 1; i <= k; i++)
		ans *= 10;
	return ans;
}

int Rotate(int n,int k,int bit)
{
	int bis = pow10(bit-k);
	int left = n / bis;
	int right = n % bis;
	return right*pow10(k) + left;
}



int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
    int t,A,B,i,j,Case = 1;
    scanf("%d",&t);
    while(t--)
    {
		int ans = 0;
		scanf("%d %d",&A,&B);
		int bit = GetBits(A);
		for(i = A; i < B; i++)
		{
			for(j = 1; j <= bit-1; j++)
			{
				int cur = Rotate(i,j,bit);
				
				if(cur > i && cur <= B)
				{
					ans++;
				}
			}
		}
		printf("Case #%d: %d\n",Case++,ans);
    }
    return 0;
}

