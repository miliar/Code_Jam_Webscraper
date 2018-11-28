#include <fstream>
#include <deque>

using namespace std;

int main()
{
	deque<unsigned long long int> tq;
	unsigned long long int R,k,n,T,temp,sum,poz,total;

	ifstream f("C-small.in");
	ofstream f2("output.out");

	f>>T;
	for(int TEST=0;TEST<T;TEST++)
	{
		f>>R>>k>>n;
		total=0;
		tq.clear();
		for(int i=0;i<n;i++)
		{
			f>>temp;
			tq.push_back(temp);
		}
		for(unsigned long long int i=0;i<R;i++)
		{
			sum=0;
			poz=0;
			while(poz<n && sum+tq[poz]<=k)
			{
				if(sum+tq[poz]<=k)
				{
					sum+=tq[poz];
					poz++;
				}
			}
			for(int i=0;i<poz;i++)
			{
				tq.push_back(tq[0]);
				tq.pop_front();
			}
			total+=sum;
		}
		f2<<"Case #"<<TEST+1<<": "<<total<<endl;
	}

	f.close();
	f2.close();
	return 0;
}