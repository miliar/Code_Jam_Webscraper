#include<iostream>
#include<cmath>
using namespace std;
short ss[100][100];
int main()
{
	freopen("c:\\2.in","r",stdin);
	freopen("c:\\out2.txt","w",stdout);
	int t,i;
	cin>>t;
	long long a1,a2,b1,b2,m,n,big,small;
	for(i=1;i<=t;i++)
	{
		cin>>a1>>a2>>b1>>b2;
		int sum=0;
		for(m=1;m<=a2;m++)
		{
			for(n=1;n<=b2;n++)
			{
				ss[m][n]=0;
				if(m>n)
				{big=m;small=n;}
				else
				{big=n;small=m;}
				if(m==n)
					ss[m][n]=-1;//bi shu
				else if(big%small==0)
					ss[m][n]=1;//bi shen
				else
				{
					long long y;
					y=big%small;
					if(small%y==0)
					{
						if((big-y)/small>1)
							ss[m][n]=1;
						else
							ss[m][n]=-1;
					}
					else
					{
						int tt,ii;
						tt=(big-y)/small;
						for(ii=1;ii<=tt;ii++)
						{
							if(ss[big-ii*small][small]==-1)
							{
								ss[m][n]=1;
							}
							else if(ss[big-ii*small][small]==1)
							{
								ss[m][n]=-1;
							}
						}
					}
				}
			if((m>=a1)&&(n>=b1)&&(ss[m][n]==1))
				sum++;
				




			}
		}
		cout<<sum<<endl;

	}


return 0;
}
