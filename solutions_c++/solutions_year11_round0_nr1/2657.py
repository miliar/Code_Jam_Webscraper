#include <iostream.h>
#include <fstream.h>

// Code Jam 2011
// Qualification Round
// A. Bot Trust



int main(int argc, char *argv[])
{
	int T,t;
	int N,n;
	
	int answer;
	int activepos;
	int idlepos;
	int pos;
	
	int delta;
	
	char bot;
	
	char lastbot;
	
	int idleturns;
	
	ifstream inFile;
	
	//inFile.open("test.in");
	if ( argc < 2 )
	{
		cout << "No input file given!" << endl;
		exit(1);
	}
	inFile.open(argv[1]);
	if ( !inFile )
	{
		cout << "Error opening file!" << endl;
		exit(1);
	}
	
	inFile >> T;
	
	for (t=0;t<T;t++)
	{
		inFile >> N;
		
		idlepos = 1;
		
		inFile >> bot;
		
		inFile >> pos;
		
		
		answer = pos;
		activepos = pos;
		lastbot = bot;
		idleturns = pos;
		
		//cout << "bot: " << bot << ", activepos: " << activepos << ", idlepos: " << idlepos << ", pos: " << pos << ", answer: " << answer << endl;
		
		for (n=1;n<N;n++)
		{
			inFile >> bot;
			inFile >> pos;
			if ( bot==lastbot )
			{
				if ( activepos - pos < 0 )
				{
					delta = pos-activepos;
				}
				else
				{
					delta = activepos-pos;
				}
				delta++; // the push
				answer = answer + delta;
				idleturns = idleturns + delta;
				activepos = pos;
			}
			else
			{
				if ( idlepos - pos < 0 )
				{
					delta = pos-idlepos;
				}
				else
				{
					delta = idlepos-pos;
				}
				delta++; // thepush
				
				if ( idleturns >= delta )
				{
					answer = answer + 1;
					idleturns = 1;
				}
				else
				{
					answer = answer + delta-idleturns;
					idleturns = delta-idleturns;
				}
				
				idlepos = activepos;
				activepos = pos;
				
				lastbot = bot;
			}
			
			//cout << "bot: " << bot << ", activepos: " << activepos << ", idlepos: " << idlepos << ", pos: " << pos << ", answer: " << answer << endl;
			
		}
		
		cout << "Case #" << t+1 << ": " << answer << endl;
	}
		
		
	
	inFile.close();
	return 0;
}