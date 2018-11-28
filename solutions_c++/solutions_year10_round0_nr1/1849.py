#include <iostream>
#include <cstdio>
#define PATH "/home/tushar/Desktop/"
#define INPUTFILE PATH "A-large.in"
#define OUTPUTFILE PATH "A-large.out"
using namespace std;

int main()
{
	freopen(INPUTFILE,"r",stdin);
	freopen(OUTPUTFILE,"w",stdout);
	int T,N,K;
	cin>>T;
	for(int i=1;i<=T;++i)
	{
		cin>>N>>K;
		bool flag = true;
		for(int j=0;j<N;++j)
			flag &= (1 & (K>>j));
		cout<<"Case #"<<i<<": "<<((flag)?"ON":"OFF")<<endl;
		}
	return 0;
	}
