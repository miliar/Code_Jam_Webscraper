#include <iostream>
#include <malloc.h>

using namespace std;

int main()
{

/** Begin Preprocessing */
	char map[26];
	map['a'-'a'] = 'y'; map['o'-'a'] = 'e'; map['z'-'a'] = 'q'; map['q'-'a'] = 'z';

	char ip[][100] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
	char op[][100] = {"our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"};

	for(int k = 0; k < 3; k ++)
	{
		for(int i = 0; ip[k][i] != '\0'; i ++)
		{
			map[ip[k][i] - 'a'] = op[k][i];
		}
	}

/* Display map
	for(int i = 0; i < 26; i ++)
	{
		cout<<i<<": "<<map[i]<<endl;
	}
*/
/** End preprocessing */

/* Program start */

	int T, count = 0; 
	string input;
	cin>>T;
	cin.ignore();

	while(count++ < T)
	{
		getline(cin, input);
	
		cout<<"Case #"<<count<<": ";	
		for(int i = 0; input[i] != '\0'; i ++)
		{
			if(input[i] == ' ')
				cout<<" ";
			else
				cout<<map[input[i] - 'a'];
		}
		cout<<endl;
	}


	return 0;
}
