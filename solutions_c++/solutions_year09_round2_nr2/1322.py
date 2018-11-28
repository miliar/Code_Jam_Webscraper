#include<stdio.h>

int a[30],l;

int f(int *a,int l)
{
	int t,i,j;
	j=0;
	while (j<l-1&&a[j]<=a[j+1]) j++; 
	//a[j]<a[j+1]
	if (j==l-1)
	{
		for (i=0,j=l-1;i<j;i++,j--)
		{
			t=a[i];
			a[i]=a[j];
			a[j]=t;
		}
		a[l]=0;
		for (i=l-1;i>=0;i--) if (a[i]!=0) break;
		a[l]=a[i];
		a[i]=0;
		l++;
	}
	else
	{
		for (i=j;i>=0;i--) if (a[i]<=a[j+1]) break;
		i++;
		t=a[i];
		a[i]=a[j+1];
		a[j+1]=t;
		for (i=0;i<j;i++,j--)
		{
			t=a[i];
			a[i]=a[j];
			a[j]=t;
		}
	}
	int ans=0;
	for (i=l-1;i>=0;i--) ans=a[i]+ans*10;
	return ans;	
}

int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.txt","w",stdout);
	int ans,k,i,T,t,n;
	scanf("%d",&T);
	for (k=1;k<=T;k++)
	{
		scanf("%d",&n);
		t=n;
		i=0;
		while (t)
		{
			a[i++]=t%10;
			t/=10;
		}
		ans=f(a,i);
		printf("Case #%d: %d\n",k,ans);
	}
}
