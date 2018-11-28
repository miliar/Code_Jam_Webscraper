# include<iostream>
# include<fstream>
# include<vector>
# include<algorithm>
# include<set>
using namespace std;
# define FOR(i,a,n) for(int i=a;i<n;++i)
# define REP(i,n) FOR(i,0,n)
ifstream fin("D-large.in");
ofstream fout("out.txt");
typedef long long LL;
bool seen[10000];
int ar[10000],place[10000];
int main()
{
	int tc;
	fin>>tc;
	int cnt=0;
	while(tc--)
	{
		int ans=0;
		++cnt;
		int n;
		fin>>n;
		REP(i,n) 
		{
			fin>>ar[i];
			--ar[i];
		}
		REP(i,n) place[ar[i]]=i;
		memset(seen,false,sizeof(seen));
		REP(i,n)
		if(!seen[i])
		{
			int num=ar[i],t=0;
			while(!seen[num])
			{
				seen[num]=true;
				num=place[num];
				++t;
			}
			if(t>1) ans+=t;
		}
		fout<<"Case #"<<cnt<<": "<<ans<<endl;
	}
}
			
			
