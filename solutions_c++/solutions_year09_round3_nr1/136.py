#include <iostream>
#include <string.h>
using namespace std;
int main()
{
	int ks,dgt,min,i,j,t,ans;
	int value[100];
	string str;
	cin >> ks;
	getline(cin,str);
for (t=1;t<=ks;t++)
{
	getline(cin,str);
	min=0;
	memset(value,255,sizeof(value));
	for (i=0;i<str.length();i++)
		if (str[i]==str[0])
			value[i]=1;
	for (i=1;i<str.length();i++)
		if (value[i]==-1)
		{
			for (j=i;j<str.length();j++)
				if (str[i]==str[j])
					value[j]=min;
			if (min==0)
				min=2;
			else
				min++;
		}
	dgt=1;
	ans=0;
	min=0;
	for (i=0;i<str.length();i++)
	{
		if (value[i]>min)
			min=value[i];
	}
	min++;
	for (i=str.length()-1;i>=0;i--)
	{
		ans+=value[i]*dgt;
		dgt*=min;
	}
	cout << "Case #" << t << ": " << ans << endl;
}
}
