#include <iostream>

using namespace std;

//#define _DEB_

char tt[26] = {
                'y', // <--a
                'h', // <--b
                'e', // <--c
                's', // <--d
                'o', // <--e
                'c', // <--f
                'v', // <--g
                'x', // <--h
                'd', // <--i
                'u', // <--j
                'i', // <--k
                'g', // <--l
                'l', // <--m
                'b', // <--n
                'k', // <--o
                'r', // <--p
                'z', // <--q
                't', // <--r
                'n', // <--s
                'w', // <--t
                'j', // <--u
                'p', // <--v
                'f', // <--w
                'm', // <--x
                'a', // <--y
                'q'  // <--z
              }
              ;

const int maxTextLen = 100;
int main()
{
	//cout << "Hello!!!" << endl;
	//return 0;
	int T;
	char res[maxTextLen+1], G[maxTextLen+1];

	cin >> T;
	cin.ignore(maxTextLen,'\n');
	for(int t=1; t<=T; t++)
	{
	        #ifdef _DEB_ 
	           cout << "Test " << t << endl;
	        #endif
		/************************************
		*	Input Data
		*************************************/
		cin.getline(G,maxTextLen+1);
	        #ifdef _DEB_ 
		   cout << "G = " << G << endl;
		#endif
		/************************************
		*	Solve the Problem
		*************************************/
		for(int i=0; res[i]=G[i]; i++)
		{
		   if('a'<=G[i] && G[i]<='z')
		      res[i] = tt[G[i]-'a'];
		}
		/************************************
		*	Output Results
		*************************************/
		cout << "Case #" << t << ": " << res << endl;
	}

	return 0;
}
