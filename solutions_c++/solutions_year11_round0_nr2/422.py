///Magicka
#include <iostream>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <algorithm>
#include <stdio.h>
#include <ctype.h>
#include <fstream>

#define MAX 30
#define FILE_IN "B-large.in"
#define FILE_OUT "output.txt"

using namespace std;

int appeared[9];
char combine[9][9];
int oppose[9][9];
vector<char> ans;
int t, c, d, n;
int size;

int reset()
{
    memset(appeared, 0, sizeof(appeared));
    ans.clear();
    size = 0;
}

int char2num(char c)
{
    switch (c)
    {
        case 'Q': return 0;
        case 'W': return 1;
        case 'E': return 2;
        case 'R': return 3;
        case 'A': return 4;
        case 'S': return 5;
        case 'D': return 6;
        case 'F': return 7;
        default : return 8;
    }
}

int init()
{
    memset(appeared, 0, sizeof(appeared));
    memset(combine, 0, sizeof(combine));
    memset(oppose, 0, sizeof(oppose));
    ans.clear();
    size = 0;
}

int input(istream &cin)
{
    cin >> c;
    char b1, b2, o;
    for (int i=0; i<c; i++)
    {
        cin >> b1 >> b2 >> o;
      //  cout << b1 << b2 << o << endl;
        combine[char2num(b1)][char2num(b2)] = o;
        combine[char2num(b2)][char2num(b1)] = o;
    }

    cin >> d;
    for (int i=0; i<d; i++)
    {
        cin >> b1 >> b2;
      //  cout << b1 << b2 << endl;
        oppose[char2num(b1)][char2num(b2)] = 1;
        oppose[char2num(b2)][char2num(b1)] = 1;
    }
    cin >> n;
   // cout << n << endl;

}

int solve(istream &cin, ostream &fout)
{
    char c;
    for (int i=0; i<n; i++)
    {
        cin >> c;
        //cout << c << endl;

        ans.push_back(c);
        appeared[char2num(c)] ++;
        size ++;
        if (size > 1)
        {
            while (combine[char2num(ans[size-1])][char2num(ans[size-2])] != 0)
            {
                appeared[char2num(ans[size-1])]--;
                appeared[char2num(ans[size-2])]--;
                ans[size-2] = combine[char2num(ans[size-1])][char2num(ans[size-2])];
                appeared[char2num(ans[size-2])]++;
                size--;
                ans.pop_back();
            }

            for (int i=0; i<8; i++)
            {
                if (oppose[char2num(ans[size-1])][i] && appeared[i]>0) reset();
            }
        }
        /*
        for (int i=0; i<size-1; i++)
            {
                cout << ans[i] << ", ";
            }
        if (size > 0) cout << ans[size-1];
        cout << endl;
        */
    }
    for (int i=0; i<size-1; i++)
    {
        fout << ans[i] << ", ";
    }
    if (size > 0) fout << ans[size-1];
}

int main()
{
    ifstream cin(FILE_IN);
    ofstream fout(FILE_OUT);

    cin >> t;
    for (int i=1; i<=t; i++)
    {
        init();
        input(cin);
        fout << "Case #" << i << ": [";
        solve(cin,fout);
        fout << "]" << endl;
    }

    fout.close();
    cin.close();
}
