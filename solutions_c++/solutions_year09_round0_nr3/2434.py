#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <math.h>

using namespace std;

string phrase = "welcome to code jam";
char line0[507];
string line;
int match;

void parser(int ind, int letter)
{
	while( letter <= 18 && ind < (int) line.size() )
	{
		if(line[ind] == phrase[letter] )
		{
			
			if( letter == 18 )
			{
				//cout << phrase[letter] << " " << ind << endl;
				match++;
				if(ind >= (int) line.size())
					return;	
				//else
				//	parser(ind+1,letter);		
			}
			else //more phrase to find
			{
			
				parser(ind+1,letter+1);
			
			
			
			}
		
		
		}
		//else	
		//	parser(ind+1,letter);
		
		
	
	
	
	
		//return;
		ind = ind + 1;
	}


}


int main()
{
	match = 0;
	int n;
	cin >> n;
	cin.getline(line0,505);
	for(int i = 1; i <= n ; i++)
	{
	
	
		cin.getline(line0,505);
		line = line0;
		//cout << line << "$$" << endl;
		parser(0,0);
		match = match % 10000;
		
		cout << "Case #" << i << ": ";
		if(match < 10) 
			cout << "000";
		else if(match < 100)
			cout << "00";
		else if(match < 1000)
			cout << "0";
		cout << match << endl;
		match = 0;
	
	
	
	}
	
	
	
	return 0;
	
	
}
