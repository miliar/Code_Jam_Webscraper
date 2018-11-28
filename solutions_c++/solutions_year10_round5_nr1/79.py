#include<iostream>
#include<algorithm>
using namespace std;

long long gcd(long long a,long long b)
{
    if(b==0)return a;
    return gcd(b,a%b);
}
long long e_gcd(long long a,long long b,long long &x,long long &y)
{
    if(b==0)
    {
        x=1;
        y=0;
        return a;
    }
    long long x1,y1;
    long long ans=e_gcd(b,a%b,x1,y1);
    x=y1;
    y=x1-a/b*y1;
    return ans;
}
long long modfc(long long a,long long b,long long n,int *ans)//ax%n=b
{
    long long d,x,y;
    d=e_gcd(a,n,x,y);
    if(b%d!=0)return -1;
    long long e=x*(b/d)%n;//LL
    if(e<0)
        e+=n;
    ans[0]=e;
    long long add=n/d;
    for(int i=1;i<d;i++)
    {
        ans[i]=ans[i-1]+add;
        if(ans[i]>=n)
            ans[i]-=n;
        //ans[i]=(e+i*(n/d))%n;
    }
    return d;
}
char a[1000000];
long prime[100000];
int ans[234234];
int main()
{
	int zuida = 1000000;
	for(int i=3;i< 1000;i+=2)
	{
		if(a[i])continue;
		for(int j=i*i;j<zuida;j+=(i<<1))
		{
			a[j]=1;
		}
	}
	int ind=1;

	prime[0]=2;
	for(int i=3;i<zuida;i+=2)
	{
		if(a[i])continue;
		prime[ind++]=i;
	}
	//cout<<ind<<endl;
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int zu;
	scanf("%d",&zu);
	for(int CaSe = 1;CaSe<=zu;CaSe++)
	{
		printf("Case #%d: ",CaSe);
		int m,n;
		scanf("%d%d",&m,&n);
		int b[11]={0};
		for(int i=0;i<n;i++)
		{
			scanf("%d",&b[i]);
		}
		if(n==1)
		{
			puts("I don't know.");
			continue;
		}
		if(b[0]==b[1])
		{
			bool f =1;
			for(int i=1;i<n;i++)
			{
				if(b[0]!=b[i])
					f=0;
			}
			if(f)
			{
				printf("%d\n",b[0]);
			}else
			{
			puts("I don't know.");

			}
			continue;
		}
		if(n==2)
		{
			puts("I don't know.");
				continue;
		}
		//////////////////
		int z=0;
		for(int i=0;i<n;i++)
		{
			z=max(z,b[i]);
		}
		int zzz= 1;
		for(int i=0;i<m;i++)zzz=zzz*10;

		int fa=-1;
		for(int i=ind-1;i>=0;i--)
		{
			if(fa==-2)break;
			if(prime[i]>zzz)continue;
			if(prime[i]<=z)break;
			int P = prime[i];

			int cha = (b[1]-b[0]+P)%P;
			int cha1 = (b[2]-b[1]+P)%P;
			int x = modfc(cha,cha1,P,ans);
			if(x==-1)continue;
			x=ans[0];
			////*******

			int y = ((b[1]- (long long) b[0]*x)%P+P)%P;

				bool f = 1;
				for(int i=2;i<n;i++)
				{
					int xx = ((long long )b[i-1] * x + y)%P;
					if(xx==b[i])
					{
						continue;
					}
					f=0;
				}
				if(!f)continue;

					b[n]=(b[n-1]*(long long) x +y)%P;
					if(fa==-1)
					{
						fa=b[n];
					}
					else
					{
						if(fa!=b[n])
						{
							fa=-2;
						}
					}
		}
		if(fa==-2 ||fa==-1)
		{
			puts("I don't know.");
		}else
		{
			printf("%d\n",fa);
		}
	}
}