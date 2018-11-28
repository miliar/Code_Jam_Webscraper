
#include <iostream>
using namespace std;
int r,gs;
long long w;
int g[1001];
int next[1001];
long long wt[1001];
void calcs()
{
	long long s[2001];
	s[0]=0;
	for (int i=1;i<=2*gs;i++)
	{
		
		s[i]=s[i-1]+((i>gs)?g[i-gs]:g[i]);

	}

	for (int i=1;i<=gs;i++)
	{
		next[i]=i;
		for (int j=i;j<=i+gs-1;j++)
		{
			
			if (s[j]-s[i-1]>w)
			{
				if (j>gs)
					next[i]=j-gs;
				else
					next[i]=j;
				break;
				
			}
			wt[i]=s[j]-s[i-1];
		}
	
		
	}

}
void getans(int cs)
{
	int p=1;
	long long ans=0;
	while (r--)
	{
		ans+=wt[p];
		p=next[p];
	}
	cout<<"Case #"<<cs<<": "<<ans<<endl;
}
int main() {
	freopen("c-large.in","r",stdin);
	freopen("c-large.out","w",stdout);
	int tn,cs;
	cin>>tn;
	cs=tn;
	while (cs--)
	{
		cin>>r>>w>>gs;
		for (int i=1;i<=gs;i++)
			cin>>g[i];
		calcs();
		getans(tn-cs);
	}
	return 0;
}
