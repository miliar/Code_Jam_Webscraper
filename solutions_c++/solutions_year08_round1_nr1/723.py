#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

void main()
{
	int T, n;
	long re = 0;
	istream &in = cin;
	//ostream & out = cout;
	ofstream out("out.txt");
	in>>T;
	for(int i = 0; i < T; ++ i)
	{
		in>>n;
		vector<int> v1(n);
		vector<int> v2(n);
		for(int j = 0; j < n; ++ j) in>>v1[j];
		for(int j = 0; j < n; ++ j) in>>v2[j];
		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end());
		re = 0;
		for(int j = 0; j < n ;++ j) re += v1[j] * v2[n-1-j];
		out<<"Case #"<<i+1<<": "<<re<<endl;

	}
	out.close();
	system("pause");
}