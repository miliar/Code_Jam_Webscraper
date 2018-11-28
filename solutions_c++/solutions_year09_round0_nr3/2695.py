#include <iostream>
#include <fstream>
#include <algorithm>
#include <utility>
#include <cmath>
#include <stack>
#include <cstdio>
#include <vector>
#include <map>
#include <string>

using namespace std;

ifstream fin("C-small-attempt0.in");
//ofstream fout("C-small.out");
FILE *f = fopen("C-small-attempt0.out", "w");

char code[20] = "welcome to code jam";


int N,L;
char str[30];
string s;
int ans = 0;

void poss(int pos, int stat)
{
    if(stat == 19)
    {
        ans++;
        if(ans > 10000) ans %= 10000;
        return;
    }

    for(int i=pos;i<L;i++)
       if(s[i] == code[stat]) poss(i+1,stat+1);

}

int main()
{
    int i=1,spaces;

    fin>>N;
    getline(fin,s);
    while(N--)
    {
        getline(fin,s);
        ans = 0;
        L = s.size();
        poss(0,0);
        fprintf(f,"Case #%d: %04d\n", i++, ans);
    }
    system("PAUSE");
    return EXIT_SUCCESS;
}
