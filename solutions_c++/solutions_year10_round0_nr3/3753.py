#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	ofstream fout("c.out");
	int n;
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		int R,K,N;
		cin>>R>>K>>N;
		int g[N];
		for(int j=0;j<N;j++)
		{
			cin>>g[j];
		}
		int rounds = 0;
		int pos = 0;
		int check = 0;
		unsigned long long int SUM = 0;
		while(rounds < R)
		{
			int sum = 0;
			check = 0;
			while(sum + g[pos] <= K)
			{
				check++;
				sum += g[pos%N];
				pos++;
				pos=pos%N;
				if(check == N)
					break;
			}
			rounds++;
			SUM+=sum;
		}
		fout<<"Case #"<<i<<": "<<SUM<<endl;
	}
	return 0;
}
