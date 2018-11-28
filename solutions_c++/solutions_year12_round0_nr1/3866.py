#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main()
{
    map<char, char> mp;
    string junk;
    int n;
    cin >> n;
    getline(cin, junk);
    vector<string> gtext, etext;
    
    for (int i=0; i<n; i++)
    {
        string s;
        getline(cin, s);
        gtext.push_back(s);
    }
    
    for (int i=0; i<n; i++)
    {
        cin >> junk >> junk;
        cin.get();
        string s;
        getline(cin,s);
        etext.push_back(s);
    }
    
    for (int i=0; i<n; i++)
        for (int j=0; j<gtext[i].size(); j++)
            mp[gtext[i][j]] = etext[i][j];
            
    mp['q'] = 'z';
    
    int found = 0;
    char notFound;
    for (int i='a'; i<='z'; i++)
        if (mp[i] >= 'a' && mp[i] <= 'z')
            found |= (1<<(mp[i]-'a'));
        else
            notFound = i;
            
    for (int i=0; i<26; i++)
        if ((found & (1<<i)) == 0)
            mp[notFound] = 'a' + i;
            
    cin >> n;
    getline(cin, junk);
    for (int i=1; i<=n; i++)
    {
        string s;
        getline(cin, s);
        for (int i=0; i<s.size(); i++)
            s[i] = mp[s[i]];
        cout << "Case #" << i << ": " << s << endl;
    }
}
