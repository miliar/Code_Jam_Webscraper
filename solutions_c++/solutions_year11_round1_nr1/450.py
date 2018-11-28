#include <iostream>
#include <fstream>

using namespace std;
ifstream fin("A-large.in");
ofstream fout("output1.txt");

//#define fin cin
//#define fout cout

long long gcd(long long a,long long b)
{
	if(b==0)return a;
	else return gcd(b,a%b);
}

long long t,n,pd,pg;

int main()
{
	fin>>t;
	for(long long tt=1;tt<=t;tt++){
		fin>>n>>pd>>pg;
		if(pg==100 && pd!=100){
			fout<<"Case #"<<tt<<": Broken"<<endl;
		}
		else if(pg==0 && pd!=0){
			fout<<"Case #"<<tt<<": Broken"<<endl;
		}
		else {
			if(100/gcd(pd,100)<=n) fout<<"Case #"<<tt<<": Possible"<<endl;
			else fout<<"Case #"<<tt<<": Broken"<<endl;
		}
	}
}