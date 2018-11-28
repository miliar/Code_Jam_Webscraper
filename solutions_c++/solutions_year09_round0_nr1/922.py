#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

string map[5002];
string str[512];

int flag[16][26];

int cmp(string a,string b)
{
	return a.compare(b)<0;
}

int main()
{
	int l,d,n;
	cin>>l>>d>>n;
	for (int i=0;i<d;++i)
		cin>>map[i];
	for (int i=0;i<n;i++)
		cin>>str[i];

//	sort(map,map+d,cmp);

/*
	for (int i=0;i<d;++i)
		cout<<map[i]<<endl;
*/

	for (int i=0;i<n;i++)
	{
		memset(flag,0,sizeof(flag));
		int p=0;
		for (int j=0;j<l;j++)
		{
			if (str[i][p]=='(')
			{
				while (str[i][++p]!=')')
				{
					flag[j][str[i][p]-'a']=1;
				}
			}
			else
			{
				flag[j][str[i][p]-'a']=1;
			}
			p++;
		}

		int sum=0,k;
		for (int j=0;j<d;j++)
		{
			for (k=0;k<l;k++)
			{
				if (!flag[k][map[j][k]-'a']) break;
			}
			if (k==l) sum++;
		}

		printf("Case #%d: %d\n",i+1,sum);
	}

	return 0;
}
