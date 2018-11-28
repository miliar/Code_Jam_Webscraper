//  -*- mode: c++; coding: utf-8; c-file-style: "stroustrup"; -*-

#include <fstream>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits>
#include <set>

using namespace std;

//                       abcdefghijklmnopqrstuvwxyz
const char *translation="yhesocvxduiglbkrztnwjpfmaq";

int main(int narg, char **arg)
{
    int t;
    cin >> t;
    string str;
    getline(cin, str);
    for(int it=0; it<t; it++)
    {
        cout << "Case #" << it+1 << ": ";
        getline(cin, str);
        for(unsigned i=0; i<str.size(); i++) if(isalpha(str[i])) str[i]=translation[str[i]-'a'];
        cout << str << endl;
    }
    return 0;
}
