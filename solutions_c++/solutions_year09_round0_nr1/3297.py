#include <iostream>
using namespace std;
char str[30][20],s[15][100];
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int L,D,N;
	cin>>L>>D>>N;
	int i,j,k,sum,p1;
	for (i=0;i<D;i++)
	{
		cin>>str[i];
	}
	for (i=1;i<=N;i++)
	{
		sum=0;
		cin>>s[i];
		for (j=0;j<D;j++)
		{
			p1=0;
			for (k=0;k<L;k++)
			{
				if (s[i][p1]!='(')
				{
					if (str[j][k]==s[i][p1])
					{
						p1++;
						continue;
					}else
					{
						break;
					}
				}
				while (s[i][++p1]!=')')
				{
					if (str[j][k]==s[i][p1])
					{
						break;
					}
				}
				if (s[i][p1]==')')
				{
					break;
				}else
				{
					while (s[i][++p1]!=')');
					p1++;
				}
			}
			if (k==L)
			{
				sum++;
			}
		}
		cout<<"Case #"<<i<<": "<<sum<<endl;
	}
	return 0;
}