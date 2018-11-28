#include <iostream>
#include <string>
#include <map>
using namespace std;

#define inf 40000

int main()
{
	int N, test;
	cin>>N;
	int s,q,i;
	string eng[105];
	int a[105][1005];
	char ch[200];
	string t; //query
	map<string, int> m;
	for (test=1; test<=N; test++)
	{
		m.clear();
		cin>>s;
		cin.ignore(200, '\n');
		for (i=0; i<s; i++)
		{
			cin.getline(ch, 200);
			eng[i]=ch;
			m[eng[i]]=i;
			a[i][0]=0;
		}
		cin>>q;
		cin.ignore(200, '\n');
		for (i=1; i<=q; i++)
		{
			cin.getline(ch, 200);
			t=ch;
			int p=m[t], j, k;
			for (j=0; j<s; j++)
			{
				if (j!=p)
				{
					a[j][i]=a[j][i-1];
					if (a[j][i]==inf)
						for (k=0; k<s; k++)
							if (a[k][i-1]+1<a[j][i])
								a[j][i]=a[k][i-1]+1;
				}
				else
					a[j][i]=inf;
			}
		}
		int min=a[0][q];
		for (i=1; i<s; i++)
			if (a[i][q]<min)
				min=a[i][q];
		cout<<"Case #"<<test<<": "<<min<<endl;
	}
	return 0;
}
