#include <iostream>
using namespace std;

int cnt=0;

int check(int x,int y)
{
	int tmp;
	if(x==y || x==0 || y==0) return 0;
	if(x<y) swap(x,y);
	if(y*2<=x) return 1;
	cnt++;
	return check(x%y,y);
}

int main()
{
	freopen("E:\\C-small-attempt0.in","r",stdin);
	freopen("E:\\C-small-attempt0.out","w",stdout);
	int T,cases=0;
	scanf("%d",&T);
	while(T--)
	{
		int i,j,ans=0;
		int a1,a2,b1,b2;
		scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
		for(i=a1;i<=a2;i++)
			for(j=b1;j<=b2;j++)
			{	
				cnt=0;
				if(check(i,j) && !(cnt%2)) ans++;
			}
			printf("Case #%d: %d\n",++cases,ans);
	}
	return 0;
}