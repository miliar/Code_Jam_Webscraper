// B. Magicka.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

int t,c,d,n;
string s;
string str;

map<string, string> combines;
map<char, string> opposed;

bool find_combine(int index)
{
    if (index > 0)
    {
        string ss = str.substr(index - 1, 2);
        if (combines.count(ss) > 0)
        {
            return true;
        }
    }
    return false;
}

int find_opposed(int index)
{
    for (int i = 0; i < index; i++)
    {
        if (opposed.count(str[index]) > 0)
        {
            string ss = opposed[str[index]];
            for (int j = 0; j < ss.size(); j++)
            {
                if (ss[j] == str[i])
                    return i;
            }
        }
    }

//     for (int i = index - 1; i >= 0; i--)
//     {
//         if (opposed.count(str[index]) > 0)
//         {
//             string ss = opposed[str[index]];
//             for (int j = 0; j < ss.size(); j++)
//             {
//                 if (ss[j] == str[i])
//                     return i;
//             }
//         }
//     }
    
    return -1;
}

int main()
{
    //freopen("1.in", "r", stdin);
    //freopen("B-small-attempt2.in", "r", stdin);
    //freopen("B-small-attempt2.out", "w", stdout);
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    //freopen("1.in", "r", stdin);
    //freopen("1.out", "w", stdout);

    cin >> t;
    for (int cc = 1; cc <= t; cc++)
    {
        combines.clear();
        opposed.clear();

        cin >> c;
        for (int i = 0; i < c; i++)
        {
            cin >> s;
            string ss = s.substr(0, 2);
            combines[ss] = s[2];
            string ss2;
            ss2 += ss[1];
            ss2 += ss[0];
            combines[ss2] = s[2];
        }
        cin >> d;
        for (int i = 0; i < d; i++)
        {
            cin >> s;
            if (opposed.count(s[0]) == 0)
            {
                opposed[s[0]] = s.substr(1,1);
            }
            else
            {
                opposed[s[0]] += s[1];
            }
            if (opposed.count(s[1]) == 0)
            {
                opposed[s[1]] = s.substr(0,1);
            }
            else
            {
                opposed[s[1]] += s[0];
            }
        }
        str = "";
        cin >> n; 
        cin >> s;
        
        for (int i = 0; i < n; i++)
        {
            str += s[i];
            int index = str.size() - 1;
            if (find_combine(index))
            {
                int length = str.size();
                string first = str.substr(0, length - 2);
                string second = str.substr(length - 2, 2);
                str = first + combines[second];
            }

            index = str.size() - 1;
            int res = find_opposed(index);
            if (res != -1)
            {
                //str = str.substr(0, res);
                str = "";
            }
        }

        cout << "Case #" << cc << ": [";
        for (int i = 0; i < str.size(); i++)
        {
            if (i == 0)
                cout << "";
            else
                cout << ", ";
            cout << str[i];
        }
        cout << "]" << endl;
    }
	return 0;
}

