#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <string.h>
#include <complex>


using namespace std;


char 
get_letter(char c)
{
    switch ( c ) {
    case 'a' :
	return 'y';
	break;
    case 'b' :
	return 'h';
	break;
    case 'c' :
	return 'e';
	break;
    case 'd' :
	return 's';
	break;
    case 'e' :
	return 'o';
	break;
    case 'f' :
	return 'c';
	break;
    case 'g' :
	return 'v';
	break;
    case 'h' :
	return 'x';
	break;
    case 'i' :
	return 'd';
	break;
    case 'j' :
	return 'u';
	break;
    case 'k' :
	return 'i';
	break;
    case 'l' :
	return 'g';
	break;
    case 'm' :
	return 'l';
	break;
    case 'n' :
	return 'b';
	break;
    case 'o' :
	return 'k';
	break;
    case 'p' :
	return 'r';
	break;
    case 'q' :
	return 'z';
	break;
    case 'r' :
	return 't';
	break;
    case 's' :
	return 'n';
	break;
    case 't' :
	return 'w';
	break;
    case 'u' :
	return 'j';
	break;
    case 'v' :
	return 'p';
	break;
    case 'w' :
	return 'f';
	break;
    case 'x' :
	return 'm';
	break;
    case 'y' :
	return 'a';
	break;
    case 'z' :
	return 'q';
	break;

    default :
	cout << "never here !" << endl;
	break;
    }
    
    return 'a';
}


int
main (void)
{
    int step;
    cin >> step;
    char dump[200];
    cin.getline(dump, 200);
    for(int i = 0; i<step; i++)
    {
	char temp[200];
	cin.getline(temp,200);
	
	cout << "Case #" << i+1 << ": ";
	for(int l=0; l<strlen(temp); l++)
	{
	    if(temp[l] == ' ')
		cout << ' ';
	    else
		cout << get_letter(temp[l]);

	}
	cout << endl;
    }

    return 0;
}
