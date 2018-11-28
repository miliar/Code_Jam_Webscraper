#include <iostream>
#include <stdio.h>
#include <string>
#include <algorithm>
#include <vector>
#include <fstream>
using namespace std;

int main()
{
    ifstream in("in.txt");
    char b[] ={"abcdefghijklmnopqrstuvwxyz"};
    char c[] ={"yhesocvxduiglbkrztnwjpfmaq"};
    ofstream out("out.txt");
    //char a,b;
    int j=6;
    int k=j;
    int o=j;
    string a;
    int u=1;
 getline(in,a);
    while(getline(in,a))
    {
        out<<"Case #"<<u<<": ";
        for(int m=0;m<a.length();m++)
        {
            if(a[m]==32)
            {
            out<<" ";
            continue;
            }
            int j= a[m]%97;
            out<<c[j];
        }
        out<<endl;
        u++;
    }

    return 0;
}
