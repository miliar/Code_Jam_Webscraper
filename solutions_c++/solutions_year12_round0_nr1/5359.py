#include <iostream>
#include <stdio.h>
#define cases 31
using namespace std;



int main()
{
	char cypher[] = {'y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u', 'o',
					 'm', 'x', 's', 'e', 'v', 'z', 'p', 'd', 'r', 'j', 'g',
					 't', 'h', 'a', 'q'};
	FILE *fptr;
	fptr = fopen("input.txt", "r");
	if (fptr == NULL)
		return -1;
	for (int i = 0; i < cases; i++)
	{
		char string[200];
		char newstring[200];
		fgets (string, 101, fptr);
		char *strptr;
		strptr = string;
		int j = 0;
		while (*strptr != '\n' && *strptr != '\0')
		{
			
			if (*strptr == ' ')
			{
				newstring[j] = ' ';
				j++;
				strptr++;
			}
			int k = 0;
			while ( cypher[k] != *strptr )
			{
				k++;
			}
			char b = (char)(k + 97);
			newstring[j] = b;
			j++;
			strptr++;
		}
		newstring[j] = '\0';
		if ( i+1 < 7)
			cout << "Case #" << i+1 << ": " << newstring << endl;
		if ( i+1 > 7)
			cout << "Case #" << i << ": " << newstring << endl;
	}

	system("Pause");
	return 0;
}