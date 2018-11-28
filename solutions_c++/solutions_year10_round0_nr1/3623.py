#include<fstream>
using namespace std;
inline long int square(long int n)
{
	return n*n;
}
long int fastpower(int n)
{
	if(n==0)
		return 1;
	if(n%2==0)
		return square(fastpower(n/2));
	return 2*square(fastpower(n/2));
}
int main()
{
	ifstream in;
	in.open("A-large.in");
	ofstream out;
	out.open("A-large.out");
	long int n,t;
	long int k;
	in>>t;
	for(int i=0;i<t;i++)
	{
		in>>n>>k;
		out<<"Case #"<<i+1<<": ";
		if((k+1)%(fastpower(n))==0)
			out<<"ON\n";
		else
			out<<"OFF\n";
	}
	return 0;
}