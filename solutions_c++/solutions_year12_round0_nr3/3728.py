#include<stdio.h>
#include<set>
#include<stdlib.h>
#include<math.h>
#include<utility>

using namespace std;

int digit(int x)
{
	int count = 0;
	while(x > 0){
		count++;
		x /= 10;
	}
	return count;
}

int shiftRight(int x,int len,int n)
{
	if(n >= len)
		return -1;
	int base = pow(10,n);
	int rest = x%base;
	int next = x/base + pow(10,len-n)*rest;
	if(next > x)
		return next;
	return -1;
}

int main()
{
	int T;
	int A,B;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		scanf("%d %d",&A,&B);
		int count = 0;
		for(int i=A;i<=B;i++)
		{
			int len = digit(i);
			set<int> same;
			for(int j=1;j<len;j++)
			{
				int m = shiftRight(i,len,j);
				if(m == -1) continue;
				if(digit(m) == len)
				{
					if(m <= B)
					{
						same.insert(m);
					}
				}
			}
			count += same.size();
		}
		printf("Case #%d: %d\n",t,count);
	}
	return 0;
}
