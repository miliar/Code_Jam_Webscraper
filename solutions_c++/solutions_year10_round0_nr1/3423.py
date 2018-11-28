#include <iostream>
#include <fstream>

using namespace std;

int main() 
{
	ifstream iff("in.txt");
	int t;
	iff>>t;
	ofstream off("out.txt");
	for(int i=0;i<t;++i)
	{
		int k,n;
		iff>>n>>k;
		if((k+1)%(1<<n)==0)
 			off<<"Case #"<<i+1<<": ON"<<endl;
		else
			off<<"Case #"<<i+1<<": OFF"<<endl;
	}
	iff.close();
	off.close();
}