#include<iostream>
#include<fstream>
using namespace std;
int main()	{
	ofstream fout("out.txt");
	ifstream fin("in.txt");

	int answers[101];
	int a[1001],b[1001];
	int T,N;

	fin>>T;
	for(int i = 1; i <= T; i++)		{
		fin>>N;
		cout<<N<<endl;
		int count = 0;

		for(int j = 0; j <N; j++)
			fin>>a[j]>>b[j];
		for(int j = 0; j < N; j++)	{
			for(int k =0; k < j; k++)	{
				if((a[j] - a[k])*(b[j] - b[k]) <0)
					count++;

			}
		}
		answers[i] = count;



	}

	for(int i = 1; i <= T; i++)	{
		fout<<"Case #"<<i<<": "<<answers[i]<<endl;
		cout<<"Case #"<<i<<": "<<answers[i]<<endl;
	}
	fout.close();
	return 0;
}