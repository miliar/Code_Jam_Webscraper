#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <istream>

using namespace std;

map<char,char> MAP;

string F = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";

string T = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

string solve();

int main()
{
    for(int i=0; i<F.length(); ++i)
	{
	    if(F[i] != ' ')
		MAP[F[i]] = T[i];
	}

    MAP['q'] = 'z';
    MAP['z'] = 'q';
    MAP[' '] = ' ';

    int T;
    cin >> T;
    string temp;
    getline(cin, temp);
   
    for(int i=0; i<T; ++i)
	{
	    cout << "Case #" << i+1 << ": " << solve() << endl;
	}

    return 0;
}


string solve()
{
    string G,S;
    getline(cin, G);

    for(int i=0; i<G.size(); ++i)
	{
	    S += MAP[G[i]];
	}
    
    return S;
}
    
