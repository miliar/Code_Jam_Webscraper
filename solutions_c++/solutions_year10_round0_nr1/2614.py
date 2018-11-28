#include <iostream>
#include <fstream>
using namespace std;
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)

void main()
{
	ifstream fin("b.in");
	ofstream fout("z.in");

	int k,n,t;
	int on;
	fin>>t;
	int i;
	rep(i,t)
	{
		fin>>n>>k;
		k++;
		on=0;
		if(k==1)
		{
			fout<<"Case #"<<i+1<<": OFF"<<endl;
			continue;
		}
		while(k%2==0)
		{
			k=k/2;
			n--;
			if(n==0)
			{
				on=1;
				break;
			}
		}
		if(on==1)
			fout<<"Case #"<<i+1<<": ON"<<endl;
		else
			fout<<"Case #"<<i+1<<": OFF"<<endl;
	}
	
	return;
}