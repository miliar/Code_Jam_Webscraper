#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream> 
#include <cmath>
#include <cstring>

using namespace std;

#define pb push_back
#define mp make_pair
#define PII pair<int,int> 
#define A first
#define B second
#define PIII pair<int,PII> 

#define I(x,y) x <y> :: iterator 
#define set(a,c) memset(a,c,sizeof(a))

#define REP(i,n) for(int i=0;i<n;i++)

typedef unsigned long long LLU;
typedef long long LL;
typedef long double LD;

bool isprime(int n)
{

	if(n<2)	return 0;
	for(int i=2;i*i<=n;i++)
		if(n%i==0)
			return 0;
	return 1;
}
int p[1001];
int a[1001];
int parent(int x)
{
	if(p[x]==x)
		return x;
	return p[x]=parent(p[x]);
}
void merge(int x,int y)
{
	x = parent(x);
	y = parent(y);
	if(x> y ) 
	{
		int temp = y;
		y =x ;
		x = temp;
	}
	p[y] = x;
}

int main()
{
	int KASES;
	int A,B,P;
	scanf("%d",&KASES);
	for(int kases=0;kases<KASES;kases++)
	{
		printf("Case #%d: ",kases+1);
		scanf("%d %d %d",&A,&B,&P);
		for(int i=A;i<=B;i++)
		{
			p[i] = i;
			a[i]= 0;
		}
		for(int i=P;i<=B;i++)
			if(isprime(i)){
				int j,found = 0;
				for(j=A;j<=B && !found;j++)
					if(j%i==0)
						found=j;
				for(;j<=B;j++)
					if(j%i==0)
						merge(found,j);
			}
		int answer = 0 ;
		for(int i=A;i<=B;i++)
		{
			if(a[parent(i)]==0)
			{
				answer++;
				a[parent(i)] =1;
			}
		}
		printf("%d\n",answer);


	}
}

