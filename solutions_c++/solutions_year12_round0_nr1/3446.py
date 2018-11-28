#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <math.h>
#include <sstream>
#include <cstring>

using namespace std;


int main()
{

 freopen("A-small-attempt0.in","r",stdin);
 freopen("output.out","w",stdout);

    string alpha   = "abcdefghijklmnopqrstuvwxyz";
    string convert = "ynficwlbkuomxsevzpdrjgthaq";


    int T  = 0;
    cin >> T;
    cin.ignore();
    string in;
    string cas = "Case #";
    int start = 1;

    while(start <= T)
    {
        string out = "";
        getline(cin,in);
        for(int i = 0; i < in.length(); ++i)
        {
            if(in[i] == ' ')
                out+=" ";
            else
            {
                for(int j = 0 ; j < convert.length(); ++j)
                    if(in[i] == convert[j])
                    {
                        out+= alpha[j];
                        break;
                    }

            }

        }

        cout << cas << start << ": " << out << endl;
        start++;
    }


    return 0;
}
