#include <iostream>

using namespace std;

int main()
{
	int TestCases;
	int NoButtons;
	
	int OCount=0,BCount=0;
	int OPos=1,BPos=1;
	int Seconds=0;
	
	char Order[100];
	int Orange[100];
	int Blue[100];
	
	cin >> TestCases;
	
	for(int i=0;i < TestCases;i++)
	{
		cin >> NoButtons;
		
		int O=0,B=0,Pushed=0,OAction=0,BAction=0;
		
		OCount=0,BCount=0;
		OPos=1,BPos=1;
		Seconds=0;
		
		for(int j=0;j < NoButtons;j++)
		{
			cin >> Order[j];
			
			if(Order[j] == 'O')
				cin >> Orange[OCount++];
			else
				cin >> Blue[BCount++];
		}
		
		while(Pushed < NoButtons)
		{
			Seconds++;
			
			OAction=0;
			BAction=0;
			
			if(OPos < Orange[O])
			{
				OPos++;
				OAction=1;
			}
				
			else if(OPos > Orange[O])
			{
				OPos--;	
				OAction=1;
			}
			
			if(BPos < Blue[B])
			{
				BPos++;
				BAction=1;
			}
				
			else if(BPos > Blue[B])
			{
				BPos--;
				BAction=1;
			}
				
			if(OPos == Orange[O] && Order[Pushed] == 'O' && OAction == 0)
			{
				Pushed++;
				O++;
				continue;
			}
			
			if(BPos == Blue[B] && Order[Pushed] == 'B' && BAction == 0)
			{
				Pushed++;
				B++;
			}
		}		
		
		cout<<"\nCase #"<<(i+1)<<": "<<Seconds;
	}
} 
