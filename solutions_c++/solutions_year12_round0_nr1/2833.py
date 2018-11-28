#include <iostream>
#include <map>
using namespace std;

map<char, char> mapping;

void loadMapping()
{
    int lineCnt;
    char googleres[200], english[200];
    scanf("%d", &lineCnt);    
    getchar();
    while(lineCnt--)
    {
        gets(googleres);
        gets(english);
        for(int i=0; googleres[i]; ++i)
        {
            mapping[googleres[i]] = english[i];
        }
    }
    mapping['z'] = 'q';
    mapping['q'] = 'z';
}

void translate(char googleres[], char english[])
{
    int i;
    for(i=0; googleres[i]; ++i)
    {
        english[i] = mapping[ googleres[i] ];
    }
    english[i] = 0;
}

void translateAll()
{
    int lineCnt;
    char googleres[500], english[500];
    scanf("%d", &lineCnt);    
    getchar();
    for(int i=1; i <=lineCnt; i++)
    {
        gets(googleres);
        translate(googleres, english);
        printf("Case #%d: %s\n", i, english);
    }
}

int main()
{
    freopen("A-Small.sample", "r", stdin);
    loadMapping();    
    freopen("A-Small.in", "r", stdin);
    freopen("A-Small.out", "w", stdout);
    translateAll();    
}