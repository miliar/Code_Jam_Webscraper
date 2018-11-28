#include<fstream>
#include<iostream>
using namespace std;

int main()
{
	ifstream cin("B-small.in");
	ofstream cout("A-small.out");
	int tests;
	cin>>tests;
	for(int c = 0; c < tests; c++)
	{
		cout <<"Case #"<<c+1<<": "<< '\n';
	}
	cin.close();
	cout.close();
	return 0;
}