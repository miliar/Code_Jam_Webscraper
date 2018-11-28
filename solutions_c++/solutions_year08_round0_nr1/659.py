#include <string>
#include <iostream>
#include <fstream>
#include <map>
using namespace std;
int nn,ii,n,m;
int a[110],b[1100];
int f[1100][110];
string st;
map<string,int> hash;
int main()
{
	ifstream cin("a-large.in");
	ofstream cout("a-large.out");
	int i,j,k,t,num;
	map<string,int>::iterator i1;
	cin >>nn;
	for (ii=1;ii<=nn;ii++)
	{
		num=0;
		memset(f,-1,sizeof(f));
		cin >>n;
		cin >>ws;
		hash.clear();
		for (i=1;i<=n;i++)
		{
			getline(cin,st);
			i1=hash.find(st);
			if (i1!=hash.end()) t=i1->second;
			else
			{
				num++;
				hash.insert(make_pair(st,num));
				t=num;
			}
			a[i]=t;
		}
		cin >>m;
		cin >>ws;
		for (i=1;i<=m;i++)
		{
			getline(cin,st);
			i1=hash.find(st);
			if (i1!=hash.end()) t=i1->second;
			else
			{
				num++;
				hash.insert(make_pair(st,num));
				t=num;
			}
			b[i]=t;
		}
		if (m==0)
		{
			cout <<"Case #" <<ii <<": "<<"0" <<endl;
			continue;
		}
		f[0][0]=0;
		for (i=1;i<=m;i++)
			for (j=1;j<=n;j++)
				if (a[j]!=b[i])
				{
					for (k=0;k<=n;k++)
					{
						if (k==j) t=0; else t=1;
						if ((f[i-1][k]>=0)&&((f[i-1][k]+t<f[i][j])||(f[i][j]<0)))
							f[i][j]=f[i-1][k]+t;
					}
				}
		t=100000;
		for (i=1;i<=n;i++)
			if ((f[m][i]>0)&&(f[m][i]<t))
				t=f[m][i];
		cout <<"Case #" <<ii <<": "<<t-1 <<endl;
	}
	return 0;
}

				
	