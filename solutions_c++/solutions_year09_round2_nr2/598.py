#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main ()
{
	int T = 0;
	cin>>T;
	string current;
	for(int i = 0; i < T; i++)
	{
		cin>>current;
		current = "0" + current;
		next_permutation(current.begin(),current.end());
	//	cout<<"current = "<<current<<endl;
		if(current[0] == '0')
		{
			cout<<"Case #"<<i+1<<": ";
			for(int j = 1; j < current.length(); j++)
				cout<<current[j];
			cout<<endl;
		}
		else
			cout<<"Case #"<<i+1<<": "<<current<<endl;
	}
	return 0;
}

