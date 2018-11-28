#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <deque>
#include <cstdlib>
#define MAX 1000001
#define MAX2 10000001
using namespace std;
int t1[MAX];
int t2[MAX];
int t3[MAX];
bool f1(int a,int b)  
{
	return t1[a]<t1[b];
}
int main()
{
	int t,n,m,a,b,c,d,i,j,k,u,v,w,x,y,z,e,f,g,h,l,o,p,r,s;
	scanf("%d", &t);
	for(z=1;z<=t;z++)
	{
	
	k=0;
		scanf("%d", &n);
	
	for(i=0;i<n;i++)
	{
		scanf("%d %d", &a, &b);
		t1[i]=a;
		t2[i]=b;
		t3[i]=i;	
	}
	
	sort(t3,t3+n,f1);
	
	for(i=0;i<(n-1);i++)
	{
		for(j=i+1;j<n;j++)
		{
			if(t2[t3[i]]>t2[t3[j]]) k++;		
		}		
	}
		
		
		printf("Case #%d: %d\n", z, k);
	}	
	return 0;
}
