#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<stack>
#include<cstring>
#include<cstdio>
#include<map>
#include<cstdlib>
#include<fstream>
#include<queue>
using namespace std;
int main()
{
	#if 1
	freopen("1.in","r",stdin);
	freopen("1.out","w+",stdout);
	#endif
	int test,n;
	int i,j,k,t;
	int f[10001];
	int sum1,sum2,sum3,sum4,maxi=0;
	cin>>test;
	for (t=1;t<=test;t++)
	{
		cin>>n;
		maxi=0;
		for (i=0;i<n;i++) scanf("%d",&f[i]);
		for (i=0;i<n;i++)
			for (j=i;j<n;j++)
			{
				sum1=0;
				sum2=0;
				sum3=0;
				sum4=0;
				for (k=i;k<=j;k++)
					sum1^=f[k];
				for (k=0;k<i;k++)
					sum2^=f[k];
				for (k=j+1;k<n;k++)
					sum2^=f[k];
				for (k=i;k<=j;k++)
					sum3+=f[k];
				for (k=0;k<i;k++)
					sum4+=f[k];
				for (k=j+1;k<n;k++)
					sum4+=f[k];
				if (sum1==sum2 && !(sum3==0 || sum4==0)) 
				{
					if ((sum3>sum4?sum3:sum4)>maxi) maxi=sum3>sum4?sum3:sum4;
				}
			}
		if (maxi==0) cout<<"Case #"<<t<<": NO"<<endl;
		else cout<<"Case #"<<t<<": "<<maxi<<endl;
	}
	return 0;
}