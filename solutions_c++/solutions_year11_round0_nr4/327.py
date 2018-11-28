#include <iostream>
#include <map>
#include <cmath>
using namespace std;

const int N=1100;

int t;
int n;
double ans;
double f[N];
int a[N];
bool visit[N];

void dfs(int x, int y)
{
//	cout<<"x y: "<<x<<" "<<y<<endl;
	if (visit[x]) 
	{
		ans+=f[y];
		return;
	}
	visit[x]=true;
	dfs(a[x], y+1);
}

int main()
{	
	freopen("d.in", "r",stdin);	
	freopen("d.txt", "w",stdout);
	f[0]=f[1]=0;
	for(int i=2; i<N; ++i)
	{
		f[i]=1;
		for(int j=1; j<i; ++j)
		{
			f[i]+= f[j];
		}	  
		f[i]*=2;
		f[i]=f[i]/(i-1);
//		cout<<i<<"  "<<f[i]<<endl;
    }    
    

	cin>>t;
	for(int L=1; L<=t; ++L)
	{
		cin>>n;
		for(int i=1; i<=n; ++i)
		{
			cin>>a[i];	
			visit[i]=false;
		}	
		ans=0;
		for(int i=1; i<=n; ++i) dfs(i, 0);
		cout.unsetf( ios::fixed );
		cout<<"Case #"<<L<<": ";
		cout.setf( ios::fixed );
		cout.precision(6);
		cout<<ans<<endl;
	}	
}
