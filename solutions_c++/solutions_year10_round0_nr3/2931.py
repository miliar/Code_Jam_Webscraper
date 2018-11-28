#include<iostream>
#include<fstream>
#include<queue>
using namespace std;

int main(int argc, char *argv[])
{
	ifstream input(argv[1]);
	ofstream out("Problem3.out");
	int t;
	input >> t;
	for(int h=0;h<t;h++)
	{
		long long r,k,n;
		input >> r >> k >> n;
		int *person = new int[n];
		queue<int> a,b;
		for(long i=0;i<n;i++)
		{	
			input >> person[i];
			a.push(person[i]);
		}
        unsigned long long cost = 0;
		for(unsigned int i=0;i<r;i++)
		{
			int remain = k;
			int numg = n;
			while(1)
			{
				if(a.empty())
				{
					while(!b.empty())
					{
						int tmp = b.front();
						b.pop();
						a.push(tmp);
					}
				}
				int now = a.front();
				numg--;
				remain -= now;
				if(remain<0)
				{
					remain += now;
					break;
				}
				if(numg>0)
				{
					a.pop();
					b.push(now);
				}
				else if(numg==0)
				{
					a.pop();
					b.push(now);
					break;
				}
			}
			cost += k-remain;
		}
		out << "Case #" << h+1 << ": " <<  cost << endl;
	}
}
