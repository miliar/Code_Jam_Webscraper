#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	ofstream fout("output");
	int n;
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		//cout<<i<<endl;
		int R,K,N;
		cin>>R>>K>>N;
		int g[N];
		for(int j=0;j<N;j++)
		{
			cin>>g[j];
		}
		unsigned long long int sum_arr[N][2];
		int pos = 0;
		int check = 0;
		unsigned long long int sum = 0;
		for(int j=0;j<N;j++)
		{
			pos = j;
			sum = 0;
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
			
			sum_arr[j][0] = sum;
			sum_arr[j][1] = pos;
		}		
		 
		pos = 0;
		unsigned long long int SUM = 0;
		for(int j=0;j<R;j++)
		{
			SUM += sum_arr[pos][0];
			pos = sum_arr[pos][1];
		}
		fout<<"Case #"<<i<<": "<<SUM<<endl;
	}
	return 0;
}
