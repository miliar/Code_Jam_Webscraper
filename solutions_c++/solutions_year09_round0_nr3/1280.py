#include <iostream>
using namespace std;
char cc[]=" welcome to code jam";
int m[1000][20];
char c[1000];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tt,ii,n,i,j,k,s;
	cin>>tt;
	cin.getline(c,1000);
	for(ii=1;ii<=tt;ii++)
	{
		cin.getline(c,1000);
		s=0;
		n=strlen(c);
		memset(m,0,sizeof(m));
		for(i=0;i<n;i++) m[i][0]=1;
		for(i=0;i<n;i++)
		{
			if(c[i]=='w') m[i][1]=1;
			for(j=2;j<20;j++)
			{
				if(c[i]==cc[j])
				{
					for(k=0;k<i;k++)
					{
						m[i][j]+=m[k][j-1];
						while(m[i][j]>=10000) m[i][j]-=10000;
					}
				}
			}
			s+=m[i][19];
			while(s>=10000) s-=10000;
		}
		printf("Case #%d: %04d\n",ii,s);
	}
	return 0;
}

