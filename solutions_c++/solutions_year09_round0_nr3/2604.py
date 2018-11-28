#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

int main()
{

	int N ; 
	cin>> N ; 

	string s = "welcome to code jam" ; 
	int D[22][502]; 

	char c ; 
	cin.get(c) ; 
	for(int n = 1 ; n <= N ; n++)
	{
		string str ; 
		getline(cin, str) ; 
		
		memset(D, 0 , sizeof(D)) ; 

		int i ; 
		for(i = 0 ; i <= str.size() ; i++)
			D[0][i] = 1 ; 
		
		for(i = 1 ; i <= s.size() ; i++)
		{	
			for(int j = 1 ; j <= str.size() ; j++)
			{
				if(s[i-1] == str[j-1])
				{
					D[i][j] = D[i-1][j] + D[i][j-1] ; 
				}
				else
					D[i][j] = D[i][j-1] ; 
				D[i][j] = D[i][j]%10000 ; 
			}
		}
		printf("Case #%d: %04d\n", n ,D[s.size()][str.size()] ) ; 
	}
	return 0 ; 
}