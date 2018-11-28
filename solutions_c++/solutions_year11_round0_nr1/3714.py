#include <stdio.h>
#define abs(a) ((a)>0?(a):-(a))

int casen;
int n;
int a[111];
char b[111];
int c[2][111];
int c0,c1;

int search(int k0,int k1,int x,int y,int num)
{
	int ans=0;
	int r;
	while(num<=n)
	{
		if(b[num]=='O')
		{
			r=abs(x-c[0][k0])+1;
			ans+=r;
			x=c[0][k0];
			if(r>=abs(y-c[1][k1])) y=c[1][k1];
			else y=c[1][k1]+(abs(y-c[1][k1]))-r;
			k0++;
		}
		else
		{
			r=abs(y-c[1][k1])+1;
			ans+=r;
			y=c[1][k1];
			if(r>=abs(x-c[0][k0])) x=c[0][k0];
			else x=c[0][k0]+(abs(x-c[0][k0]))-r;
			k1++;
		}
		//printf("%c r=%d x=%d y=%d\n",b[num],r,x,y);
		num++;
	}
	return ans;
}

void solve()
{
	int ans=0;
	ans=search(1,1,1,1,1);
	printf("%d\n",ans);
}

int main()
{
	int j=0;
	scanf("%d",&casen);
	while(casen--)
	{
		j++;
		c0=c1=0;
		printf("Case #%d: ",j);
		scanf("%d",&n);
		//printf("n=%d\n",n);
		for(int i=1;i<=n;i++)
		{
			char str[11];
			scanf("%s",str);
			b[i]=str[0];
			scanf("%d",&a[i]);
			if(b[i]=='O') c[0][++c0]=a[i];
			else c[1][++c1]=a[i];
			//printf("%c %d\n",b[i],a[i]);
		}
		c[1][++c1]=1;
		c[0][++c0]=1;
		solve();
	}
	return 0;
}
