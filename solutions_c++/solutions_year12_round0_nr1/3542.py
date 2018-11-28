#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;
    
    string a[3];
    string aa[3];
    
    a[0] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    a[1] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    a[2] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    
    aa[0] = "our language is impossible to understand";   //abcdefghijklmnop rstuvwxy
    aa[1] = "there are twenty six factorial possibilities";
    aa[2] = "so it is okay if you want to just give up";
    
    char mapping[26];
    
    int i;
    
    for (i = 0; i < 26; i++)
        mapping[i] = '0';
    
    for (int k = 0; k < 3; k++)
    {
        for (i = 0; i < a[k].size(); i++)
        {
            if (a[k][i] == ' ')
                continue;
                
            if (mapping[a[k][i] - 'a'] == '0')
            {
                mapping[a[k][i] - 'a'] = aa[k][i];               
            }    
        }
    }
    
    for (i = 0; i < 26; i++)
    {
        if (mapping[i] == '0')
        {
            cout << (char)('a' + i) << " is missing" << endl;
            system("pause");               
        }    
    }
    
    mapping['q' - 'a'] = 'z';
    mapping['z' - 'a'] = 'q';
    
    int T;
    
    fin.open("A-small-attempt2.in");
    fout.open("out.txt");
    
    fin >> T;
    string tmp;
    getline(fin, tmp);
    
    int tcase = 0;
    while (T > 0)
    {
        cout << "T = " << T << endl;
        tcase++;
        
        string s = "";
        getline(fin, s);
        cout << "T = " << T << " " << s << endl;
        
        string ans = "";
        for (i = 0; i < s.size(); i++)
        {
            if (s[i] == ' ')
                ans += ' ';
            else
                ans += mapping[s[i] - 'a'];
        }      
        fout << "Case #" << tcase << ": " << ans << endl;
        T--;
    }    
    
    fin.close();
    fout.close();
    
    system("pause");
    return 0;    
}
