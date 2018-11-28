# include <iostream>
# include <vector>
# include <algorithm>
# include <fstream>

using namespace std;

struct sums{
	long long sum;
	int next;
};


sums sumsi[1001]={0};

void compute(int k,int N,int g[])
{
	long long s = 0;
	int c = 0;

	int j = 0;
	for(int i = 0;i<N;i++)
	{
		s = 0;
		c = 0;
		j = i;
		while(s+g[j]<=k && c<N)
		{
			s+=g[j];
			j = (j+1)%N;
			c++;
		}
		
		sumsi[i].sum=s;
		sumsi[i].next=j;
	}


}


int main()
{
	int T,cas=0;
	ifstream in("C-large.in");
	ofstream out("out3");

	in>>T;

	while(T--)
	{
		int R,k,N;
		int g[1001]={0};

		in>>R>>k>>N;

		for(int i = 0;i<N;i++)
		{
			in>>g[i];
		}
	
		compute(k,N,g);

		long long int sum = 0;

		int j = 0;
		for(int i = 0;i<R;i++)
		{
			sum+=sumsi[j].sum;
			j = sumsi[j].next;

		}
		
		out<<"Case #"<<++cas<<": "<<sum<<endl;
	
	}

return 0;

}

