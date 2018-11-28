#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

const int maxn=1010;
const int inf=999999;

int dyna[maxn],e,q;
string engin[maxn],query[maxn];

int main()
{
	int test;
	cin >> test;
	for (int w=1;w<=test;w++)
	{
		cin>> e;
		getline(cin,engin[0]);
		for (int i=1;i<=e;i++)
			getline(cin,engin[i]);
		cin >> q;
		getline(cin,engin[0]);
		for (int i=1;i<=q;i++)
			getline(cin,query[i]);
		for (int i=0;i<=q;i++)
			dyna[i]=inf;
		dyna[q+1]=0;
		for (int i=q;i>=1;i--)
		{
			for (int j=1;j<=e;j++)
			{
				if (query[i]!=engin[j])
				{
					query[q+1]=engin[j];
					for (int k=i+1;k<=q+1;k++)
						if (query[k]==engin[j])
						{
							dyna[i]=min(dyna[k]+1,dyna[i]);
							break;
						}
						
				}
			}
		}
		cout <<"Case #"<<w<<": "<< max(0,dyna[1]-1) << endl;
	}
	return 0;
}
