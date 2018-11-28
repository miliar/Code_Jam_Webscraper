#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

ifstream in("C.in");
ofstream out("C.txt");

int main()
{
	int T;
	in>>T;
	for (int t=1; t<=T; t++)
	{
		int times, capacity, group, people[1000];
		in>>times>>capacity>>group;
		for (int i=0; i<group; i++)
			in>>people[i];
		
		long long sum[group];
		int next[group];
		for (int i=0; i<group; i++)
		{
			sum[i]=people[i];
			int j=(i+1)%group;
			while (j!=i)
			{
				if (sum[i]+people[j]<=capacity)
					sum[i]+=people[j];
				else
					break;
				j=(j+1)%group;
			}
			next[i]=j;
		}
		
		long long total=0;
		int pos=0;
		for (int i=0; i<times; i++)
		{
			total+=sum[pos];
			pos=next[pos];
		}
		
		out<<"Case #"<<t<<": "<<total<<endl;
	}
    return 0;
}
