

#include <iostream>

using namespace std;

char g[] = "yhesocvxduiglbkrztnwjpfmaq";


int main()
{
	int T, i;
	char c;
	
	cin >> T;
	scanf("%c", &c); // get rid of newline character after T
	
	for(i = 1; i <= T; i++)
	{

		string s;
		
		
		
		
		scanf("%c", &c);

		while( c != '\n')
		{			
			if( c == ' ')
			{
				s += c;
			}
			
			else
			{
				s += g[c - 0x61];
			}
			
			scanf("%c", &c);
		}
		
		cout << "Case #" << i << ": " << s << endl;
	}
}

