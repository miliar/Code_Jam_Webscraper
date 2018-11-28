#include <fstream>
using namespace std;
ifstream fin("large_case.in");
ofstream fout("large_case.out");
int main()
{
	int T,N;
	int values[1001];
	int i,j;
	fin>>T;

	for (i=0;i<T;i++)
	{	
		int min=1000001;
		int temp=0;
		int sum=0;
		fin>>N;
		for (j=0;j<N;j++)
		{
			fin>>values[j];
			if (values[j]<min)
			{
				min=values[j];
			}
			sum+=values[j];
			temp=temp^values[j];
		}
		if (temp==0)
		{
			fout<<"Case #"<<i+1<<": "<<sum-min<<endl;
		}
		else
		{
			fout<<"Case #"<<i+1<<": "<<"NO"<<endl;
		}
	}
	return 0;
}