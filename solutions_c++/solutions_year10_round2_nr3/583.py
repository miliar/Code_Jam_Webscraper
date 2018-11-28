#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
int t,a[30],b[30];
const int MD=100003;

int find(int k)
{
	for (int i=b[0];i>0;i--)
		if (b[i]==k) return i;
	return 0;
}

void pre()
{
	memset(a,0,sizeof(0));  
	for (int n=2;n<=25;n++)
		for (int i=1<<(n-2);i<1<<(n-1);i++)
			{
				b[0]=0;
				for (int j=2;j<=n;j++)
					if (i>>(j-2)&1) b[++b[0]]=j;
				int k=n;  while(find(k)) k=find(k);
				if (k==1) a[n]++;
			}
}		

int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("c.out","w",stdout);
	pre();
	cin>>t;
	for (int i=1;i<=t;i++)
	{
		int n;
		cin>>n;
		cout<<"Case #"<<i<<": "<<a[n]%MD<<endl;
	}
	fclose(stdin); fclose(stdout);
	return 0;
}
