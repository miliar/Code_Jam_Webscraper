#include <iostream>
#include <cassert>

using namespace std;

int main()
{
    char training_crypto[] = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
    char training_answer[] = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";

    assert(sizeof(training_crypto) == sizeof(training_answer));

    char mapping[26];
    for (int i = 0; i < 26; i++)
        mapping[i] = '\0';

    mapping['q'-'a'] = 'z';
    mapping['z'-'a'] = 'q';

    for (int i = 0; i < sizeof(training_crypto); i++)
    {
        if (training_crypto[i] == ' ' || training_crypto[i] == '\0')
            continue;
//        cerr << training_crypto[i] << " => " << training_answer[i] << endl;
        if (mapping[training_crypto[i]-'a'] == '\0')
            mapping[training_crypto[i]-'a'] = training_answer[i];
        else
            assert(mapping[training_crypto[i]-'a'] == training_answer[i]);
    }

    for (int i = 0; i < 26; i++)
    {
//         if (mapping[i] == '\0')
//             cout << "no dest for " << (char)(i + 'a') << endl;
    }

    int numCases;
    cin >> numCases;

    string line;
    getline(cin, line);

    for (int testCase = 1; testCase <= numCases; testCase++)
    {
        getline(cin, line);
        for (int i = 0; i < line.length(); i++)
            if (line[i] != ' ')
                line[i] = mapping[line[i]-'a'];
        cout << "Case #" << testCase << ": " << line << endl;
    }

    return 0;
}
