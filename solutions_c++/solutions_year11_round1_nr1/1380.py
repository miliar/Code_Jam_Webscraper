#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
using namespace std;

int gcd(int A,int B)
{
	return B==0 ? A : gcd(B,A%B);
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int TC;
	cin>>TC;
	for(int tc = 1 ; tc<=TC ; ++tc)
	{
		int N,PD,PG;
		cout<<"Case #"<<tc<<": ";
		cin>>N>>PD>>PG;
		int GC = gcd(PD,100);
		bool flag = (PG==100 || PG==0)&&(PG!=PD);
		if(100/GC <= N && !flag)cout<<"Possible"<<endl;
		else cout<<"Broken"<<endl;	
	}
	return 0;
}