
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
#include <map>
#include <string.h>
using namespace std;

int taulu[20000000]= {0};

typedef long long int lint;

int RotateIntValue (int num, int value)
{
    string number;
    stringstream ss; //(num);
    ss << num;
    ss >> number;
    for (int i=0; i<number.size(); i++)
    {
        char c = number[0];
        number.erase(0,1);
        number += c;
        // cout << number << endl;
        if (number[0] != '0')
            taulu[atoi(number.c_str())] = value;
    }
}

int factorial(int x)
{
    if(x==1||x==0)
        return(1);
    else
        return(x*factorial(x-1));

}
int ncr(int n, int r)
{
    if (n<r) return 0;

    return factorial(n)/((factorial(r))*(factorial(n-r)));
}

int main()
{
    map<char,char> mappi;

string str1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvzq";
string str2 = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upqz";

for (int i=0; i<str1.size(); i++){
    mappi[str1[i]] = str2[i];

}

    ifstream lue("A-small-attempt6.in");
    ofstream out("file.txt");
    int lines=0;
    int a,b;
    string line;
    int num=0;
    getline(lue,line);
    while(getline(lue,line))
    {
        num++;
        out << "Case #" << num << ": ";
        for (int i=0; i<line.size(); i++){
            char c = mappi[line[i]];
            if (c)
                out << c;
            else{ out << line[i];}
        }
        out << endl;



    }

}



