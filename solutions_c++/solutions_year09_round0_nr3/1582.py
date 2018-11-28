#include <iostream>
#include <cstring>
#include <string>

using namespace std;

int n, len;
char s[1000];
char sub[100]="welcome to code jam";
int f[100];

void calc(int c, char s[])
{
	memset(f,0,sizeof(f));
	for (int i=0;s[i]!=0;i++)
	{
		for (int j=0; j<len; ++j)
			if (sub[j]==s[i])
			{
				if (j==0) f[j]++;
				else if (f[j-1]>0) f[j]+=f[j-1];
			}
	}
	cout<<"Case #"<<c<<": "<<f[len-1]/1000<<(f[len-1]%1000)/100<<(f[len-1]%100)/10<<f[len-1]%10<<endl;
}
int main()
{
	len = strlen(sub);
	cin>>n;
	cin.getline(s,100);
	for (int i=0;i<n;i++)
	{
		cin.getline(s,1000);
		calc(i+1,s);
	}
	return 0;
}
