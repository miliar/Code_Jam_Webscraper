#include <iostream>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
using namespace std;

long long Count;
bool a[2000001l];
long A, B, num[10];
char str1[10],str2[10];

void process(long n)
{
	long temp;
	int i,j,c,d,k=1;
    if(a[n])
			return;
	num[0] = n;
	a[n] = true;
	sprintf(str1,"%ld",n);
	c = strlen(str1);
	for(i=1; i<c; i++)
	{
		string str(str1);
		str = str.substr(c-i,i) + str.substr(0,c-i);
		temp = atol(str.c_str());

		if(!a[temp] && temp>=A && temp<=B)
		{
			a[temp] = true;
			num[k++] = temp;
		}
	}
	Count += k*(k-1)/2;
}

int main(void)
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int t,T;
	scanf("%d",&T);
	for(int t = 1; t <= T; ++t)
	{
		Count = 0ll;
  		memset(a,0,2000001l);
		scanf("%ld%ld",&A,&B);
		for(long i=A; i<=B; i++)
			process(i);
		printf("Case #%d: %lld\n",t,Count);
	}
	return 0;
}
