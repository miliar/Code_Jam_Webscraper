#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
#include <map>

using namespace std;

int main()
{
    map<char,char>  _map;
//    _map[' ']=' ';

    string p_alphabet ="abcdefghijklmnopqrstuvwxyz";
    string c_alphabet ="abcdefghijklmnopqrstuvwxyz";
    ifstream is, ss;
    ofstream rs;
    ss.open("./source.txt");
    string plain, cipher;
    for(int i=0; i<4; i++)
    {
        getline(ss,cipher);
        getline(ss,plain);
        for(int j=0; j<cipher.length(); j++)
        {
            _map[cipher[j]]=plain[j];
            for(int k=0; k<26; k++)
            {
                if(c_alphabet[k]==cipher[j])
                {
                    c_alphabet[k]=' ';
                }
                if(p_alphabet[k]==plain[j])
                {
                    p_alphabet[k]=' ';
                }
            }
        }
    }
    for(int i=0; i<26; i++)
    {
        if (c_alphabet[i]!=' ')
        {
            for(int j=0; j<26; j++)
                if (p_alphabet[j]!=' ')
                    _map[c_alphabet[i]]=p_alphabet[j];

        }
    }

    cout << _map.size();

    is.open("./A-small-attempt.in");
    rs.open("./res.out");
    int num_of_test;
    is >>  num_of_test;
    string _str;
    getline(is,_str);
    for(int i=0; i<num_of_test; i++)
    {
        string str, resstr;
        getline(is,str);
        resstr="";
        for(int j=0; j<str.length(); j++)
        {
            resstr=resstr+_map[str[j]];
        }
        rs << "Case #" << i+1 << ": " << resstr << endl;
    }
    return 0;
}


