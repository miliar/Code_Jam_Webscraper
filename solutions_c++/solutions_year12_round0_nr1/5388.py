/* Enter your code here. Read input from STDIN. Print output to STDOUT */
#include <iostream> 
#include <string> 
#include <vector> 
#include <map> 
#include <stdio.h> 
#include <stdio.h>
#include <stdlib.h>
#include <limits>

using namespace std; 

char conv [] = { 'y','h','e','s','o','c','v',   'x'  ,'d','u','i','g','l','b','k','r',  'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q' }; 
char conv2 [] = { 'y','h','e','s','o','c','v',   'z'  ,'d','u','i','g','l','b','k','r',  'x', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q' }; 

string process (string s)
	{
	string p = ""; 
	for (unsigned int k=0;k<s.length();k++)
		{
		if (s[k] != ' ')
			p += conv[s[k]-'a'];
		else
			p += ' ';
		}
	return p;
	}

int main () 
	{ 	
	int t; 
	cin >> t; 
	cin.clear(); // ignore erroneous line of input:
	cin.ignore(numeric_limits<streamsize>::max(), '\n');
	for(int i=0;i<t;i++)
		{
		string s; 
		getline (cin, s);
		cout << "Case #" << (i+1) << ": " << process(s) << endl; 
		}
	return 0; 
	} 
