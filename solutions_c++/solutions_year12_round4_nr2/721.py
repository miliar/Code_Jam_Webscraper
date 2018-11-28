#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
#define max(a,b) (a > b ? a : b)
#define min(a,b) (a < b ? a : b)
int main()
{
	int T;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>T;
	for(int ind=1;ind<=T;ind++)
	{
		int n,W,L;
		cin>>n>>W>>L;
		int r[1005],t[1005];
		for(int i=0;i<n;i++)
		{cin>>r[i];t[i]=r[i];}
		sort(r,r+n);
		reverse(r,r+n);
		int x[1005],y[1005];
		int tx[1005],ty[1005];
		x[0]=0;y[0]=0;
		int i=1;
		while(i<n && y[i-1]+r[i-1]+r[i]<=L)
		{
			x[i]=0;
			y[i]=y[i-1]+r[i-1]+r[i];
			i++;
		}
		while(i<n && x[i-1]+r[i-1]+r[i]<=W)
		{
			y[i]=L;
			x[i]=x[i-1]+r[i-1]+r[i];
			i++;
		}

		while(i<n && y[i-1]-r[i-1]-r[i]>=0)
		{
			x[i]=W;
			y[i]=y[i-1]-r[i-1]-r[i];
			i++;
		}
		while(i<n && x[i-1]-r[i-1]-r[i]-r[i]>=r[0])
		{
			y[i]=0;
			x[i]=x[i-1]-r[i-1]-r[i];
			i++;
		}
		//printf("Case #%d: %l\n",ind,res);
		cout<<"Case #"<<ind<<":";
		int fl[11];
		memset(fl,0,sizeof(fl));
		for(int i=0;i<n;i++)
		{
			int j=0;
			while(fl[j] || t[i]!=r[j])j++;
			tx[i]=x[j];ty[i]=y[j];fl[j]=1;
		}
		for(int j=0;j<n;j++)cout<<" "<<tx[j]<<" "<<ty[j];
		cout<<endl;
		
	}
}