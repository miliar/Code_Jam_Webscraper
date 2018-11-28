#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string>

#define JAM 1
using namespace std;

char replaces [30];

char reemplazo(char x)
{
    return replaces[(int)x-'a'];
}

int main()
{
    #ifdef JAM
        freopen("input.in","r",stdin);
    #endif

    int n;
    cin >>n >> ws;
    int i =0;
    string ins[50];
    string matchs[50];
    for(i=0;i<n;i++)
        getline(cin,ins[i]);


    freopen("match.in","r",stdin);
    for(i=0;i<n;i++)
        getline(cin, matchs[i]);

    for(i=0;i<3;i++)
    {
        for(int j=0;j<matchs[i].size();j++)
        {
            if((matchs[i][j]>='a')&&(matchs[i][j]<='z'))
                replaces[ins[i][j]-'a'] = matchs[i][j];
        }
    }
    replaces['q'-'a'] = 'z';
    replaces['z'-'a'] = 'q';

    freopen("inputposta.in","r",stdin);
    cin >>n >> ws;
    string entrada [50];
    freopen("salidita.out","w",stdout);
    for(i=0;i<n;i++)
        getline(cin,entrada[i]);

    for(int j=0;j<n;j++)
    {
        cout << "Case #" << j+1 << ": ";
        for(i=0;i<entrada[j].size();i++)
        {
            if(entrada[j][i]==' ')
                cout << ' ';
            else
                cout << (char)(reemplazo(entrada[j][i]));
        }
        if(j!=n-1) cout << endl;
    }

    return 0;
}
