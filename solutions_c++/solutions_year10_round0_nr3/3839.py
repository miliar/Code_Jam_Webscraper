#include<iostream>
#include<fstream>
#include<queue>
using namespace std;

int main()
{
	queue<long> Grps,t;
	long r,k,n;
	long c;
	long tmp;

	long money;
	long sum;

	ifstream file;
	ofstream file1;

	file.open("C-small-attempt0.in");
	file1.open("output.txt");

	file>>c;

	for(long i=0;i<c;i++)
	{
		file>>r;
		file>>k;
		file>>n;

		money=0;

		for(long j=0;j<n;j++)
		{
			file>>tmp;
			Grps.push(tmp);
		}

		sum=0;

		while(r>0)
		{
			while(!Grps.empty() && (Grps.front()+sum)<=k)
			{
				sum+=Grps.front();
				tmp=Grps.front();
				Grps.pop();

				t.push(tmp);
			}

			while(!t.empty())
			{
				Grps.push(t.front());
				t.pop();
			}

			money+=sum;
			sum=0;
			r--;
		}

		while(!Grps.empty())
		{
			Grps.pop();
		}

		while(!t.empty())
		{
			t.pop();
		}

		file1<<"Case #"<<i+1<<": "<<money<<endl;

	}

	return 0;
}