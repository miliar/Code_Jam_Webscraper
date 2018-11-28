#include<stdio.h>
#include<string.h>
#include<math.h>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
using namespace std;
#define MAX 1010
const int BIG=0x3f3f3f3f;
int main()
{
	int cs,n,ot,op,bt,bp,i,j,t;
	char c[2];
	scanf("%d",&cs);
	for(int dd=1;dd<=cs;dd++)
	{
		ot=bt=0;
		op=bp=1;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%s%d",c,&t);
			if(c[0]=='O')
			{
				ot=max(bt,ot+abs(op-t))+1;
				op=t;
			}
			else
			{
				bt=max(ot,bt+abs(bp-t))+1;
				bp=t;
			}
		}
		printf("Case #%d: %d\n",dd,max(ot,bt));
	}
}