#include<iostream>
#include<fstream>
using namespace std;

int g[1010];
long long s[2020];
int next[1010];
long long ans;
int t,r,k,n;

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("C-large.in");
	fout.open("C-large.out");

	fin>>t;
	for (int i=1;i<=t;i++)
	{
		s[0]=0;
		fin>>r>>k>>n;
		for (int j=1;j<=n;j++)
		{
			fin>>g[j];
			s[j]=s[j-1]+g[j];
		}
		for (int j=1;j<=n;j++)
		{
			s[j+n]=s[j+n-1]+g[j];
		}
		for (int j=1;j<=n;j++)
		{
			int now=j;
			while ((now-j+1<=n)&&(s[now]-s[j-1]<=k))
				++now;
			next[j]=now;
		}
		int now=1;
		ans=0;
		for (int j=0;j<r;++j)
		{
			ans+=s[next[now]-1]-s[now-1];
			now=(next[now]-1)%n+1;
		}
		fout<<"Case #"<<i<<": "<<ans<<endl;
	}
	fout.close();
	//system("pause");
	return 0;
}

