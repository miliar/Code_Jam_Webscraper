#include<iostream>
#include<fstream>
using namespace std;

//Patrick's calculation is XOR

int main()
{
	ifstream fin("C.in");
	ofstream fout("C.out");
	
	//1 <= T <= 100
	//1 <= C <= 10^6
	//N(max) = 1000;
	int T,N,tmp,sum,min,max;
	int C[1010] ={0};

	fin>>T;
	
	for(int i = 1;i <= T; i++)
	{
		fin>>N;
		sum = 0;
		max = 0;
		for(int j = 1;j <= N; j++)
			{
			fin>>C[j];
            sum = sum^C[j];
            }
        
		fout<<"Case #"<<i<<": ";
		if(sum == 0)
		{
			min = 1000010;
			tmp = 0;
			for(int i = 1;i <= N;i++)
				if(C[i] < min)
				{
					min = C[i];
					tmp = i;
				}
			for(int i= 1;i <= N;i++)
				if(i != tmp)
					max += C[i];
				
			fout<<max<<endl;
		}
		else fout<<"NO"<<endl;
	}
	
	return 0;
}
