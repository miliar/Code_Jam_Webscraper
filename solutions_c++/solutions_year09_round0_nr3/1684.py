#include <iostream>
#include <string.h>
using namespace std;
int main()
{
	const char wtcj[20]="welcome to code jam";
	string str;
	int tot,t,ans,i,j,k;
	int opt[1000][19];
	cin >> tot;
	getline(cin,str);
for (t=1;t<=tot;t++)
{
	getline(cin,str);
	memset(opt,0,sizeof(opt));
	for (i=str.length()-1;i>=0;i--)
	{
		if (str[i]=='m')
			opt[i][18]=1;
		for (j=0;j<18;j++)
			if (str[i]==wtcj[j])
				for (k=i+1;k<str.length();k++)
					opt[i][j]=(opt[i][j]+opt[k][j+1])%10000;		
	}
	cout << "Case #" << t << ": ";
	ans=0;
	for (i=0;i<str.length();i++)
		ans+=opt[i][0];
	ans=ans%10000;
	if (ans<1000)
		cout << 0;
	if (ans<100)
		cout << 0;
	if (ans<10)
		cout << 0;
	cout << ans << endl;
}}
