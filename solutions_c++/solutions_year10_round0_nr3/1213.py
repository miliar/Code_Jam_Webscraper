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
	ifstream fin("C:\\C-smal.in");
	ofstream fout("C:\\C-smalll.out");
	int t;
	fin>>t;
	int rr=1;
	while(rr<=t)
	{
		long long r,k,n;
		fin>>r>>k>>n;
		vector<long long> v;
		long long temp;
		FOR(i,0,n) 
		{
			fin>>temp;
			v.push_back(temp);
		}
		vector<long long> visit(n,0);
		map<long long,long long> m;
		vector< long long > final;
		vector<long long> in(n,0);
		int cur=0;
		long long left=k;
		long long ans=0;
		long long roundsleft=r;
		while(!visit[cur])
		{
			long long temp=cur;
			long long total=0;
			left=k;
			FOR(i,0,n) in[i]=0;
			while(left>=v[cur] && !in[cur])
			{
				in[cur]=1;
				left-=v[cur];
				total+=v[cur];
				cur=(cur+1)%n;
			}
			visit[temp]=1;
			int index=final.size();
			m[temp]=index;						//Associate the beggining group no of a round with the no of people during the round 
			final.push_back(total);
		}
		long long loopsize=final.size()-m[cur];
		long long initsize=m[cur];
		long long accumulated=0;
		roundsleft-=initsize;
		if(roundsleft<0) initsize=r;
		FOR(i,0,initsize) ans+=final[i];		//Accumulate the earnings before the loop of rounds
		if(roundsleft<0)						// No Loop
		{
			cout<<"Case #"<<rr<<": "<<ans<<endl;
			continue;
		}
		FOR(i,m[cur],m[cur]+loopsize)			//Accumulate earnings in the loop of rounds
			accumulated+=final[i];
		long long rounds=(roundsleft)/loopsize;		//Calculate total number of loops encountered in R rounds
		ans+=accumulated*rounds;
		long long remains=roundsleft%loopsize;		//No of elements in the final incomplete loop
		FOR(i,m[cur],m[cur]+remains)				//Accumulate elements in incomplete loop
				ans+=final[i];
		fout<<"Case #"<<rr<<": "<<ans<<endl;
		rr++;
	}
}