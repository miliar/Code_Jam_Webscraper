#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

struct col{
	long long p,v;
};

int main()
{
	ifstream fin("input.txt");
	ofstream fout("ouput.txt");
	long long T;
	fin >> T;
	for(long long ca=0;ca<T;ca++)
	{
		long long n,d;
		fin >> n >> d;
		vector<col> all;
		for(long long i=0;i<n;i++)
		{
			col newc;
			fin >> newc.p >> newc.v;
			all.push_back(newc);
		}
		vector <long long> go;
		long long dnow=all[0].p;
		for(long long i=0;i<all.size();i++)
		{
			if (all[i].p>dnow)
				dnow=all[i].p;
			while(all[i].v>0)
			{
				go.push_back(dnow-all[i].p);
				all[i].v--;
				dnow+=d;
			}
		}
		long long min=go[0],max=go[0];
		for(long long i=1;i<go.size();i++)
		{
			if (go[i]>max)
				max=go[i];
			if (go[i]<min)
				min=go[i];
		}
		fout << "Case #" << ca+1 << ": " << 
			(max-min)/2;
		if ((max-min)%2==1)
			fout << ".5";
		fout << "\n";
	}
}