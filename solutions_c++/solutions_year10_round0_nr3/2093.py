#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int main()
{
	ifstream infile("C:\\Users\\qingpingw\\Desktop\\c-small.in");
	ofstream outfile("C:\\Users\\qingpingw\\Desktop\\c-small.txt");
	int test;
	int R,N,K;
	int i,j;
	int sum=0;
	int count=0;
	int temp;
	int num[1005];
	infile>>test;
	i=1;
	while(i<=test)
	{
		infile>>R>>K>>N;
		count=0;
		temp=0;
		for(j=0;j<N;j++)
		{
			infile>>num[j];
			temp+=num[j];
		}
		j=0;
		sum=0;
		if(temp>K)
		{
			while(R)
			{
				j=j%N;
				if((sum+num[j])<=K)
				{
					sum=sum+num[j];
				}
				else
				{
					count+=sum;
					sum=num[j];				
					R--;
				}
				j++;

			}
		}
		else
			count=R*temp;
		
		outfile<<"Case #"<<i<<": "<<count<<endl;
		i++;

	}
	system("pause");
	return 0;
}


