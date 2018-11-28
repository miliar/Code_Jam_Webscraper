#include <string>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <sstream>
# include<fstream>
using namespace std;
# define FOR(i,a,n) for(int i=a;i<n;++i)
# define REP(i,n) FOR(i,0,n)
typedef long long LL;
ifstream fin("B-large.in");
ofstream fout("out.txt");
LL ar[1000005];
vector<LL> v;
int main()
{
	int tc;
	fin>>tc;
	int cnt=0;
	while(tc--)
	{
		v.clear();
		++cnt;
		LL l,t,n,c,sum=0;
		fin>>l>>t>>n>>c;
		REP(i,c) fin>>ar[i];
		FOR(i,c,n) ar[i]=ar[i-c];
		int st=-1;
		REP(i,n) 
		{
			if(sum+ar[i]*2>t)
			{
				st=i;
				break;
			}
			else sum+=ar[i]*2;
		}
		if(st==-1) 
		{
			fout<<"Case #"<<cnt<<": "<<sum<<endl;
		}
		else
		{
		int p;
		if(sum<t) 
		{
			p=st+1;
		}
		else p=st;
		FOR(i,p,n) v.push_back(ar[i]);
		if(sum<t) 
		{
			v.push_back(ar[st]-(t-sum)/2);
			sum+=(t-sum);
		}
		sort(v.begin(),v.end(),greater<int>());
		int m=v.size();
		REP(i,m)
		{
			if(l) 
			{
				sum+=v[i];
				--l;
			}
			else
			{
				sum+=2*v[i];
			}
		}
		fout<<"Case #"<<cnt<<": "<<sum<<endl;
	}
	}
}
		
		
				
		

		
