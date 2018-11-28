#include<iostream>
#include<fstream>
#include<queue>
using namespace std;

int main(int argc, char *argv[])
{
	ifstream input(argv[1]);
	ofstream out("Problem1.out");
	int t;
	input >> t;
	for(int h=0;h<t;h++)
	{
		unsigned long long n,k;
		input >> n >> k;
		int x = k+1;
		int left = 1;
		for(int i=0;i<n;i++)
			left *= 2;
		if(x%left==0)
			out << "Case #" << h+1 << ": ON" << endl;
		else
			out << "Case #" << h+1 << ": OFF" << endl;
	}
}
