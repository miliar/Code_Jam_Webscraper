# include<iostream>
# include<fstream>
# include<vector>
# include<algorithm>
# include<set>
using namespace std;
# define FOR(i,a,n) for(int i=a;i<n;++i)
# define REP(i,n) FOR(i,0,n)
char r[200];
int p[200];
ifstream fin("A-large.in");
ofstream fout("out.txt");
typedef long long LL;
int main()
{
	int tc;
	fin>>tc;
	int cnt=0;
	while(tc--)
	{
		LL ans=0;
		++cnt;
		int n;
		fin>>n;
		REP(i,n) fin>>r[i]>>p[i];
		int o=1,b=1;
		LL ot=0,bt=0;
		REP(i,n)
		{
			if(r[i]=='O')
			{
				ot=max(ans,ot+abs(p[i]-o));
				ot=max(ot,ans)+1;
				o=p[i];
			}
			else
			{
				bt=max(ans,bt+abs(p[i]-b));
				bt=max(bt,ans)+1;
				b=p[i];
			}
			ans=max(ot,bt);
		}
		fout<<"Case #"<<cnt<<": "<<ans<<endl;
	}
		
		
}
	
	
	

