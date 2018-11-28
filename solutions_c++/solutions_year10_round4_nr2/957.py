
#include "string.h"
#include "math.h"
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
#include <string>
#include <iostream>
using namespace std;

#define max(a,b)            (((a) > (b)) ? (a) : (b))
#define min(a,b)            (((a) < (b)) ? (a) : (b))

const int MAX_INT = 0x07070707;
const double eps = 1e-10;

const int N =1030;

int m[N];
int n;

int sum(int l,int r)
{
	int t=0;
	for(int i=l;i<=r;i++)
		t +=m[i];
	return t;
}
void f(int l,int r)
{
	for(int i=l;i<=r;i++)
	{
		m[i]--;
		if(m[i]<0)
			m[i]=0;
	}
}
int check(int l,int r)
{
	if(sum(l,r)<=0)return 0;

	f(l,r);
	int mid = (l+r)/2;
	return check(l,mid)+check(mid+1,r)+1;
}
int main()
{
	freopen("F://Google Code Jam//B-small-attempt2.in","r",stdin);
	//freopen("F://Google Code Jam//read.txt","r",stdin);
	freopen("F://Google Code Jam//write.txt","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int tst=1;tst<=cas;tst++)
	{
		printf("Case #%d: ",tst);
		int i,p,x;
		scanf("%d",&p);
		for(i=0;i<(1<<p);i++){
			scanf("%d",&m[i]);
			m[i] = p-m[i];
		}

		for(i=0;i<(1<<p)-1;i++)
			scanf("%d",&x);

		printf("%d\n",check(0,(1<<p)-1));
	}
	return 0;
}