#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <sstream>
using namespace std;

void permute(const char* in, char* out, int len, vector<int> &perm)
{
     for (int offset = 0; offset < len; offset += perm.size())
     {
         for (int i = 0; i < perm.size(); i++)
         {
             out[offset+perm[i]] = in[offset+i];
         }
     }
     //cout << out << endl;
}

int minGroups(string str)
{
    int total = 0;
    char last = '0';
    
    for (int i = 0; i < str.length(); i++)
    {
        if (str[i] != last)
        {
           total++;
           last = str[i];
        }
    }
    return total;
}

int main()
{
    ifstream in("happy.txt");
    ofstream out("sad.txt");
    
    int cases;
    in >> cases;
    for (int i = 0; i < cases; i++)
    {
        int len;
        string str;
        in >> len >> str;
        char ch[10000];
        for (int k = 0; k < 10000; k++) ch[k] = 0;
        vector<int> vec;
        for (int j = 0; j < len; j++)
        {
            vec.push_back(j);
        }
        int minn = 10000;
        do
        {
            permute(str.c_str(), ch, str.length(), vec);
            minn = min(minn, minGroups(string(ch)));
        } while (next_permutation(vec.begin(), vec.end()));
        out << "Case #" << (i+1) << ": " << minn << endl;
    }
    system("PAUSE");
    return 0;
}   
