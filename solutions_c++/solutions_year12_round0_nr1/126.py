#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

void fill_in_translation_table(map<char, char>& dict, const string& s, const string& t)
{
    for (size_t i = 0; i < s.length(); i++)
    {
        dict[s[i]] = t[i];
    }
}

bool check_translation_table_complete(const map<char, char>& dict)
{
    bool ok = true;
    for (char c = 'a'; c <= 'z'; c++)
    {
        if (dict.find(c) == dict.end())
        {
            cerr << "missing " << c << endl;
            ok = false;
        }
    }
    return ok;
}

void complete_translation_table(map<char, char>& dict)
{
    vector<bool> used(26, false);
    map<char, char>::iterator it;
    for (it = dict.begin(); it != dict.end(); it++)
    {
        if (it->second == ' ')
        {
            continue;
        }
        used[it->second-'a'] = true;
    }
    for (size_t i = 0; i < 26; i++)
    {
        if (!used[i])
        {
            dict['z'] = i + 'a';
        }
    }
}

string translate(map<char, char>& dict, string s)
{
    for (size_t i = 0; i < s.length(); i++)
    {
        s[i] = dict[s[i]];
    }
    return s;
}

int main()
{
    int T, t;
    string s;
    // Prepare translation table
    map<char, char> dict;

    // Given in the problem example
    dict['y'] = 'a';
    dict['e'] = 'o';
    dict['q'] = 'z';

    // From the sample input-output
    fill_in_translation_table(dict, "ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand");
    fill_in_translation_table(dict, "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
    fill_in_translation_table(dict, "de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");

    // Check if the translation table is complete
    /*
    if (!check_translation_table_complete(dict))
    {
        cerr << "Error!" << endl;
    }
    */
    // Turns out it is missing 'z'
    complete_translation_table(dict);

    cin >> T;
    getline(cin, s);
    for (t = 1; t <= T; t++)
    {
        getline(cin, s);
        cout << "Case #" << t << ": " << translate(dict, s) << endl;
    }

    return 0;
}

