#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

int main()
{

// Examples 
string 
goog1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi",
goog2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
goog3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv",
norm1 = "our language is impossible to understand",
norm2 = "there are twenty six factorial possibilities",
norm3 = "so it is okay if you want to just give up";

// Build Map
map<char,char> translation; 
for(int i = 0; i < goog1.size(); i++)
	translation[goog1[i]] = norm1[i];
	
for(int i = 0; i < goog2.size(); i++)
	translation[goog2[i]] = norm2[i];
	
for(int i = 0; i < goog3.size(); i++)
	translation[goog3[i]] = norm3[i];

// USE HINT 
translation['q'] = 'z';
translation['z'] = 'q';

// Solve
freopen("C:\\Users\\Agrim\\Desktop\\A-small-attempt0.in","r",stdin);
freopen("C:\\Users\\Agrim\\Desktop\\A-small.out","w+",stdout);

int T; // # of test cases
cin >> T;

string s;getline(cin,s);
for (int i = 1; i <= T; i++)
{
	getline(cin,s);
	//cout << s;
	for (int i = 0; i < s.size(); i++)
		cout << translation[s[i]];
	cout << endl;	
}

}