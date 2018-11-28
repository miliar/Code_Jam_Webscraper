#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

int main(void){


	char map[256];
	string a[3] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
	string t[3] = {"our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"};

	for (int i=0; i < 3; i++) 
	{
		for ( int pos = 0; pos < a[i].length(); ++pos )
		{
			map[a[i][pos]] = t[i][pos];
		}
	}
	
	map['q'] = 'z';
	map['z'] = 'q';

	int T;	
	cin >> T;
	string googlerese;
	
	
	getline (cin, googlerese, '\n');
	for (int i=0; i < T; i++) 
	{
		getline (cin, googlerese, '\n');
	
		string translation (googlerese);

		for ( int pos = 0; pos < googlerese.length(); pos++ ) {
			translation[pos] = map[googlerese[pos]];			
		}
		
		cout << "Case #" << (i+1) << ": " << translation << "\n";
	}	
}