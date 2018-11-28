#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<iostream>
#include<string.h>
#include<vector>
#include<stack>
#include<queue>
#define eps 1e-11
#define INF (2<<31)-1

using namespace std;

int max(int a, int b) {
	if(a>b) return a;
	return b;
}
int min(int a, int b){
	if(a<b) return a;
	return b;
}

int t, n, or[200], bl[200], T, ct=1;
int turn[1000], po[200], pb[200];

int main()
{
	char c;
	int p, o, b, i, k, res=0;
		freopen("A.in","r",stdin);
		freopen("out.txt","w",stdout);
	scanf("%d", &T);
	while(T--)
	{
		k=0;
		scanf("%d", &n);
		o=b=1;
		po[0]=pb[0]=1;
		bl[0]=or[0]=1;
		for(i=0;i<n;i++)
		{
			scanf("%s", &c);
			scanf("%d", &p);
			if(c=='O')
			{
				turn[i]=0;
				or[o]=abs(po[o-1]-p)+1;
				po[o++]=p;
			}
			else
			{
				turn[i]=1;
				bl[b]=abs(pb[b-1]-p)+1;
				pb[b++]=p;
			}
		}
		o=b=1;
		res=0;
		for(i=0;i<n;i++)
		{
			if(turn[i]==0)
			{
				res+=or[o];
				bl[b]-=min(bl[b]-1, or[o]);
				or[o]=0;
				o++;
			}
			else
			{
				res+=bl[b];
				or[o]-=min(bl[b], or[o]-1);
				bl[b]=0;
				b++;
			}
		}

		printf("Case #%d: %d\n", ct++, res );
	}

	return 0;
	
}
