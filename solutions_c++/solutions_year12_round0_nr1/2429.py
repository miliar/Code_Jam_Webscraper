#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    string a1="ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
    string a2="our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
    char a[26];
    for (int i=0;i<(int)a1.size();i++)
    {
        if (a1[i]!=' ') a[a1[i]-'a']=a2[i];
    }
    a['q'-'a']='z';
    a['z'-'a']='q';

    int n;
    cin >> n;
    getchar();
    for (int i=0;i<n;i++)
    {
        string temp;
        cout << "Case #" << i+1 << ": ";
        getline(cin,temp);
        for (int j=0;j<(int)temp.size();j++)
        {
            if (temp[j]!=' ') cout << a[temp[j]-'a']; else cout << " ";
        }
        cout << endl;
    }
    //cout << "Hello world!" << endl;
    return 0;
}
