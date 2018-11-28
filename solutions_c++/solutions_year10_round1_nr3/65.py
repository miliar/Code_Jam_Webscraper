#include<iostream>

#include<fstream>


using namespace std;

ifstream in("C.in");
ofstream out("C.out");

const int Max = 1000002;
int lose[1000008];

void computeLose()
{
	lose[1]=1;
	lose[2] = 3;
	for(int i=3;i<Max;i++)
	{
		lose[i] = lose[i-1];
		while(true)
		{
			int big = lose[i]+1;
			int small = i;
			big -= small;
			
			//if( lose) then win and break
			//else lose[i]++ and continue
			if(lose[big]>=small) 
			{
				break;
			}
			else
			{
				lose[i]++;
			}
		}
	}
}


int main()
{
	int T;
	in>>T;
	computeLose();
	
	for(int c=0;c<T;c++)
	{
		int A1,A2,B1,B2;
		in>>A1>>A2>>B1>>B2;
		long long res=0;
		for(int i=B1;i<=B2;i++)
		{
			if(A1>lose[i])
				res += A2-A1+1;
			else if(A2>lose[i])
				res += A2-lose[i];
		}
		for(int i=A1;i<=A2;i++)
		{
			if(B1>lose[i])
				res += B2-B1+1;
			else if(B2>lose[i])
				res += B2-lose[i];

		}


		out<<"Case #"<<c+1<<": "<<res<<"\n";
	}
		
	return 0;
}