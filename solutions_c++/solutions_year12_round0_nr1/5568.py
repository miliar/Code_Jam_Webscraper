#include<iostream>
#include<string>

using namespace std;


int main()      {
        int n, k=1;
        int i;
        string s;

        char table[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u',
                          'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w',
                          'j', 'p', 'f', 'm', 'a', 'q'};

        cin >> n;
        getline(cin, s);
        while (n>0)     {
                getline(cin, s);
//              cout << s << endl;
                cout << "Case #" << k << ": ";
                for (i=0; i<s.length(); i++)    {
                        if (s[i]==' ')
                                cout << ' ';
                        else
                               cout << table[s[i]-'a'];

                }
                cout << endl;
                n--;
                k++;
        }

        return 0;
}
