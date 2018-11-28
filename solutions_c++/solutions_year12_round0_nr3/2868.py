#include <iostream>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <string>
#include <bitset>
#include <map>

#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>

using namespace std;

#define MAX 1010

bool used[MAX][MAX];

int ilen(int n)
{
	int i=0;
	if(n==0) return i;
	while(n)
	{
		i++;
		n/=10;
	}
	return i;
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-out.txt","w",stdout);
	int t,T;
	int i,j,l;
	int n,r,x,a,b;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		cin>>a>>b;
		r=0;
		for(i=a;i<=b;i++)
			for(j=a;j<=b;j++)
				used[i][j]=0;
		l = ilen(a);
		for(i=a;i<b;i++)
		{
			for(j=1;j<l;j++)
			{
				n = i;
				x = i % int(pow(10,j));
				n /= int(pow(10,j));
				n += x*int(pow(10,l-j));
				if(n>=a && n<=b && n!=i)
					if(!used[i][n])
					{
						r++;
						used[i][n]=1;
						used[n][i]=1;
						//printf("%d %d\n",i,n);
					}
			}
		}
		printf("Case #%d: %d\n",t,r);
	}
	return 0;
}





