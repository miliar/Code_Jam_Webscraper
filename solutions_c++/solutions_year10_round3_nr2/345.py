#include<iostream>
#include<fstream>
using namespace std;
int findk(int L, int C , int P)	{
	int k = 0;
	while(L < P)	{
		L = L*C;
		k++;
	}
	return k;

}
int results[32];
int main()	{
	ofstream fout("out.txt");
	ifstream fin("in.txt");
	int answers[1001];
	int T;
	fin>>T;
	__int64 L,P,C;
	for(int i = 0; i <32; i++)
		results[i] = 0;
	results[2] = 1;
	for(int i = 2; i <32; i++)	{
		int t = i/2;
		if(i%2 !=0)
			t++;
		
		results[i] = results[t]+1;
		//cout<<i<<" "<<results[i]<<endl;

	}

	for(int i = 1; i <= T; i++)		{
		fin>>L>>P>>C;
		int k = 0;
		while(L < P)	{
			L = L*C;
			k++;
		}
		cout<<i<<" "<<k<<endl;
		answers[i] = results[k];


	}

	for(int i = 1; i <= T; i++)	{
		fout<<"Case #"<<i<<": "<<answers[i]<<endl;
		cout<<"Case #"<<i<<": "<<answers[i]<<endl;
	}
	fout.close();
	return 0;
}