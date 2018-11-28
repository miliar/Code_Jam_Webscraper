#include <map>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

ifstream inf;
ofstream outf;
const int maxx = 2000;
int main(void){
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	inf.open("input.txt");
	outf.open("output.txt");
	int n; // входные данные
	vector <bool> isp(maxx+10, true);
	isp[0] = isp[1] = false;
	for (int i=2; i<maxx; i++)
		if (isp[i])
		{
			for(int j = i*2; j < maxx;j+=i)
				isp[j] = false;
		}

	int tests;
	inf >> tests;
	long long minn, maxa;
	minn = 0;
	maxa = 0;
	for (int test = 0; test < tests; test++)
	{	
		long long n;
		inf >> n;		
		minn = 0;
		maxa = 0;
		if(n!= 1)
		{
			maxa++;
		for (long long i = 2; i <= n; i++)
			if (isp[i])
			{
				long long j = i;
				int power = 1;
				while (j <= n)
				{
					j*=i;
					power++;
				}
				power--;
				minn++;
				maxa+=power;		

			}
		}
		


		outf << "Case #" << test+1 << ": " << maxa - minn << endl;		

	
	}

	outf.close();
	return 0;
}

