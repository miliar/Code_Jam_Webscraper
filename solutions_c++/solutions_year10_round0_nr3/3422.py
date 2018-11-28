#include <iostream>
#include <map>
#include <sstream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <set>

using namespace std;

int T,R,k,N;
vector<int> v;

long long f()
{
	int at=0;
	map<int, int> round;
	map<int, long long> profit;
	int end;
	long long P=0;

	int i=0;
	for(; i<R; i++)
	{	
		if(round.count(at)) {end=i; break;}
		round[at]=i;
		profit[at]=P;

		long long p=0;
		for(int j=0; j<N and p+v[at]<=k; p+=v[at], at=(at+1)%N, j++);
		P+=p;
	}

	if(i==R) return P;

	int c=end-round[at];
	long long cp=P-profit[at];
	long long ret=((R-round[at])/c)*cp+profit[at];
	R=(R-round[at])%c;
	
	for(i=0; i<R; i++)
	{	
		long long p=0;
		for(int j=0; j<N and p+v[at]<=k; p+=v[at], at=(at+1)%N, j++);
		ret+=p;
	}
	return ret;
}

int main(int argc, char** argv)
{
	cin>>T;
	for(int i=0; i<T; i++)
	{
		cin>>R>>k>>N;
		v.clear();
		for(int j=0; j<N; j++)
		{
			int g;
			cin>>g;
			v.push_back(g);
		}
		cout<<"Case #"<<i+1<<": "<<f()<<endl;
	}
	return 0;
}
