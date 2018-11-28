#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main()
{
	int i,j,k,a[105][2],t,n,l1,l2;
	char s[105][105];
	double b[105][3];

	freopen("al.in","r",stdin);
	freopen("al.out","w",stdout);
	cin>>t; k=0;
	while(t--)
	{
		k++;
		cin>>n;
		for(i=0;i<n;i++) cin>>s[i];
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
				if (s[i][j]!='.')
				{
					a[i][1]++;
					if (s[i][j]=='1') a[i][0]++;
				}
		for(i=0;i<n;i++)
			if (a[i][1]==0) b[i][0]=0;
			else
				b[i][0]=a[i][0]*1.0/a[i][1];
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
				if (s[i][j]!='.')
				{
					l1=a[j][0]; l2=a[j][1]-1;
					if (s[j][i]=='1') l1--;
					if  (l2==0) b[i][0]+=0;
					else
						b[i][1]+=l1*1.0/l2;
				}
			if (a[i][1]!=0) b[i][1]/=a[i][1];
		}
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
				if (s[i][j]!='.')
					b[i][2]+=b[j][1];
			if (a[i][1]!=0) b[i][2]/=a[i][1];
		}
		printf("Case #%d:\n",k);
		for(i=0;i<n;i++)
			printf("%.10lf\n",b[i][0]*0.25+b[i][1]*0.5+b[i][2]*0.25);
	}
	//system("pause");
	return 0;
}