#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
using namespace std;
int na[120],nb[120];
bool can(int x,int y)
{
	int t1=0,t2=0;
	while(x){na[t1++]=x%10;x/=10;}
	while(y){nb[t2++]=y%10;y/=10;}
	if(t1!=t2)return false;
	for(int i=0;i<t1;i++)
	{
		bool C=true;
		for(int j=0;j<t1;j++)
		if(na[j]!=nb[(i+j)%t1])
		{C=false;break;}
		if(C)return true;
	}
	return false;
}
int _,ca,i,j,a,b;
int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d\n",&_);
	for(ca=1;ca<=_;ca++)
	{
		scanf("%d%d",&a,&b);
		int ret=0;
		for(i=a;i<=b;i++)
		for(j=i+1;j<=b;j++)
		{
			if(can(i,j))ret++;
		}
		printf("Case #%d: %d\n",ca,ret);
	}
}
