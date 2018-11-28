#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>
#include <list>
#include <set>
using namespace std;

int main(int argc, char **argv)
{
	ifstream ifstr("C:\\Documents and Settings\\login\\Desktop\\small.in");
	int nC;
	ifstr >> nC;
	ofstream ofstr("small.out");
	for (int i = 1; i <= nC; i++)
	{
		__int64 N = 0;
		__int64 K = 0;
		ifstr >> N >> K;
		bool flag = true;
		for (int j = 0; j < N; j++)
		{
			if (!((1<<j)&K))
				flag = false;
		}

		if (flag)
			ofstr << "Case #" << i << ": ON" << endl;
		else
			ofstr << "Case #" << i << ": OFF" << endl;
	}
	return 0;
}


