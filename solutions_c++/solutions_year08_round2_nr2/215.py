#include<iostream>
#include<string>
#include<vector>
#include<cmath>
#include<algorithm>
using namespace std;
//__int64 n,A,B,C,D,M,i,j,k;

int p[1003],a[1005],si[1005],f[1005][1005];
int main()
{
	int i,num=0,j;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int n=1000;
	for (i=2;i<=1000;i++)
	{
	   if (a[i]==0)
	   {
		  num++;p[num]=i;
	   }
	   for (j=1;((j<=num) && (i*p[j]<=n)); j++)
	   {
		  a[i*p[j]] = 1 ;
		   if (i%p[j] == 0) break;
	   }
	} 
	int ca,N,e;
//	for(i=0;i<1000;i++)
//		for(j=0;j<1000;j++)
	//		for(e=0;e<1000;e++)
	//			;
		//	cout<<"sd"<<endl;
	scanf("%d",&N);
	for(ca=1;ca<=N;ca++)
	{
		int A,B,P;
		scanf("%d%d%d",&A,&B,&P);
		memset(f,0,sizeof(f));
		memset(si,0,sizeof(si));
		for(i=A;i<=B;i++)
			for(j=i+1;j<=B;j++)
                  for(e=P;e<=i;e++)
					  if(a[e]==0&&i%e==0&&j%e==0)
						  f[i][j]=f[j][i]=1;
	 for(e=A;e<=B;e++)
		for(i=A;i<=B;i++)
			for(j=A;j<=B;j++)
				//if(i!=j&&i!=e&&j!=e)
					f[i][j]|=f[i][e]&&f[e][j];
			int sum=0;
			for(i=A;i<=B;i++)
				if(si[i]==0)
				{
					sum++;si[i]=1;
					for(j=i+1;j<=B;j++)
						if(f[i][j])
							si[j]=1;
				}
					printf("Case #%d: %d\n",ca,sum);
	}

	return 0;
}