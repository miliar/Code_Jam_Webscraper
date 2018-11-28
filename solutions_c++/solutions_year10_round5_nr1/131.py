#include <iostream>
using namespace std;


int a[111],w[111];
char mas[1111111];
int prms[111111];
int val = 0;


int pow(int a, int b ,int c)
{
	int r=1;
	for (;b;b>>=1)
	{
		if (b&1)
		{
			r=(1LL*r*a)%c;
		}
		a=(1LL*a*a)%c;
	}
	return r;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	for (int i=2;i<=1000000;)
	{
		prms[val++]=i;
		for (int j=i*2;j<=1000000;j+=i)
			mas[j]=1;
		for (++i;i<=1000000&&mas[i]==1;i++);
	}
	int t;
	scanf("%d",&t);
	for (int i=1;i<=t;i++)
	{
		cerr<<i<<endl;
		printf("Case #%d: ",i);
		int d,k;
		scanf("%d%d",&d,&k);
		for (int j=0;j<k;j++)
			scanf("%d",a+j);
		int big = 10;
		for (;d>1;d--)
			big*=10;
		int cnt=0,res;
		for (int u=0;u<val&&big>=prms[u];u++)
		{
			int da=1;
			for (int j=0;j<k;j++)
				if (a[j]>=prms[u])
					da=0;
			int ooo=0;
			if (da)
			{
				int brk = 0;
				int tempA=-1;
				for (int j=0;j<k-1;j++)
				{
					w[j]=a[j+1]-a[j];
					if (w[j]<0)
						w[j]+=prms[u];
					if (j)
					{
						if (w[j-1])
						{
							int E = pow(w[j-1],prms[u]-2,prms[u]);
							int rE = (1LL*E*w[j])%prms[u];
							if (tempA==-1)
								tempA=rE;
							else if (tempA!=rE)
								tempA=-2;
						}
						else 
						{
							if (w[j])
								brk=1;
							else
								tempA=0;
						}
					}
				}
				if (k==1)
				{
					cnt = 100;
				}
				else if (k==2)
				{
					if (a[0]==a[1])
					{
						res=a[1];
						cnt=1;
					}
					else
						cnt = 100;
				}
				else if (!brk && tempA>=0)
				{
					int yB = a[1]-(1LL*a[0]*tempA)%prms[u];
					if (yB<0)
						yB+=prms[u];
					yB = (1LL*a[k-1]*tempA+yB)%prms[u];
					if (!cnt || res==yB)
					{
						cnt = 1;
						res = yB;
					}
					else
						cnt++;
				}






		///*		for (int A=0;A<prms[u];A++)
		//		{
		//			int B=-1;
		//			int st=1;
		//			if (k==1)
		//				st=0;
		//			for (int j=0;j<k-1;j++)
		//			{
		//				int b=a[j+1] - (1LL*a[j]*A)%prms[u];
		//				if (b<0)
		//					b+=prms[u];
		//				if (B==-1)
		//					B=b;
		//				else if (b!=B)
		//					st = 0;
		//			}
		//			if (st)
		//			{
		//				int R=(1LL*A*a[k-1]+B)%prms[u];
		//				if (!cnt || R==res)
		//				{
		//					cnt=1;
		//					res=R;
		//				}
		//				else
		//				{
		//					cnt = 100;
		//					ooo=1;
		//					break;
		//				}
		//			}
		//		}
		//		if (ooo)
		//			break;*/
			}
		}
		if (cnt==1)
		{
			printf("%d\n",res);
		}
		else
		{
			printf("I don't know.\n");
		}
	}
	return 0;
}