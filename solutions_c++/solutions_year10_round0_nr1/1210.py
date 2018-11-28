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
	ofstream fout("C:\\Al.out");
	int t;
	fin>>t;
	int rr=1;
	while(rr<=t)
	{
		long long n,k;
		fin>>n>>k;
		long long no=2;
		if(k==0) {fout<<"Case #"<<rr<<": OFF"<<endl; rr++; continue;}
		long long i=2;
		while(i<=n)
		{
			no*=2;
			i++;
		}
		cout<<no<<endl;
		if(k%no==no-1)fout<<"Case #"<<rr<<": ON"<<endl;
		else fout<<"Case #"<<rr<<": OFF"<<endl;
		rr++;
	}
}