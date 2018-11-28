#include <iostream>
#include <stdio.h>
#include <string.h>
#include <map>
#include <fstream>

using namespace std;

int main()
{
    map<char, char> code;

    string str1 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    string str2 = "there are twenty six factorial possibilities";

    for(int i = 0; i < str1.length() ; i++)
    {
        code[str1[i]] = str2[i];
    }

    str1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    str2 = "our language is impossible to understand";

    for(int i = 0; i < str1.length() ; i++)
    {
        if(code[str1[i]] == 0){
            code[str1[i]] = str2[i];
        }
    }

    str1 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    str2 = "so it is okay if you want to just give up";

    for(int i = 0; i < str1.length() ; i++)
    {
        if(code[str1[i]] == 0){
            code[str1[i]] = str2[i];
        }
    }

    code['z'] = 'q';
    code['q'] = 'z';

    ifstream infile;
    ofstream outfile;

    outfile.open("output.txt");
    infile.open("input.in", ifstream::in);
    int n;
    char str[200]; string output = "";
    infile>>n;
    infile.getline(str,1000);
    int b = n; int j = 1;
    //cin.ignore();
    //while(getline(cin,str))
    while(infile.getline(str,1000))
    {
        b--;
        for(int i = 0; i < strlen(str); i++){
            output += code[str[i]];
        }
        outfile<<"Case #"<<j<<": "<<output<<endl;
        output = "";
        j++;
        if(b == 0)
            break;
    }

    return 0;
}
