#include <iostream>
#include <string>
using namespace std;

main()
{
      freopen("A-small-attempt1.in","r",stdin);
      freopen("rav22_A.txt","w",stdout);
	string in[] = {
                    "ejp mysljylc kd kxveddknmc re jsicpdrysi",
                    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                    "de kr kd eoya kw aej tysr re ujdr lkgc jv"
	};

    string out[] = {
                    "our language is impossible to understand",
                    "there are twenty six factorial possibilities",
                    "so it is okay if you want to just give up"
    };

	int map[26];
	for (int i = 0; i < 3; i++)
	{
	    for (int j = 0; j < in[i].size(); j++)
	    {
            map[in[i][j]-'a'] = out[i][j]-'a';
	    }
	}

	map[113-'a'] = 122-'a';
	map[122-'a'] = 113-'a';

	int t;
	cin >> t;
	string text;
	getline(cin,text);

	for (int testIndex = 1; testIndex <= t; testIndex++)
	{
		getline(cin,text);
		cout << "Case #" << testIndex << ": ";
		for (int i = 0; i < text.size(); i++)
		{
		    if (text[i] == ' ')
		    {
		        cout << " ";
		    }
			else
			{
			    cout << (char)(map[text[i]-'a']+'a');
			}
		}
		cout << "\n";
	}

}
