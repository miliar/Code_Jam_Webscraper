//
//  main.cpp
//  taskA
//
//  Created by sergey on 4/14/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <string>
#include <map>

using namespace std;

map<char, char> code;

void build_code()
{
	int used[255];
	for (int i = 0; i < 255; i++)
		used[i] = 0;

    //code.insert(make_pair('a', 'y'));
    //code.insert(make_pair('o', 'e'));
    code.insert(make_pair('z', 'q'));
    code.insert(make_pair('q', 'z'));
	used['q']++;
	used['z']++;
    
    string str1("ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv");
    string str2("our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up");
    
    for (int i = 0; i < str1.size(); i++)
    {
        char ch1 = str1[i];
        char ch2 = str2[i];
        if (code.find(ch1) != code.end())
        {
            if (code[ch1] != ch2)
            {
                cout << "error\n";
                cout << i << " " << ch1 << " " << ch2 << endl;
                return;
            }
        }
        else
        {
			used[ch2]++;
            code.insert(make_pair(ch1, ch2));
        }
    }
    
}

int main(int argc, const char * argv[])
{
	int N;
	cin >> N;

	build_code();
	string str;
	getline(cin, str);
	for (int i = 1; i <= N; i++)
	{
		getline(cin, str);
		cout << "Case #" << i << ": ";
		for (int j = 0; j < str.size(); j++)
		{
			cout << code[str[j]];
		}

		cout << endl;
	}

	return 0;
}

