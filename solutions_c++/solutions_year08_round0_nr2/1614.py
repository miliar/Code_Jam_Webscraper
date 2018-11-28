#include<iostream>
#include<fstream>
#include<map>
#include<string>
#include<sstream>
using namespace std;
string Arr[105];
string Q[1005];
int N,M;
int Mem[1005][105];
int Solve(int QPos,int SPos)
{
	if(QPos==M)
		return 0;
	if(Mem[QPos][SPos]!=-1)
		return Mem[QPos][SPos];
	int Min=-1;
	if(Q[QPos]==Arr[SPos])
	{
		int T;
		for(int i=0;i<N;i++)
			if(i!=SPos)
			{
				T=Solve(QPos,i);
				if(T<Min || Min==-1)
					Min=T;
			}
		return Mem[QPos][SPos]=1+Min;
	}
	return Mem[QPos][SPos]=Solve(QPos+1,SPos);
}
int main()
{
	ifstream cin("c:\\A-large.in");
	ofstream cout("c:\\test.out");
	int S;
	string In;
	stringstream SS;
	getline(cin,In);
	SS<<In;
	SS>>S;
	int Count=1;
	while(S--)
	{
		memset(Mem,-1,sizeof(Mem));
		SS.clear();
		getline(cin,In);
		SS<<In;
		SS>>N;
		for(int i=0;i<N;i++)
		{
			getline(cin,Arr[i]);
		}
		SS.clear();
		getline(cin,In);
		SS<<In;
		SS>>M;
		for(int i=0;i<M;i++)
			getline(cin,Q[i]);
		int Min=-1;
		for(int i=0;i<N;i++)
		{
			int T=Solve(0,i);
			if(T<Min || Min==-1)
				Min=T;
		}
		cout<<"Case #"<<Count<<": "<<Min<<endl;
		Count++;
	}
	cout<<"Done"<<endl;
	return 0;
}
