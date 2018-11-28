////////////////////////////////////////////////////////////////////////////////
// Solution to Speaking in Tounges,
// Google code jam Qualification Round 2012
// Tristram Healy, trissylegs@gmail.com
// Apr 14 2012
////////////////////////////////////////////////////////////////////////////////

#include <iostream>
#include <string>
#include <cstdio>

#define NUM_LETTERS 26
#define MAX_LINE 101

using namespace std;

string googKey(void);
string genKey(string goog, string engl);
void modKey(string goog, string engl, string& key);
void finKey (string &key);
string decode(string input, string key);

int main(void)
{
    string key = googKey();
    char G[MAX_LINE] = "\0";
    int T, i;

    cin >> T;
    cin.ignore(MAX_LINE, '\n');

    //cout << key << endl;

    for(i = 1; i <= T; i++)
    {
	cin.getline(G, MAX_LINE);
	//scanf("%300s", G);
	//cout << G << endl;
	printf("Case #%d: ", i);
	cout << decode(string(G), key) << endl;
    }

    return 0;
}

string googKey(void)
{

    string googKey;
    string enAlphabet = "abcdefghijklmnopqrstuvwxyz";

    string goog1 = 
	"ejp mysljylc kd kxveddknmc re jsicpdrysi\n"
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd\n"
	"de kr kd eoya kw aej tysr re ujdr lkgc jv\n";

    string eng1 = 
	"our language is impossible to understand\n"
	"there are twenty six factorial possibilities\n"
	"so it is okay if you want to just give up\n";

    string goog2 = "y qee";
    string eng2 = "a zoo";


    googKey = genKey(goog1, eng1);
//    cout << googKey << endl;
	
    modKey(goog2, eng2, googKey);
//    cout << googKey << endl;

    finKey(googKey);
//    cout << googKey << endl;

//    cout << decode(goog1, googKey) << endl;

    return googKey;
}

string genKey (string goog, string eng)
{
    //Fill the output string with a string long enough to hold the key
    //               abcdefghijklmnopqrstuvwxyz
    string output = "--------------------------";
    
    modKey(goog, eng, output);
    return output;
}

void modKey (string goog, string eng, string &key)
{
    unsigned int i;

    for(i = 0; i < goog.size(); i++)
    {
	if(goog[i] >= 'a' && goog[i] <= 'z' && key[goog[i] - 'a'] == '-')
	{
	    key[goog[i] - 'a'] = eng[i];
	}
    }
}

void finKey (string &key)
{
    int count = 0;
    int i;
    string alpha("abcdefghijklmnopqrstuvwxyz");
    size_t missing;
    size_t found;

    for(i = 0; count < 2 && i < NUM_LETTERS; i++)
    {
	if (key[i] == '-')
	{
	    missing = i;
	    count++;
	}
    }
    if(count == 1)
    {
	for(i = 0; alpha.size() != 1 && i < NUM_LETTERS; i++)
	{
	    found = alpha.find(key[i]);
	    if (found != string::npos)
		alpha.erase(found, 1);
	}
	key[missing] = alpha[0];
    }
}

string decode(string input, string key)
{
    string output;
    size_t i;
    char j;
    for(i = 0; i < input.size(); i++)
    {
	j = input[i];
	if(j >= 'a' && j <= 'z')
	    output.push_back(key[j - 'a']);
	else
	    output.push_back(j);
    }

    return output;
}
