#include <iostream>
#include <algorithm>
using namespace std;

int T,PD,PG;
long long N;
int gcd(int a,int b)
{
	return b?gcd(b,a%b):a;
}
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	cin>>T;
	for (int Te=1;Te<=T;++Te)
	{
		cin>>N>>PD>>PG;
		cout<<"Case #"<<Te<<": ";
		if (PD>PG && !PG || PD<PG && PG==100 || (long long)(100/gcd(PD,100))>N)	cout<<"Broken"<<endl;
		else	cout<<"Possible"<<endl;
	}
	return 0;
}
