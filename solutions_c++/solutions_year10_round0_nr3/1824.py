#include<fstream>
using namespace std;
int main()
{
	int done[1000];
	unsigned long long cost[1000];
	int next[1000];
	int g[1000];
	unsigned long long hist[1001];
	int T;

	ifstream fin("C-large.in");
	ofstream fout("C-large.out");

	int i;
	fin>>T;

	for(i=1;i<=T;++i)
	{
		int j;
		for(j=0;j<1000;++j)
		{
			done[j]=-1;
			cost[j]=0;
			next[j]=-1;
			g[j]=-1;
			hist[j]=0;
		}
		int R,k,N;
		fin>>R>>k>>N;
		for(j=0;j<N;++j)
			fin>>g[j];
		int m;
		for(j=0;j<N;++j)
		{
			unsigned long long euro=0;
			int count=0;
			for(m=j;;m=(m+1)%N)
			{
				if(count==N || euro+g[m]>k)
					break;
				else
					euro+=g[m];
				++count;
			}
			cost[j]=euro;
			next[j]=m;
		}
		unsigned long long ans=0;
		int start=0;
		bool cycle=false;
		hist[0]=0;
		int cs;
		for(j=1;j<=R;++j)
		{
			if(done[start]!=-1)
			{
				cycle=true;
				cs=done[start];
				break;
			}
			
			done[start]=j;
			ans+=cost[start];
			start=next[start];
			hist[j]=ans;
		}
		if(cycle)
		{
			int len=j-cs;
			ans=ans + (ans-hist[cs-1]) * ((R-(j-1))/len) + hist[cs-1 + ((R-(j-1))%len)]-hist[cs-1];
		}
			
		fout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}
			
			

