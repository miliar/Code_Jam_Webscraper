#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>
#include<conio.h>

using namespace std;

int n, m;

int main(void)
{
	int i, j, k, t, tt;

	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );

	scanf( "%d\n", &tt );
	for( t = 1; t <= tt; ++ t )
	{
		printf( "Case #%d:", t );
		string s;
		getline(cin, s, '\n');	
		char match[27]="yhesocvxduiglbkrztnwjpfmaq";		
		char ch;
		printf(" ");
		for(i=0; i<s.length(); ++i)
		{
			ch = s[i];
			if( ch == ' ' )
				cout << " ";
			else			
				cout << match[(int)ch - 97];
		}
		printf("\n");
	}
	getch();
	return 0;
}
