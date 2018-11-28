#include <iostream>
using namespace std;
int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int t,i,j;
	double r[55],k[55],n[55],g[55][1010],capa,sign,tp,euro,times;
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>r[i]>>k[i]>>n[i];
		for(j=0;j<n[i];j++)
			cin>>g[i][j];
	}
	for(i=0;i<t;i++)
	{
		capa=0;euro=0;times=0,tp=0;
		for(j=0;j<n[i];)
		{
			if(times==r[i])
			{
				cout<<"Case #"<<i+1<<": "<<euro<<endl;
				break;
			}
			if(capa==0)
			{
				sign=j;
			}
			if(j==sign&&tp>=n[i])
			{
				capa=0;
				tp=0;
				times++;
				if(j==n[i]-1)
				{
					j=0;
					continue;
				}
				continue;
			}
			else
			{
				if(capa+g[i][j]<=k[i])
				{
					capa+=g[i][j];
					euro+=g[i][j];
					tp++;
				}
				else
				{
					tp=1;
					times++;
					if(times==r[i])
					{
						cout<<"Case #"<<i+1<<": "<<euro<<endl;
						break;
					}
					sign=j;
					capa=g[i][j];
					euro+=g[i][j];
					if(j==n[i]-1)
					{
						j=0;
						continue;
					}
					j++;
					continue;
				}
			}
			if(j==n[i]-1)
			{
				j=0;
				continue;
			}
			j++;
		}
	}
	return 0; 
}