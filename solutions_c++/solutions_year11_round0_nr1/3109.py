#include <iostream>
using namespace std;

int t;
int o[110],b[110],no,nb;
char x;
bool g[110];

int main()
{

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for (int qw=0; qw<t; qw++) 
	{
		int z,n,ans=0;
		no=nb=1;
		o[0]=b[0]=1;
		scanf("%d ",&n);
		for (int i=1; i<=n; i++)
		{
			scanf("%c %d ",&x,&z);
			if (x=='O') { o[no++]=z;g[i-1]=0;}
			else { b[nb++]=z; g[i-1]=1;}
		}
		int k1,k2,buf1=0,buf2=0; k1=k2=1;
		for (int i=0; i<n; i++)
		{
			if (g[i]) {
				z=max(1,abs(b[k1]-b[k1-1])+1-buf2);
				ans+=z;
			buf1+=z; k1++; buf2=0;}
			else {
				z=max(1,abs(o[k2]-o[k2-1])+1-buf1);
				ans+=z;
			buf2+=z; k2++; buf1=0;}
		}
		printf("Case #%d: %d\n",qw+1,ans);
	}
	return 0;
}