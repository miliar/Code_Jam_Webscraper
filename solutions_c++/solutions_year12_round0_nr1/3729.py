#include <iostream>
#include <stdio.h>
#include <fstream>
#include <map>
using namespace std;

char str[255];

char *z1="ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
char *z2="our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";

map <char, char> mp;
int main()
{
    ifstream inf("a.in");
    ofstream ouf("a.out");
    
    int n;
    inf >> n;
    inf.ignore();
    mp.clear();
    int i=0;
    while (i<strlen(z1))
    {
        mp[z1[i]] = z2[i];
        i++;
    }
    mp['z']='q';
    mp['q']='z';
    int j;
    for (i=1; i<=n; i++)
    {
        inf.getline(str,255);
        for (j=0;j<strlen(str);j++)
        {
            str[j] = mp[str[j]];
        }
        ouf << "Case #" << i << ": " << str << endl;
    }
    for (i='a'; i<='z'; i++)
    {
        cout << (char)i << " " << mp[i] << endl;
    }
    
    inf.close();
    ouf.close();
//    system("pause");
    return 0;
}
