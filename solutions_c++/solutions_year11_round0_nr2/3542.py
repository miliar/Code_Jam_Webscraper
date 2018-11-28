#include <iostream>

using namespace std;

char String[100];
char FinalString[100];
char Combinations[36][3];
char Oppositions[28][3];

int C,D,N,F;
int End=0;
	
int Check()
{
	for(int x=F-1;x > 0;x--)
	{
		for(int a=0;a < C;a++)
		{
			if( (FinalString[x] == Combinations[a][0] && FinalString[x-1] == Combinations[a][1]) || 
			(FinalString[x] == Combinations[a][1] && FinalString[x-1] == Combinations[a][0]) )
			{
				F--;
				FinalString[--F] = Combinations[a][2];
				F++;
				break;
			}
		}
	}
	
	if(D >= 1)
	{
		for(int x=0;x < F;x++)
		{
			for(int a=0;a < D;a++)
			{
				if( FinalString[x] == Oppositions[a][0] )
				{
					for(int y=0;(y < F && y != x);y++)
					{
						if( FinalString[y] == Oppositions[a][1] )
							return 1;
					}
				}
		
				if( FinalString[x] == Oppositions[a][1] )
				{
					for(int y=0;(y < F && y != x);y++)
					{
						if( FinalString[y] == Oppositions[a][0] )
							return 1;
					}
				}
			}
		}
	}
	
	return 0;
}

int main()
{
	int TestCases;
	
	cin >> TestCases;
	
	for(int i=0;i < TestCases;i++)
	{
		F=0;
		
		for(int j=0;j < 100;j++)
			FinalString[j]=NULL;
		
		cin >> C;
		
		for(int j=0;j < C;j++)
			cin >> Combinations[j][0] >> Combinations[j][1] >> Combinations[j][2];
		
		cin >> D;
		
		for(int j=0;j < D;j++)
			cin >> Oppositions[j][0] >> Oppositions[j][1];
			
		cin >> N;
		 	
		for(int j=0;j < N;j++)
			cin >> String[j];
			
		for(End=1;End <= N;End++)
		{
			FinalString[F++]=String[End-1];
			
			if( Check() == 1)
			{
				F=0;
				for(int r=0;r < F;r++)
					FinalString[r]=NULL;
			}
		}
		
		cout << "Case #" << (i+1) << ": [";
		
		for(int j=0;j < F;j++)
		{
			cout << FinalString[j];
			if(j != (F-1) )
				cout<<", ";
		}
		
		cout << "]\n";
	}
	
	return 0;
}
