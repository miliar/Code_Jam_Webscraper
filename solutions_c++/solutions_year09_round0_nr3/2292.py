#include<iostream>
#include<string>
#include<fstream>
using namespace std;
string Wel = "welcome to code jam";
string S;
int Mem[50][600];
int Solve(int Pos1,int Pos2)
{
	if(Mem[Pos1][Pos2]!=-1)
		return Mem[Pos1][Pos2];
	if(Pos1 == Wel.length())
		return 1;
	if(Pos2==S.length())
		return 0;
	int Sum = 0;
	if(Wel[Pos1]==S[Pos2])
		Sum += Solve(Pos1+1,Pos2+1);
	Sum = (Sum + Solve(Pos1,Pos2+1))%10000;
	return Mem[Pos1][Pos2]=Sum;
}
int main()
{
	ifstream cin("CodeJam.in");
	ofstream cout("CodeJam.out");
	int N;
	cin>>N;
	getline(cin,S);
	for(int i=0;i<N;i++)
	{
		memset(Mem,-1,sizeof(Mem));
		getline(cin,S);
		int T= Solve(0,0);
		cout<<"Case #"<<i+1<<": ";
		if(T<1000)
			cout<<"0";
		if(T<100)
			cout<<"0";
		if(T<10)
			cout<<"0";
		cout<<T<<endl;
	}
}