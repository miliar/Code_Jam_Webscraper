#include <iostream>
#include<cmath>
#include<vector>
#include<map>
#include<set>
using namespace std;
int sum=0;
int gcd(int x,int y)
{
	int temp;
	if(x==y|| !x|| !y) return 0;
	if(x<y) {
		temp=x;
		x=y;
		y=temp;
	}
	if(y*2<=x) return 1;
	sum++;
	return gcd(x%y,y);
}
int main(){
	freopen("D: \\C-small-attempt0.in","r",stdin);
	freopen("D: \\C-small-attempt0.out","w",stdout);
	int cnt=1,T;
	scanf("%d",&T);
	while(T--)
	{
		int res=0,x,y,a,b;
		scanf("%d%d%d%d",&x,&y,&a,&b);
		for(int i=x;i<=y;i++)
			for(int j=a;j<=b;j++)
			{
				sum=0;
				if(gcd(i,j) && sum%2==0) 
					res++;
			}
			printf("Case #%d: %d\n",cnt,res);
			cnt++;
	}
	return 0;
}