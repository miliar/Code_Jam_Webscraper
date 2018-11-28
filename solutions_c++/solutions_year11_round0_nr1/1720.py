#include <iostream>
#include <cstring>
using namespace std;

int f[110],p[110],la[110];
int i,j,t,ca,n,s,lb,lo;
char ch;

int main()
{
	freopen("in.in","r",stdin);
	freopen("ou.ou","w",stdout);
	cin>>t;
	while (t--)
	{
		ca++;
		cin>>n;
		lo=0; lb=0; p[0]=1;
		for (i=1;i<=n;i++)
		{
			cin>>ch>>j;
			p[i]=j;
			if (ch=='O') 
			{
				la[i]=lo;
				lo=i;
			}
			if (ch=='B') 
			{
				la[i]=lb;
				lb=i;
			}
		}
		memset(f,0,sizeof(f));
		for (i=1;i<=n;i++)
		{
			s=f[la[i]]+abs(p[la[i]]-p[i]);
			if (f[i-1]>s) s=f[i-1];
			f[i]=s+1;
		}
		cout<<"Case #"<<ca<<": "<<f[n]<<endl;
	}
}
