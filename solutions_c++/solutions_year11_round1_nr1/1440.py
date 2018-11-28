#include <iostream> 
#include <cmath> 
#include <string> 
#include <cstring> 
#include <set> 
#include <map> 
#include <vector> 
#include <sstream>
#include <cstdio> 
#include <queue>
using namespace std; 
long long gcd(long long a,long long b)
{
	

	return a==0?b:gcd(b%a,a);
}
int main(int argc, char *argv[]) 
{ 
 	freopen("A.txt","r",stdin);
 	freopen("AOUT.txt","w",stdout);
	int T;cin>>T;
	int c=1;
	while(T--)

	{
		long long N;int Pd,Pg;
		cin>>N>>Pd>>Pg;
		
		long long x1=Pd,y1=100,x2=Pg,y2=100;
		long long d=gcd(x1,y1);
		x1/=d;y1/=d;
		if(y1>N||x2<x1||y2<y1||(y2-x2<y1-x1))
		{
			cout<<"Case #"<<c++<<": Broken"<<endl;
		}
		else cout<<"Case #"<<c++<<": Possible"<<endl;
	}  
	  return 0; 
}

