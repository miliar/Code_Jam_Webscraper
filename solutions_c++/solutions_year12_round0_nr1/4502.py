#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <stdlib.h>

using namespace std;

int make_codebook()
{
    map<char, char> codebook;
    map<char, bool> used_letters;

    for (char c='a'; c <= 'z'; c++)
    {
        codebook.insert(pair<char, char> (c, ' '));
        used_letters.insert(pair<char,bool> (c, false));
    }
    codebook['a'] = 'y'; used_letters['y'] = true;
    codebook['o'] = 'e'; used_letters['e'] = true;
    codebook['z'] = 'q'; used_letters['q'] = true;

    string in  = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
    string out = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

    for (unsigned int i=0; i < in.size(); i++)
    {
        codebook[in[i]] = out[i];
        used_letters[out[i]] = true;
    }

    char q;
    for (char c='a'; c <= 'z'; c++)
    {
        if(used_letters[c] == false)
        {
            q = c;
            break;
        }
    }
    codebook['q'] = q;

    fstream cpp;
    cpp.open("main.cpp", ios_base::out);
    cpp << endl;
    cpp << "void init_codebook(map<char, char>* codebook)" << endl;
    cpp << "{" << endl;

    for (char c='a'; c <= 'z'; c++)
    {
        cpp << "    codebook->insert(pair<char, char> ('" << c << "', '" << codebook[c] << "'));" << endl;
    }

    cpp << "}";
    cpp.close();

    return 0;
}

void init_codebook(map<char, char>* codebook)
{
    codebook->insert(pair<char, char> ('a', 'y'));
    codebook->insert(pair<char, char> ('b', 'h'));
    codebook->insert(pair<char, char> ('c', 'e'));
    codebook->insert(pair<char, char> ('d', 's'));
    codebook->insert(pair<char, char> ('e', 'o'));
    codebook->insert(pair<char, char> ('f', 'c'));
    codebook->insert(pair<char, char> ('g', 'v'));
    codebook->insert(pair<char, char> ('h', 'x'));
    codebook->insert(pair<char, char> ('i', 'd'));
    codebook->insert(pair<char, char> ('j', 'u'));
    codebook->insert(pair<char, char> ('k', 'i'));
    codebook->insert(pair<char, char> ('l', 'g'));
    codebook->insert(pair<char, char> ('m', 'l'));
    codebook->insert(pair<char, char> ('n', 'b'));
    codebook->insert(pair<char, char> ('o', 'k'));
    codebook->insert(pair<char, char> ('p', 'r'));
    codebook->insert(pair<char, char> ('q', 'z'));
    codebook->insert(pair<char, char> ('r', 't'));
    codebook->insert(pair<char, char> ('s', 'n'));
    codebook->insert(pair<char, char> ('t', 'w'));
    codebook->insert(pair<char, char> ('u', 'j'));
    codebook->insert(pair<char, char> ('v', 'p'));
    codebook->insert(pair<char, char> ('w', 'f'));
    codebook->insert(pair<char, char> ('x', 'm'));
    codebook->insert(pair<char, char> ('y', 'a'));
    codebook->insert(pair<char, char> ('z', 'q'));
}

int main(int, char**)
{
    // return make_codebook();

    map<char, char> codebook;
    init_codebook(&codebook);

    fstream in;
    fstream out;

    in.open("A-small-attempt0.in", ios_base::in);
    out.open("A-small-attempt0.out", ios_base::out);

    string line;
    getline(in, line);

    int T = atoi(line.c_str());

    for (int i=0; i < T; i++)
    {
        getline(in, line);

        out << "Case #" << i+1 << ": ";
        for (unsigned int c=0; c < line.size(); c++)
        {
            if (line[c] == ' ') out << (char)' ';
            else out << (char)codebook[line[c]];
        }
        out << endl;
    }

    in.close();
    out.close();

    return 0;
}

