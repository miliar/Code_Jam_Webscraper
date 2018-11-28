#include <iostream>
#include <cstdlib>
#include <fstream>
#include <string>
#include <cmath>
#include <map>

using namespace std;

int main()
{
    ifstream fin("a-input.in");
    ofstream fout("a-output.out");
    int T;
    fin >> T;
    for(int c=0; c<T; c++)
    {
        string message;
        fin >> message;
        map <char, char> translate;
        map <char, char> back;
        translate[message[0]]='1';
        back['1']=message[0];
        string normal="0123456789abcdefghijklmnopqrstuvwxyz";
        for(int i=0; i<normal.size(); i++) for(int j=1; j<message.size(); j++)
        {
            if(translate.find(message[j])==translate.end() && back.find(normal[i])==back.end())
            {
                translate[message[j]]=normal[i];
                back[normal[i]]=message[j];
            }
        }
        int minBase=0;
        string digits;
        for(int i=0; i<message.size(); i++)
        {
            bool found=false;
            for(int j=0; j<digits.size(); j++) if(digits[j]==message[i]) found=true;
            if(!found) digits+=message[i];
        }
        minBase=digits.size();
        string translated;
        for(int i=0; i<message.size(); i++) translated+=translate[message[i]];
        unsigned long long minimum=0xFFFFFFFFFFFFFFFFULL;
        for(int i=max(minBase, 2); i<=36; i++)
        {
            unsigned long long number=strtoll(translated.c_str(), 0, i);
            if((unsigned long long)number<(unsigned long long)minimum) minimum=(unsigned long long)number;
        }
        fout << "Case #" << c+1 << ": " << (unsigned long long)minimum << endl;
    }
    fin.close();
    fout.close();
    return 0;
}
