#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;



int main()
{
	ifstream in("C:\\Users\\German\\Documents\\Visual Studio 2005\\Projects\\Problemas\\A-large.in");
	//ifstream in("sample.in");
	ofstream out("C:\\Users\\German\\Documents\\Visual Studio 2005\\Projects\\Problemas\\sol.out");
	int T;
	in >> T;
	getline(in, string());
	for(int t=1; t<=T; t++)
	{
		int N, K;
		in >> N >> K;
		unsigned int snapperChain = 1 << N;
		string res;
		if ((K % snapperChain) == snapperChain-1)
			res = "ON";
		else
			res = "OFF";

		out << "Case #" << t << ": " << res << endl;


	}
	system("pause");
	return 0;
}
