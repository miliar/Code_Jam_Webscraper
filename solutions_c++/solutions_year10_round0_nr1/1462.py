#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <cctype>
#include <algorithm>
#include <vector>
#include <numeric>
#include <set>
#include <queue>
#include <map>
#include <list>
#include <string>
#include <iostream>
#include <stack>
#include <sstream>
using namespace std; 
#define PB push_back
#define MP make_pair
#define F first
#define S second 
#define BE(a) a.begin(),a.end() 
#define CLS(a,b) memset(a,b,sizeof(a))
#define SZ(a) ((int)a.size())
const long double pi=acos(-1.0);
#define torad(a) ((a)*pi/180.0)
typedef vector<int> vi ; 
typedef vector<string> vs ; 
typedef vector<double> vd ; 
typedef pair<int,int> pii ; 
typedef long long ll ; 
typedef long double ld ; 
typedef double dl ; 
class node {public:
int n,k,i,sol;
node()
{
	sol=0;
}
};
typedef vector<node> vn ; 
int cases,g;
int n,k;
int m;
bool cmpkn(const node & a, const node &b)
{
	if(a.k!=b.k)return a.k<b.k;
	if(a.n!=b.n)return a.n<b.n;
}
bool cmpi(const node & a, const node &b)
{
	return a.i<b.i;
}
node arr[10000];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
////////////////////////////////////////////
	int i,j,k;
	scanf("%d",&cases);
	for(g=0;g<cases;g++)
	{
		m=0;
		scanf("%d%d",&n,&k);

		printf("Case #%d: ",g+1);

		if((k+1)%(1<<n)==0)
			printf("ON\n");
		else
			printf("OFF\n");
		
	}
/*	int cur=0;
	sort(arr,arr+cases,cmpkn);
	m=0;
		for(i=0;i<=100000000;i++)
		{
			bool c=1;
			for(j=0;j<30;j++)
			{
				if(c==1)
				{
					c&= ( (m>>j) &1 );
					m^=(1<<j);
				}
				while(arr[cur].k==0)
				{
					arr[cur].sol=0;
					cur++;
				}
				while(arr[cur].n==j+1 && arr[cur].k==i+1)
				{
					if((m & ((1<<arr[cur].n)-1))==((1<<arr[cur].n)-1))
						arr[cur].sol=1;
					else
						arr[cur].sol=0;
					cur++;
				}
				if(cur==cases)
					goto bara;
			}
		}
bara:
		sort(arr,arr+cases,cmpi);
		for(g=0;g<cases;g++)
		{
			if(arr[g].sol)
				printf("ON\n");
			else
				printf("OFF\n");

		}*/
	return 0;
}