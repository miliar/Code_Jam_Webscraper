#include<vector>
#include<iostream>
#include<algorithm>
#include<set>
#include<queue>
#include<cstring>
#include<string>
#include<map>
#include<fstream>
#include<cmath>
using namespace std;

#define FOR(i,a,b) for(int (i)=(a);(i)<(b);++(i))
#define all(a) (a).begin(),(a).end()
long long calc(long long no)
{
	int total=0;
	while(no>0)
	{
		no/=2;
		total++;
	}
	return total-1;
}
int main()
{
	ifstream fin("C:\\B-large.in");
	ofstream fout("C:\\B-large.out");
	int t;
	fin>>t;
	int rr=1;
	while(rr<=t)
	{
		long long l,p,factor;
		fin>>l>>p>>factor;
		//cout<<l<<" "<<p<<endl;
		long long cur=l*factor;
		long long total=0;
		while(cur<p)
		{
			total++;
			cur*=factor;
		}
		int zz=0;
		if(total==0)
			fout<<"Case #"<<rr<<": "<<zz<<endl;
		else
		{
			int final=calc(total)+1;
			fout<<"Case #"<<rr<<": "<<final<<endl;
		}
		rr++;
	}
}