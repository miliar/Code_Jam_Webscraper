#include<iostream>
#include<fstream>
	using namespace std;
int main()
{
	ifstream in;
	ofstream out;
	in.open("A-large.in");
	out.open("out.txt");
	int T,n,k;
	long long  a;
	in>>T;
	int s=1;
	while (T--)
	{
		in>>n>>k;
		a=1<<n;
		if ((k+1)%a==0) out<<"Case #"<<s<<": ON"<<endl;
		else out<<"Case #"<<s<<": OFF"<<endl;
		s++;
	}
	in.close();
	out.close();
	return 0;
}