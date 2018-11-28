#include <iostream>
using namespace std;

char a[2000];

void init()
{
	
	cin.getline(a+1,30);
	a[0]='0';
}

void make()
{
	int j,i,u,l,k;
	char c;
	j=0;
	i=1;
	while (a[i])
	{
		if (a[i-1]<a[i]) j=i;
		i++;
	}
	l=i-1;
	k=l;
	while (a[k]<=a[j-1]) k--;
	c=a[j-1];
	a[j-1]=a[k];
	a[k]=c;
	u=(j+l)/2;
	for (i=j;i<=u;i++)
	{
		c=a[i];
		a[i]=a[l-i+j];
		a[l-i+j]=c;
	}
	if (a[0]=='0') cout<<a+1<<endl;
	else cout<<a<<endl;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int cs,i;
	cin>>cs;
	cin.get();
	for (i=1;i<=cs;i++)
	{
		init();
		cout<<"Case #"<<i<<": ";
		make();
	}
	return 0;
}