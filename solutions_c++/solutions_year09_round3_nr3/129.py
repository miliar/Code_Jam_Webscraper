#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int Mem[10005][105];
int Qs[105];
int Q;
int Solve(int Start,int End)
{
	if(Start == End || Start+1>=End)
		return 0;
	if(Mem[Start][End]!=-1)
		return Mem[Start][End];
	int Min = INT_MAX;
	int N = Qs[End] - Qs[Start]-1;
	for(int i=Start+1;i<=End-1;i++)
	{
		int T = N - 1;
		T+=Solve(Start,i);
		T+=Solve(i,End);
		if(T<Min)
			Min = T;
	}
	return Mem[Start][End] = Min;
}
int main()
{
	ifstream cin("d:\\CodeJam.in");
	ofstream cout("d:\\CodeJam.out");
	int k;
	cin>>k;
	for(int i=0;i<k;i++)
	{
		memset(Mem,-1,sizeof(Mem));
		int N;
		cin>>N>>Q;
		for(int j=1;j<=Q;j++)
			cin>>Qs[j];
		Qs[Q+1]=N+1;
		Qs[0]=0;
		cout<<"Case #"<<i+1<<": "<<Solve(0,Q+1)<<endl;
	}
}