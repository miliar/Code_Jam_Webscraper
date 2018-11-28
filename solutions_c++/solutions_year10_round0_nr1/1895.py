#include <fstream>
using namespace std;
int main()
{
	unsigned int t,n,k;
	unsigned int b;
	ifstream in("A-large.in");
	ofstream out("result.txt");
	in>>t;
	for (int i=0;i<t;i++){
		in>>n>>k;
		b=(1<<n)-1;
		if ((k&b)==b)
			out<<"Case #"<<i+1<<": "<<"ON"<<endl;
		else
			out<<"Case #"<<i+1<<": "<<"OFF"<<endl;
	}
	return 0;
}