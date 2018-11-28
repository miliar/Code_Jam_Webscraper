// tongues.cpp : Defines the entry point for the console application.
//

#include <string>
#include <iostream>
#include <map>

using namespace std;


int main()
{

	string sin = "ejp mysljylc kd kxveddknmc re jsicpdrysi" \
		"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" \
		"de kr kd eoya kw aej tysr re ujdr lkgc jv";
	
	string sout =
		"our language is impossible to understand" \
		"there are twenty six factorial possibilities" \
		"so it is okay if you want to just give up";
	
	map<char,char> dic;
	
	for(int i = 0, n = sin.size(); i < n; ++i)
		dic[sin[i]] = sout[i];
	
/* 	for(int i = 'a'; i <= 'z'; ++i)
 * 		if(dic.find((char)i) == dic.end())
 * 			cout << (char)i << endl;
 */

	dic['q'] = 'z';
	dic['z'] = 'q';
	dic[' '] = ' ';
	
	int t;
	cin >> t;
  string nothing;
  getline(cin,nothing);

	for(int it = 0; it < t; ++it){
		string g;
		getline(cin, g);
		//cout << "g is: " << g << endl;
		
		string english;
		for(int ig = 0, ng = g.size(); ig < ng; ++ig)
      english += dic[g[ig]];
		cout << "Case #" << it + 1 << ": " << english << endl;
	}

	return 0;

}

