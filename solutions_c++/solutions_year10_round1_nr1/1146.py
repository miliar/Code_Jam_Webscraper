#include<vector>
#include<iostream>
#include<algorithm>
#include<set>
#include<queue>
#include<cstring>
#include<string>
#include<map>
#include<fstream>
using namespace std;

#define FOR(i,a,b) for(int (i)=(a);(i)<(b);++(i))
#define all(a) (a).begin(),(a).end()
int main()
{
	ifstream fin("C:\\A-large.in");
	ofstream fout("C:\\A-large.out");
	int t;
	fin>>t;
	int rr=1;
	while(rr<=t)
	{
		int m,n,K;
		fin>>n>>K;
		//cout<<n<<" "<<K<<endl;
		m=n;
		vector< vector<int> > v(n,vector<int>(n));
		vector< vector<int> > final(n+1,vector<int>(n+1));
		vector<vector<int> > rright(n,vector<int>(n,0));
		
		
		FOR(i,0,n)
			FOR(j,0,n)
		{
			char temp;
			fin>>temp;
			if(temp=='.') v[i][j]=0;
			else if(temp=='R') v[i][j]=1;
			else v[i][j]=2;
		}
		FOR(i,0,n)
			FOR(j,0,n)
		{
			int total=0;
			FOR(k,j,n)
			{
				if(v[i][k]>0) total++;
			}
			rright[i][j]=total;
		}

		FOR(i,0,n)
			FOR(j,0,n)
		{
			final[i][n-rright[i][j]]=v[i][j];
		}
		int prev=-1;
		int done1=0,done2=0;
		int total=0;
		total=0;
		prev=-1;
		FOR(i,0,n)
		FOR(j,0,n)
		{
			total=0;
			FOR(k,0,K)
			{
				if(i>=n || j+k>=n) continue;
				int a;
				if(final[i][j+k]==prev) total++;
				else total=1;
				if(total==K)
				{
					if(final[i][j]==1){done1=1;}
					else if(final[i][j]==2) {done2=1;}
				}
				prev=final[i][j+k];
			}
		}
		total=0;
		prev=-1;
		
		FOR(i,0,n)
		FOR(j,0,n)
		{
			total=0;
			FOR(k,0,K)
			{
				if(i+k>=n || j>=n) continue;
				int a;	
				if(final[i+k][j]==prev) total++;
				else total=1;
				if(total==K)
				{
					if(final[i][j]==1){ done1=1;}
					else if(final[i][j]==2) {done2=1;}
				}
				prev=final[i+k][j];
			}
		}
		total=0;
		prev=-1;
		FOR(i,0,n)
		FOR(j,0,m)
		{
			total=0;
			FOR(k,0,K)
			{
			if(i+k>=n || j+k>=m) continue;
			int a;	
			if(final[i+k][j+k]==prev) total++;
			else total=1;
			if(total==K)
			{
				if(final[i][j]==1){ done1=1;}
				else if(final[i][j]==2) {done2=1;}
			}
			prev=final[i+k][j+k];
			}
		}
		FOR(i,0,n)
			FOR(j,0,m)
		{
			total=0;
			FOR(k,0,K)
			{
			if(i+k>=n || j+k>=m) continue;
			int a;	
			if(final[i+k][j+k]==prev) total++;
			else total=1;
			if(total==K)
			{
				if(final[i][j]==1){ done1=1;}
				else if(final[i][j]==2) {done2=1;}
			}
			prev=final[i+k][j+k];
			}
		}
		total=0;
		prev=-1;
		FOR(i,0,n)
			FOR(j,0,m)
		{
			total=0;
			FOR(k,0,K)
			{
				if(i-k<0 || j-k<0) continue;
				int a;
				if(final[i-k][j-k]==prev) total++;
				else total=1;
				if(total==K)
				{
					if(final[i][j]==1) done1=1;
					else if(final[i][j]==2) done2=1;
				}		
				prev=final[i-k][j-k];
			}
		}
		total=0;prev=-1;
		FOR(i,0,n)
		FOR(j,0,m)
		{
			total=0;
			FOR(k,0,K)
			{
				if(i+k>=n || j-k<0) continue;
				int a;
				if(final[i+k][j-k]==prev) total++;
				else total=1;
				if(total==K)
				{
					if(final[i][j]==1) done1=1;
					else if(final[i][j]==2) done2=1;
				}		
				prev=final[i+k][j-k];
			}
		}
		total=0;prev=-1;
		FOR(i,0,n)
		FOR(j,0,m)
		{
			total=0;
			FOR(k,0,K)
			{
				if(i-k<0 || j+k>=n) continue;
				int a;
				if(final[i-k][j+k]==prev) total++;
				else total=1;
				if(total==K)
				{
					if(final[i][j]==1) done1=1;
					else if(final[i][j]==2) done2=1;
				}		
				prev=final[i-k][j+k];
			}
		}
		if(done1==1 && done2==1) fout<<"Case #"<<rr<<": "<<"Both"<<endl;
		else if (done1==1) fout<<"Case #"<<rr<<": "<<"Red"<<endl;
		else if(done2==1) fout<<"Case #"<<rr<<": "<<"Blue"<<endl;
		else fout<<"Case #"<<rr<<": "<<"Neither"<<endl;
		rr++;
	}
}