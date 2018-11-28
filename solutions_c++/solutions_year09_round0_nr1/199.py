//jhurwitz

#include <fstream>
#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

struct trie
{
    trie* children[26];
    trie()
    {
        for (int i=0; i<26; i++)
            children[i] = NULL;
    }
} *words;
int L, D, N;
vector<int> chars[20];
int cnt;

ifstream fin("a-large.in");
ofstream fout("a-large.out");

void dfs(int let, trie* t, int left)
{
    if (left==0)
    {
        cnt++;
        return;
    }
    for (vector<int>::iterator iter=chars[let].begin(); iter!=chars[let].end(); iter++)
        if (t->children[*iter] != NULL)
            dfs(let+1, t->children[*iter], left-1);
}

void problem(int casenum)
{
    char line[1000];
    fin.getline(line, 1000);
    char *c = line;
    
    for (int i=0; i<20; i++)
        chars[i].clear();
    for (int i=0; i<L; i++, c++)
        if (*c != '(')
            chars[i].push_back(*c-'a');
        else
        {
            c++;
            while (*c != ')')
            {
                chars[i].push_back(*c-'a');
                c++;
            }
        }
    
    /*for (int i=0; i<L; i++)
    {
        for (vector<int>::iterator iter=chars[i].begin(); iter!=chars[i].end(); iter++)
            cout << (char)(*iter+'a');
        cout << endl;
    }*/
        
    cnt=0;
    dfs(0, words, L);
    
    fout << "Case #" << casenum << ": " << cnt << endl;
}

int main()
{
    fin >> L >> D >> N;
    for (int i=1; i<=D; i++)
    {
        char word[20];
        fin >> word;
        trie *t = words;
        for (int i=0; i<L; i++)
        {
            int let = word[i]-'a';
            if (t->children[let] == NULL)
                t->children[let] = new trie();
            t = t->children[let];
        }
    }
    
    char junk[17];
    fin.getline(junk, 17);
    
    for (int i=1; i<=N; i++)
        problem(i);
    
    return 0;
}
