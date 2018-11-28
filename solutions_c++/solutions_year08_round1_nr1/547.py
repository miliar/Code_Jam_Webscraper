
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <iostream>
#include <algorithm>
#include <conio.h>
using namespace std;

vector<long long> a;
vector<long long> b;


void main()
{
	ifstream inf("A-large.in");		//large
	ofstream outf("A-large.out");

	int i;
	int N;
	inf >> N;
	int time;
	for (time=0; time <N; time++)
	{
		a.clear();
		b.clear();
		int t;
		int len;
		inf >> len;
		for (int i=0; i<len; i++)
		{
			inf >> t;
			a.push_back(t);
		}
		for (int i=0; i<len; i++)
		{
			inf >> t;
			b.push_back(t);
		}
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());

		long long re = 0;
		for (int i=0; i<len; i++)
		{
			re += a[i] * b[len-i-1];
		}

		outf << "Case #" << time+1 << ": " << re << endl;
	}

	inf.close();
	outf.close();
	getch();
}
