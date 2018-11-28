#include<iostream>
#include<string>
#include<algorithm>
#include<cmath>
#include<fstream>
using namespace std;

char Arr[50][50];

bool Occupied[50];
struct Row
{
	int Pos,End;
};
Row Rows[50];
int N;
void Swap(int Pos,int Pos2)
{
	int Step = ((Pos2>Pos)?1:-1);
	for(int i=Pos;i!=Pos2;i+=Step)
	{
		Row T = Rows[i];
		Rows[i]=Rows[i+Step];
		Rows[i+Step]=T;
	}
}
int Solve(int Pos)
{
	if(Pos == N-1)
		return ((Rows[Pos].End<=Pos)?0:-1);
	
	int Min = -1;
	if(Rows[Pos].End<=Pos)
		Min = Solve(Pos+1);
	for(int i=Pos+1;i<N;i++)
	{
		if(Rows[i].End <= Pos)
		{
			Swap(i,Pos);
			int T = Solve(Pos+1);
			if(Min==-1 && T!=-1)
				Min = T+i-Pos;
			if(T!=-1)
				Min = min(T+i-Pos,Min);
			Swap(Pos,i);
		}
	}
	return Min;
}
int main()
{
	ifstream cin("d:\\codejam.in");
	ofstream cout("d:\\codejam.out");
	int K;
	cin>>K;
	for(int Case = 1; Case<=K;Case ++)
	{

		
		cin>>N;
		memset(Rows,0,sizeof(Rows));
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<N;j++)
			{
				cin>>Arr[i][j];
				if(Arr[i][j]=='1')
				{
					Rows[i].End=j;
					Rows[i].Pos = i;
				}
			}
		}
		int Cost = Solve(0);
		/*
		for(int i=0;i<N;i++)
		{
			
			int Min = INT_MAX;
			int Pos = 0;
			for(int j=i;j<N;j++)
			{
				if(Rows[j].End <= i)
				{
					Pos = j;
					break;
				}
			}
				for(int j=Pos;j>i;j--)
				{
					Row T = Rows[j];
					Rows[j]=Rows[j-1];
					Rows[j-1] = T;
					Cost++;
				}
			
		
		}*/
		cout<<"Case #"<<Case<<": "<<Cost<<endl;
	}
}