#include <iostream.h>
#include <fstream.h>
#include <list.h>

/*
	Google Code Jam 2012
	Qualification Round
	Problem B. Dancing With the Googlers
*/

#define MAXLEN 5000

int main(int argc, char* argv[])
{
	int T,t;
	int p;
	int S;
	int ti;
	int N,n;
	
	int answer;
	
	char sLine[MAXLEN];
	
	ifstream inFile;
	
	if ( argc < 2 )
	{
		inFile.open("test.in");
	}
	else
	{
		inFile.open(argv[1]);
	}
	
	//inFile.open("A-test.in");
	
	if ( !inFile )
	{
		cout << "Error opening file!" << endl;
		exit(1);
	}
	
	inFile >> T;
	
	inFile.getline(sLine,MAXLEN);

	for (t=0;t<T;t++)
	{
		inFile >> N;
		inFile >> S;
		inFile >> p;
		
		answer = 0;
		
		for (n=0;n<N;n++)
		{
			inFile >> ti;
			
			ti = ti - p;
			
			if ( ti < 0 )
			{
				continue;
			}
			
			if ( ti/2 >= (p-1) )
			{
				// no 'surprises' here :-)
				answer++;
			}
			else if ( ti/2 >= (p-2) )
			{
				// actually check for equality is enough since if it is larger it will be >=(p-1)
				// any 'surprises' left?
				if ( S>0 )
				{
					answer++;
					S--;
				}
			}
			
		}
		
		
		
		cout << "Case #" << t+1 << ": " << answer << endl;
	}
	
	inFile.close();
	return 0;
}