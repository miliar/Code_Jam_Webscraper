#include <stdio.h>
#include <iostream>
using namespace std;

main()
{
	char c;
	int cases;
	int count;
	cin >> cases;
	count = 1;
	c = getchar(); // get rid of new line
	cout << "Case #" << count << ": ";
	while((c = getchar()) != EOF)
	{
		if(c != '\n')
		{
			switch(c)
			{
			   case 'a': c = 'y';
				     break;		
			   case 'b': c = 'h';
				     break;		
			   case 'c': c = 'e';
				     break;		
			   case 'd': c = 's';
				     break;		
			   case 'e': c = 'o';
				     break;		
			   case 'f': c = 'c';
				     break;		
			   case 'g': c = 'v';
				     break;		
			   case 'h': c = 'x';
				     break;		
			   case 'i': c = 'd';
				     break;		
			   case 'j': c = 'u';
				     break;		
			   case 'k': c = 'i';
				     break;		
			   case 'l': c = 'g';
				     break;		
			   case 'm': c = 'l';
				     break;		
			   case 'n': c = 'b';
				     break;		
			   case 'o': c = 'k';
				     break;		
			   case 'p': c = 'r';
				     break;		
			   case 'q': c = 'z';
				     break;		
			   case 'r': c = 't';
				     break;		
			   case 's': c = 'n';
				     break;		
			   case 't': c = 'w';
				     break;		
			   case 'u': c = 'j';
				     break;		
			   case 'v': c = 'p';
				     break;		
			   case 'w': c = 'f';
				     break;		
			   case 'x': c = 'm';
				     break;		
			   case 'y': c = 'a';
				     break;		
			   case 'z': c = 'q';
				     break;
			   default : break;
			}
			cout << c;
		}
		else
		{
			count++;
			cout << endl;
			if(count <= cases)
				cout << "Case #" << count << ": ";
		}
	}
}
