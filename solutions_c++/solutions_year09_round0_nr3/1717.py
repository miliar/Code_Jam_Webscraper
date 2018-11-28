#include<iostream>
#include<cstring>
using namespace std;

char a[600],b[100];
int low,high;
int com(int l,int h,int x,int y)
{
	int ans=0,i;
	if(x>y) return 0;
	if(y-x>h-l) return 0;
	if(y==x)
	{
		int s=0;
		for(i=l;i<=h;i++) if(b[x]==a[i]) s++;
		if(s>=10000) s%=10000;
		return s;
	}
	int m=(l+h)/2,t1,t2;
	for(i=0;i<y-x;i++) 
	{
		t1=com(l,m,x,x+i);
		t2=com(m+1,h,x+i+1,y);
		ans+=t1*t2;
		if(ans>=10000) ans%=10000;
	}
	ans+=com(l,m,x,y);
	ans+=com(m+1,h,x,y);
		if(ans>=10000) ans%=10000;
	return ans;
}

int main()
{
	int n,i,l,low,high;
	//freopen("C-small-attempt0.in","r",stdin);
//	freopen("c-s.out","w",stdout);
	scanf("%d",&n);
	getchar();
	strcpy(b,"welcome to code jam");
	int len=strlen(b);
	for(i=1;i<=n;i++)
	{
		gets(a);
		l=strlen(a);
		low=0,high=l-1;
		while(low<l&&a[low]!=b[0]) low++;
		while(high>=0&&a[high]!=b[len-1]) high--;
		if(low+len-1>high) 
		{
			printf("Case #%d: 0000\n",i);
			continue;
		}
       int ans=com(low,high,0,len-1);
	   int m=(low+high)/2;
	   printf("Case #%d: %d%d%d%d\n",i,ans/1000,ans%1000/100,ans%100/10,ans%10);
	}
	return 0;
}
		
