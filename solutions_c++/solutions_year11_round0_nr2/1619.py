#include <iostream>
#include <cstring>
using namespace std;

char c[256][256];
bool d[256][256];
char ch1,ch2,ch3;
int nc,nd,n,t,ca,i,j,len;
char h[256];

int main()
{
	freopen("in.in","r",stdin);
	freopen("ou.ou","w",stdout);
	cin>>t;
	while (t--)
	{
		ca++;
		memset(c,0,sizeof(c));
		memset(d,0,sizeof(d));
		memset(h,0,sizeof(h));
		cin>>nc;
		for (i=0;i<nc;i++)
		{
			cin>>ch1>>ch2>>ch3;
			c[ch1][ch2]=ch3;
			c[ch2][ch1]=ch3;
		}
		cin>>nd;
		for (i=0;i<nd;i++)
		{
			cin>>ch1>>ch2;
			d[ch1][ch2]=1;
			d[ch2][ch1]=1;
		}
		len=0;
		cin>>n;
		for (i=1;i<=n;i++)
		{
			cin>>ch1;
			if (c[h[len]][ch1]!='\0')
			{
				h[len]=c[h[len]][ch1];
				continue;
			}
			for (j=1;j<=len;j++)
			if (d[ch1][h[j]]) break;
			if (j<=len) 
			{
				len=0; continue;
			}
			len++; h[len]=ch1;
		}
		cout<<"Case #"<<ca<<": [";
		for (i=1;i<len;i++) cout<<h[i]<<", ";
		if (len>0) cout<<h[len];
		cout<<']'<<endl;
	}
}
