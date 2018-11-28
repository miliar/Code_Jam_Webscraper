#include <iostream>
#include <cmath>
using namespace std;
#define eps 1e-9
/*#define N 50000
bool a[N];
int p[5200];
int d[50];
int cnt[50];
int f[N];
int num;

void Prime()
{
    memset(a,0,sizeof(a));
    int i,j;
    for (i=2;i<N;++i)
	{
		if (!a[i]) p[num++]=i;
        for(j=0;j<num && i*p[j]<N;++j)
		{
            a[i*p[j]]=1;
            if(!(i%p[j])) break;
        }
    }
}

int check(int x)
{
	long j;
	for (j=0;p[j]<=sqrt((double)x);j++)
		if (x%p[j]==0) return 0;
	return 1;
}


int pfactor(int n)
{
	int i,res=0;
	int f;

//	if (check(n)) return res;
//	d[res++]=1;cnt[res-1]=1;
//	d[res++]=n;cnt[res-1]=1;
	for (i=0;p[i]<=sqrt((double)n);++i)
		if (n%p[i]==0)
		{
			f=0;
			d[res++]=p[i];
			while (n%p[i]==0)
			{
				++f;
				n/=p[i];
			}
			cnt[res-1]=f;
		}
	if (n!=1)
	{
		d[res++]=n;
		cnt[res-1]=1;
	}

//	if (n!=1) d[res++]=n;
	return res;
}

int factor(int n)
{
	int len=pfactor(n);
	int bound=1,j,q,k,tt,a;
	int fac,res=0;
	for(j=0; j<len; j++)        //  采用数字电路加1法枚举约数
		bound*=(cnt[j]+1);         //  求出最大值bound.. 
	for(j=0; j<bound; j++)
	{                                          // 0 ~ bound-1
		fac= 1;
		q=j;
		for(int k=0; q && k<len; k++)
		{                                          // 模出每一位取几个
			tt=q % (cnt[k]+1);
			for(a=0; a< tt; a++) 
				fac*=d[k];
			q/=(cnt[k]+1);
		}
		f[res++]=fac;
	}
	return res;
}

int max(int x,int y)
{
	return x>y?x:y;
}

int min(int x,int y)
{
	return x<y?x:y;
}*/

int main()
{
	int i,j,i2,j2,m,n,t;
	int k,b1,b2,len;
	int aa,ok;
	double cc[3];
	double p,s ;
//	Prime();

	freopen("B-small-attempt2.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for (k=1;k<=t;++k)
	{
		scanf("%d%d%d",&n,&m,&aa);

//		b1=max(n,m);
//		b2=min(n,m);

//		len=factor(aa);
//		for (i=0;i<len;++i) printf("%d ",f[i]);printf("\n");
/*		for (i=0;i<len;++i)
		{
			if (f[i]*f[i]==aa) 
			{
				ok=1;
				break;
			}
			if (i<len-1&&f[i]*f[i+1]==aa)
			{
				ok=2;
				break;
			}
		}
		*/

		
		for (i=0;i<=n;++i)
			for (j=0;j<=m;++j)
			
				for (i2=0;i2<=n;++i2)
					for (j2=0;j2<=m;++j2)
					{
						if ((i*j2-i2*j)==0) continue;
						cc[0]=sqrt((i-i2)*(i-i2)+(j-j2)*(j-j2));
						cc[1]=sqrt(i*i+j*j);
						cc[2]=sqrt(i2*i2+j2*j2);
						p=(cc[0]+cc[1]+cc[2])/2;
						
						s=sqrt((p-cc[0])*(p-cc[1])*(p-cc[2])*p);
					//printf("%lf\n",aa*1.0/2);
						if (fabs(s-aa*1.0/2)<1e-6)
						{
							printf("Case #%d: 0 0 %d %d %d %d\n",k,i,j,i2,j2);
						//	printf("%lf %lf %lf\n",cc[0],cc[1],cc[2]);
						//printf("%lf\n",sqrt((p-cc[0])*(p-cc[1])*(p-cc[2])*p));
							goto end;
						}
					}

		printf("Case #%d: IMPOSSIBLE\n",k);
/*
		if (ok==1) 
		{
			if (f[i]>b1) printf("Case #%d: IMPOSSIBLE\n",k);
			else printf("Case #%d: 0 0 0 %d %d 0\n",k,f[i],f[i]);
			continue;		
		}
		if (ok=2)
		{
			if (f[i+1]>b1||f[i]>b2) printf("Case #%d: IMPOSSIBLE\n",k);
			else {
				if (b1==n) printf("Case #%d: 0 0 0 %d %d 0\n",k,f[i],f[i+1]);
				else printf("Case #%d: 0 0 0 %d %d 0\n",k,f[i+1],f[i]);
			continue;	
			}
		
		}*/
end:;

	}
	return 0;
}

