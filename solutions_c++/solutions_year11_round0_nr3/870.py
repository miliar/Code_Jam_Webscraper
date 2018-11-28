# include<iostream>
# include<fstream>
# include<vector>
# include<algorithm>
# include<set>
using namespace std;
# define FOR(i,a,n) for(int i=a;i<n;++i)
# define REP(i,n) FOR(i,0,n)
ifstream fin("C-large.in");
ofstream fout("out.txt");
typedef long long LL;
LL ar[10000];
int main()
{
	int tc;
	fin>>tc;
	int cnt=0;
	while(tc--)
	{
		++cnt;
		int n;
		LL val=0,ans=0;
		fin>>n;
		REP(i,n) 
		{
			fin>>ar[i];
			val^=ar[i];
		}
		if(val) fout<<"Case #"<<cnt<<": NO"<<endl;
		else
		{
			sort(ar,ar+n);
			FOR(i,1,n) ans+=ar[i];
			fout<<"Case #"<<cnt<<": "<<ans<<endl;
		}
	}
}
		
			
	
	
	

