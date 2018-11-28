#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;

bool myfunction (int i,int j) { return (i<j); }
int main ()
{
	int T,N,C,sum,xor;
	ifstream in ("C-large.in");
	ofstream out ("output.txt");
	in>>T;
	vector<int>candy;
	for (int i=1;i<=T;i++)
	{
		in>>N;
		candy.clear();
		in>>C;
		xor=C;
		sum=C;
		candy.push_back(C);
		for (int k=1;k<N;k++)
		{
			in>>C;
			candy.push_back(C);
			sum+=C;
			xor=xor^C;
		}
		sort(candy.begin(),candy.end(),myfunction);
		out<<"Case #"<<i<<": ";
		if (xor==0)
		{
			sum-=candy[0];
			out<<sum<<endl;
		}
		else
			out<<"NO"<<endl;
	}
	return 0;
}