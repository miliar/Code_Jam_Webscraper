#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <string>
#include <cmath>
#define pb push_back
#define fs first
#define sc second

using namespace std;



string testInput[] = {
        "ejp mysljylc kd kxveddknmc re jsicpdrysi",
        "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
        "de kr kd eoya kw aej tysr re ujdr lkgc jv"};

string testOutput[] = {
        "our language is impossible to understand",
        "there are twenty six factorial possibilities",
        "so it is okay if you want to just give up"
};

char refTo[256];



void calcLettersMapping(){
    for (int i=0;i<256;++i) refTo[i] = 0;
    for (int i=0;i<3;++i){
        for (int j=0;j<testInput[i].size();++j){
            refTo[testInput[i][j]] = testOutput[i][j];
        }
    }
    char ost = 0;
    refTo['q'] = 'z';

    refTo['z'] = 'q';
}
char buffer[150];



int main(void){
#ifndef KEYBOARD_INPUT
    freopen("a-small-in.txt", "r", stdin);
    freopen("a-small-out.txt", "w", stdout);
#endif
    int n;

    scanf ("%d%*c", &n);

    calcLettersMapping();

    for (int i=0;i<n;++i){
        gets(buffer);

        string s = (string)buffer;
        for (int j=0;j<s.size();++j) {
            if ( s[j] == '\n') continue;
            s[j] = refTo[s[j]];
        }
        printf ("Case #%d: %s\n", i+1,s.c_str());
    }



	return 0;
}
