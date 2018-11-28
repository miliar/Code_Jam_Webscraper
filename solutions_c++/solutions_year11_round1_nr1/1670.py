

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

string answer(long int N, int a, int b)
{
	if(a == 100 && b == 0)
		return "Broken";
	else if(b == 0 && a != 0)
		return "Broken";
	else if (b == 100 && a != 100)
		return "Broken";
	else
	{

	bool t = false;
	long int p;
	//long in q;
	
	for(long int i = 1; i <= N; i++)
	{
		p = i*a;
		if(p % 100 ==0  )
		{
			//q = p / 100; 

			t = true;
			break;
		}

	}
	if(t)
	{
		return "Possible";
	}
	}

	return "Broken";
}

int main()
{
	ifstream in("A-small-attempt2.in");
	ofstream out("A-small-attempt2.out");
	
	
	string s;
	int T;

	in >> T;
	getline(in ,s);
	int i;
	long int N; 
	int a, b;
	for(i = 0; i < T; i++)
	{
		in >> N >> a >> b;

		out << "Case #" << i+1 << ": " << answer(N, a, b) << endl;	
		getline(in, s);
	}


	return 0;
}