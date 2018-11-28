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
long long gcd(long long a,long long b)
{
	long long temp;
	while(1)
	{
		if(b==0) return a;
		else
		{
			temp=b;
			b=a%b;
			a=temp;
		}
	}
}

long long lcm(long long a,long long b)
{
	return (a*b)/gcd(a,b);
}
#define FOR(i,a,b) for(int (i)=(a);(i)<(b);++(i))
#define all(a) (a).begin(),(a).end()
int main()
{
	ifstream fin("C:\\B-small.in");
	ofstream fout("C:\\B-smal.out");
	int t;
	fin>>t;
	int rr=1;
	while(rr<=t)
	{
		int n;
		fin>>n;
		vector<long long> no(n);
		vector<long long> diff;
		long long temp;
		FOR(i,0,n)
		{
			fin>>temp;
			no[i]=temp;
			FOR(j,0,i)
			{
				long long tt=no[i]-no[j];
				if(tt<0) tt=-tt;
				diff.push_back(tt);
			}
		}
		long long ans=diff[0];
		long long sz=diff.size();
		FOR(i,0,sz)
		{
			ans=gcd(ans,diff[i]);
		}
		long long left;
		if(no[0]%ans==0) left=0;
		else left=ans-(no[0]%ans);
		fout<<"Case #"<<rr<<": "<<left<<endl;
		rr++;
	}

}