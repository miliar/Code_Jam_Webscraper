// Author : Muhammad Rifayat Samee
// Problem : 
// Algorithm:
#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<algorithm>
#include<string>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#define MAX(a,b) (a>b)?a:b
#define MIN(a,b) (a<b)?a:b
#define INF 987654321
#define pi (2*acos(0.0))
#define eps 1e-7

using namespace std;
int power[35];

void cal()
{
	int i;

	power[0] = 1;
	power[1] = 2;

	for(i=2;i<=30;i++)
	{
		power[i] = power[i-1]*2;
	}
}


int main()
{
	//freopen("A-large.in.txt","r",stdin);
	//freopen("A.out","w",stdout);
	cal();

	int n,k,cases,ct=1,d,r,q;
	scanf("%d",&cases);
	while(cases--)
	{
		scanf("%d %d",&n,&k);
		
	
		d = power[n]-1;
			
		if((k%(d+1))==d)
			printf("Case #%d: ON\n",ct++);
		else
			printf("Case #%d: OFF\n",ct++);
	}
	return 0;


}