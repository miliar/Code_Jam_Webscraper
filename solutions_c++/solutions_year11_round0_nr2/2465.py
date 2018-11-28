#include <iostream>
#include <fstream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <time.h>
#include <stdlib.h>
using namespace std;

#define pb push_back
#define vi vector <int>
#define rep(i,n) for(int i = 0; i < n; i++)
#define read(a) rep(i, a.size()) fin >> a[i];
#define write(a) rep(i, a.size()) fout << a[i] << ' '; fout << endl;
#define fi first
#define se second
#define ll long long
const int inf = 2000000000, mod = 1000000007;
const char null_char = (char)(0);

int main()
{
    ifstream fin ("input.txt");
    ofstream fout ("output.txt");
    int t;
    fin >> t;
    for (int count = 1; count <= t; count++)
    {
        int c, d, n;
        map <pair<char, char>, char> combine;
        map <pair<char, char>, char> opposed;
        fin >> c;
        for (int i = 0; i < c; i++)
        {
            string s;
            fin >> s;
            combine[make_pair(s[0], s[1])] = s[2];
        }
        fin >> d;
        for (int i = 0; i < d; i++)
        {
            string s;
            fin >> s;
            opposed[make_pair(s[0], s[1])] = 'Y';
        }
        string s;
        fin >> n >> s;
        vector <char> a;
        for (int i = 0; i < n; i++)
        {
            a.push_back(s[i]);
            if (a.size() < 2)
               continue;
            if (combine[make_pair(a[a.size() - 1], a[a.size() - 2])] != null_char)
            {
                char c = combine[make_pair(a[a.size() - 1], a[a.size() - 2])];
                a.pop_back();
                a.pop_back();
                a.push_back(c);
            }
            if (combine[make_pair(a[a.size() - 2], a[a.size() - 1])] != null_char)
            {
                char c = combine[make_pair(a[a.size() - 2], a[a.size() - 1])];
                a.pop_back();
                a.pop_back();
                a.push_back(c);
            }
                  
            for (int j = 0; j < (int)a.size() - 1; j++)
                if (opposed[make_pair(a[j], a[a.size() - 1])] != null_char || opposed[make_pair(a[a.size() - 1], a[j])] != null_char)
                   a.clear();
        }
        fout << "Case #" << count << ": ";
        fout << "[";
        for (int i = 0; i < a.size(); i++)
        {
            fout << a[i];
            if (i != a.size() - 1)
               fout << ", ";
        }
        fout << "]" << endl;
    }
    return 0;
}








