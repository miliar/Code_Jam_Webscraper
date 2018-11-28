#include<fstream>
#include<iostream>
using namespace std;

int add(const int& a, const int& b)
{
	return (a|b)-(a&b);
}

int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");

	int t,v[2000];
	in>>t;
	for(int i=0;i<t;i++)
	{
		int n;
		in>>n;
		for(int j=0;j<n;j++)
			in>>v[j];
		int suma1,suma2,minim;
		suma1=v[0];
		suma2=v[0];
		minim=v[0];
		for(int j=1;j<n;j++)
		{
			suma1=add(suma1,v[j]);
			suma2+=v[j];
			if(v[j]<minim)
				minim=v[j];
		}
		if(suma1!=0)
			out<<"Case #"<<i+1<<": "<<"NO\n";
		else
			out<<"Case #"<<i+1<<": "<<suma2-minim<<"\n";
	}
	in.close();
	out.close();
}

