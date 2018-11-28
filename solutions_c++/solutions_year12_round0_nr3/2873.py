#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <stack>

using namespace std;

vector<string> intToStr( int a )
{
	vector<string> b;
	string temp = "";
	
	while( a != 0 )
	{
		temp.push_back( (char)((a%10)+'0') );
		a/=10;
	}
	
	string str = "";
	
	for (int i = temp.size()-1; i >= 0 ; i--)
	{
		str.push_back( temp[i] );
	}
	
	for (int i = 0; i < str.size()-1; i++)
	{
		for (int j = str.size()-1; j > 0; j--)
		{
			char c = str[j];
			str[j] = str[j-1];
			str[j-1] = c;
		}
		
		if( str[0] == '0' )
			continue;
		
		b.push_back(str);
	}
	
	return b;
}

int strToInt( string a )
{
	int b = 0;
	
	for (int i = 0; i < a.size(); i++)
	{
		b *= 10;
		b += ( (int)(a[i]-'0') );
	}
	
	return b;
}

int main(){	
	
	int T;
	cin >> T;
	
	for (int o = 1; o <= T; o++)
	{
		int count = 0;
		
		int A,B;
		
		cin >> A >> B;
		
		for (int i = A; i <= B; i++)
		{		
			vector<string> str;
			
			str = intToStr( i );
			
			int jj[str.size()];
			
			for (int j = 0; j < str.size(); j++)
			{
				jj[j] = strToInt( str[j] );
			}

			for (int j = 0; j < str.size(); j++)
			{		
				if( i < jj[j] && jj[j] >=A && jj[j] <= B )					
					count++;
			}
		}
		
		cout << "Case #" << o << ": " << count << endl;
	}
	
	return 0;
}

