#include <iostream>
#include <algorithm>
using namespace std;
int R,k,N;
int g[1001];
long long ans=0;
void doit()
{
	int pos=0;
	long long tmp=0;
	for(int i=0;i<R;i++)
	{
		int t=0;
		while(tmp+g[pos]<=k&&t<N)
			tmp+=g[pos],pos++,pos%=N,t++;
		ans+=tmp;
		tmp=0;
	}
}
int main ()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		ans=0;
		cin>>R>>k>>N;
		for(int i=0;i<N;i++)
		{	
			scanf("%d",&g[i]);
		}
		doit();
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}


	return 0;
}
