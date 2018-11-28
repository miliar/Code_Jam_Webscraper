#include <cstdlib>

#include <iostream>
using namespace std;
int gcd(int a,int b)
{
	if(a==1||b==1) return 1;
	if(a==b) return a;
	if(a==0) return b;
	if(b==0) return a;
	if(a>b)
		return gcd(a%b,b);
	else
		return gcd(b%a,a);
}
bool getmintime2()
{
	bool result=false;
	int n,g,d;
	cin>>n>>d>>g;
	if(g==100&&d<100) return result;
	if(g==0&&d>0) return result;
	int number=100/gcd(d,100);
	if((number)<=n)
		return true;
	else
	return false;


	return result;

}

int main(int argc, char* argv[])
{
	int num_test;
	cin>>num_test;
	for(int i=0;i<num_test;i++)
	{
		cout<<"Case #"<<i+1<<": "<<(getmintime2()?"Possible":"Broken")<<"\n";
	}
	return 0;
}

