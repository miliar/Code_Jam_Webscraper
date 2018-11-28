#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main()
{
	unsigned int tests;
	char input[100];
	char google[27] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','\0'};
	char english[27]= {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q','\0'};
	unsigned short int inputLength;
	
	cin >> tests;
	cin.ignore();
	
		for(int i = 1; i <= tests; i++)
		{
			
			gets(input);
			
			inputLength = strlen(input);
			
			for(int letter=0; letter < inputLength; letter++)
			{
				for(int find=0; find < 26; find++)
				{
					if(input[letter] == google[find])
					{
						input[letter] = english[find];
						break;
					}
					
				}
				
			}
			
				
			cout << "Case #" << i << ": ";
			cout << input;
			
			if(i < tests)
				cout << endl;
			
		}
	
	return 0;	
}
